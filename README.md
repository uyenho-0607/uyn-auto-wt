# UYN Auto WT - Web and Mobile Test Automation Framework

A robust test automation framework built with Python, supporting both web and mobile application testing using Selenium and Appium.

## 🚀 Features

- Web application testing with Selenium
- Mobile application testing with Appium
- Page Object Model (POM) design pattern
- Allure reporting integration
- Cross-platform support
- Modular and maintainable test structure
- Code quality tools integration (flake8, isort, black)

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd uyn-auto-wt
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Framework Structure

```
uyn-auto-wt/
├── config/                 # Configuration files
├── docs/                  # Documentation
│   ├── test_case_rules.md
│   └── page_object_rules.md
├── src/                   # Source code
│   ├── components/       # Reusable UI components
│   │   ├── web/         # Web components
│   │   │   ├── modals/          # Modal dialogs
│   │   │   ├── notifications/   # Notification components
│   │   │   ├── setting.py       # Settings component
│   │   │   ├── side_bar.py      # Sidebar component
│   │   │   └── tab_bar.py       # Tab bar component
│   │   └── mobile/      # Mobile components
│   │
│   ├── core/            # Core framework functionality
│   │   ├── actions/     # Action implementations
│   │   │   ├── web_actions.py
│   │   │   └── mobile_actions.py
│   │   ├── driver/      # Driver management
│   │   │   ├── web_driver.py
│   │   │   └── mobile_driver.py
│   │   └── config_manager.py
│   │
│   ├── data/            # Test data and constants
│   │   ├── enums.py
│   │   └── ui_messages.py
│   │
│   ├── page_object/     # Page Object classes
│   │   ├── web/        # Web page objects
│   │   │   ├── base_page.py
│   │   │   ├── home_page.py
│   │   │   ├── login_page.py
│   │   │   └── trade_page.py
│   │   └── mobile/     # Mobile page objects
│   │
│   ├── utils/           # Utility functions
│   │   ├── allure_utils.py
│   │   ├── assert_utils.py
│   │   ├── common_utils.py
│   │   ├── logging_utils.py
│   │   └── video_utils.py
│   │
│   └── consts.py        # Global constants
│
├── tests/               # Test cases
│   ├── web/            # Web test cases
│   │   ├── login/      # Login test cases
│   │   └── trade/      # Trade test cases
│   └── mobile/         # Mobile test cases
├── conftest.py         # Pytest configurations
├── pytest.ini          # Pytest settings
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

### Key Components

1. **Components** (`src/components/`)
   - Reusable UI components
   - Web components:
     - Modals (dialog boxes)
     - Notifications
     - Settings
     - Sidebar
     - Tab bar
   - Mobile components: to be updated

2. **Core** (`src/core/`)
   - Framework's core functionality
   - Actions:
     - Web actions
     - Mobile actions
   - Driver management:
     - Web driver
     - Mobile driver
   - Configuration management

3. **Page Objects** (`src/page_object/`)
   - Page Object Model implementation
   - Web pages
   - Mobile pages

4. **Utils** (`src/utils/`)
   - Allure reporting
   - Assertions
   - Common utilities
   - Logging

5. **Tests** (`tests/`)
   - Web tests:
     - Login tests
     - Trade tests
     - ...
   - Mobile tests

6. **Config** (`config/`)
   - Environment configurations files

7. **Docs** (`docs/`)
   - Rules to note for using the framework

## 🧪 Running Tests

### Basic Test Execution

To run all tests with Allure reporting:
```bash
pytest --alluredir=./allure-results
```

To generate and view the Allure report:
```bash
allure serve ./allure-results
```

### Test Execution Examples

Here are some practical examples of running tests with different combinations of options:

```bash
# Run web tests on SIT environment for Lirunex client with MT4 server using demo and live account
pytest --platform=web --env=sit --client=lirunex --server=mt4 --account=demo,live --alluredir=./allure-results

# Run mobile tests on UAT environment with live account and retry failed tests
pytest --platform=mobile --env=uat --account=live --reruns 3 --alluredir=./allure-results

# Run smoke tests on Chrome browser in headless mode
pytest --platform=web --browser=chrome --headless -m "smoke" --alluredir=./allure-results

# Run all login tests
pytest tests/web/login --platform=web --env=sit --alluredir=./allure-results

# Run specific test case
pytest .\tests\web\login\test_LGN_TC01_positive_valid_credentials.py --platform=web --env=sit --alluredir=./allure-results
```

Note: All commands include `--alluredir=./allure-results` for test reporting. You can generate the report after test execution using:
```bash
allure serve ./allure-results
```

## 🛠️ Development Tools

- **Code Quality**:
  - flake8: Linting
  - isort: Import sorting
  - black: Code formatting

- **Testing**:
  - pytest: Test runner
  - pytest-selenium: Selenium integration
  - allure-pytest: Test reporting
  - pytest-check: Additional test features
