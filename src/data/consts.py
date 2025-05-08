from pathlib import Path

# Framework Paths
ROOTDIR = Path(__file__).parent.parent.parent
CONFIG_DIR = ROOTDIR / "config"
VIDEO_DIR = ROOTDIR / ".videos"

# Grid Configuration
GRID_SERVER = "http://aqdev:aq123@selenium-grid.aquariux.dev/wd/hub"
GRID_S3_BUCKET_URL = "https://selenium-grid-videos.aquariux.dev"
# Timeouts (in seconds)
EXPLICIT_WAIT = 10 
IMPLICIT_WAIT = 0
PAGE_LOAD_WAIT = 30
SHORT_WAIT = 5
