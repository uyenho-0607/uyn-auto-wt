import glob
import json
import os
from typing import Dict, Any

import allure

from src.core.config_manager import Config
from src.data.consts import ROOTDIR, GRID_S3_BUCKET_URL
from src.data.project_info import StepLogs
from src.utils.file_utils import save_recorded_video
from src.utils.logging_utils import logger


def capture_and_attach_video(driver):
    """Attach video recording to Allure report based on platform type."""
    platform = Config.get_value("platform")
    
    if platform in ['android', 'ios']:
        # For mobile, get the video directly from Appium
        try:
            video_data = driver.stop_recording_screen()
            video_path = save_recorded_video(video_data)
            allure.attach.file(
                video_path,
                name="Screen Recording",
                attachment_type=allure.attachment_type.MP4 if platform == 'android' else allure.attachment_type.MOV
            )
        except Exception as e:
            logger.error(f"Failed to capture mobile screen recording: {str(e)}")

    else:
        # For web, use Selenium Grid's S3 video
        video_url = f'<a href="{GRID_S3_BUCKET_URL}/videos/{driver.session_id}.mp4">Session Video</a>'
        allure.attach(video_url, name="Screen Recording", attachment_type=allure.attachment_type.HTML)


def capture_and_attach_screenshot(driver, name="screenshot"):
    try:
        allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        logger.error(f"Failed to capture screenshot: {str(e)}")


def log_step_to_allure():
    """Add recorded steps from logger to allure"""
    test_steps = []
    test_steps_log = StepLogs.test_steps

    steps_index = [
        index for index, value in enumerate(test_steps_log) if ("step" or "steps") in value.lower()
    ]

    for i in range(len(steps_index)):
        if i == len(steps_index) - 1:
            test_steps.append(test_steps_log[steps_index[i]:])
            break

        test_steps.append(test_steps_log[steps_index[i]:steps_index[i + 1]])

    for steps in test_steps:
        step = steps.pop(0)
        with allure.step(step):
            for verify in steps:
                with allure.step(verify):
                    pass

    del test_steps_log[:]


def custom_allure_report(allure_dir: str) -> None:
    """Process and customize Allure test result files in the specified directory."""
    allure_dir_path = ROOTDIR / allure_dir
    # get all allure result files
    allure_result_files = [f for f in os.listdir(allure_dir_path) if f.endswith("result.json")]
    # Sort result files based on created time (newest first)
    files = [os.path.join(allure_dir_path, f) for f in allure_result_files]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            _remove_zero_duration(data)

            # Process failed status
            if data["status"] == "failed":
                _process_failed_status(data)

            # Process broken status
            if StepLogs.broken_steps:
                _process_broken_status(data)

            # Clean up and customize report
            _cleanup_and_customize_report(data)

            # Write back the modified data
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            logger.error(f"Error processing file {os.path.basename(file_path)}: {str(type(e).__name__)}, {str(e)}")
            continue


def _process_failed_status(data: Dict[str, Any]) -> None:
    """Process failed test status and update steps."""
    failed_attachments = list(
        filter(lambda x: x["name"] == "screenshot", data.get("attachments", []))
    )

    for item in data.get("steps", []):
        for v_step in item.get("steps", []):
            for failed_step, msg_detail in StepLogs.all_failed_logs:
                # Adjust status of "step" and "verify" -> failed
                if v_step["name"].lower() == failed_step.lower():
                    v_step["status"] = "failed"
                    item["status"] = "failed"

                    # Add failed detailed message to failed verify step
                    v_step.update(statusDetails=dict(message=msg_detail))

                    if failed_attachments:
                        # Add screenshot attachments to failed verify step
                        v_step["attachments"] = failed_attachments[:1]
                        del failed_attachments[:1]

                    break


def _process_broken_status(data: Dict[str, Any]) -> None:
    """Process broken test status and update steps."""

    def __update_step_status(step, step_type="step", attachment=False):
        logger.debug(StepLogs.broken_steps)
        broken_step = next((i for i in StepLogs.broken_steps if step_type in i.lower()), None)
        if not broken_step:
            return

        if step["name"].lower() == broken_step.lower():
            step["status"] = "broken"
            if attachment:
                item["attachments"] = list(
                    filter(lambda x: x["name"] == "broken", data.get("attachments", []))
                )
            StepLogs.broken_steps.remove(broken_step)
        logger.debug(f"{StepLogs.broken_steps} after remove")

    for item in data.get("steps", []):
        __update_step_status(item, attachment=True)

        for v_step in item.get("steps", []):
            __update_step_status(v_step, "verify")

    data["status"] = "broken"  # Adjust status test case -> broken
    data["steps"][-1]["attachments"] = list(
        filter(lambda x: x["name"] == "broken", data.get("attachments", []))
    )


def _cleanup_and_customize_report(data: Dict[str, Any]) -> None:
    """Clean up attachments and customize report details."""
    # Clean up attachments and status details
    if data.get("attachments"):
        data["attachments"] = [
            item for item in data["attachments"] if item["name"] == "Screen Recording"
        ]

    # Remove trace
    data.get("statusDetails", {}).pop("trace", None)

    # Customize test case name
    data["name"] = data["fullName"].split(".")[-1].replace("#test", "")
    data["name"] = " ".join(data["name"].split("_"))

    # Remove server, account Parameters on Allure report
    if data.get("parameters"):
        data["parameters"] = [
            item for item in data["parameters"] if item["name"] not in ["server", "account"]
        ]


def _remove_zero_duration(data: Dict[str, Any]):
    def __update_duration(step):
        start = step.get("start", 0)
        stop = step.get("stop", 0)
        if stop == start:
            step["stop"] += 1

    for item in data.get("steps", []):
        __update_duration(item)

        for v_step in item.get("steps", []):
            __update_duration(v_step)


def clean_allure_log_files(allure_dir):
    """
    Check and delete all .txt log files in the allure-results directory.
    This helps keep the test results clean and prevents accumulation of log files.
    """
    allure_results_dir = ROOTDIR / allure_dir
    if not os.path.exists(allure_dir):
        return

    # Find all .txt files in allure-results directory
    log_files = glob.glob(str(allure_results_dir / '*.txt'))
    
    # Delete each log file
    for log_file in log_files:
        try:
            os.remove(log_file)

        except Exception as e:
            logger.error(f"Error deleting log file {log_file}: {str(e)}")
