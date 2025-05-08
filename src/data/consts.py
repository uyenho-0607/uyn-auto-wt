from pathlib import Path

ROOTDIR = Path(__file__).parent.parent.parent
CONFIG_DIR = ROOTDIR / "config"
GRID_SERVER = "http://aqdev:aq123@selenium-grid.aquariux.dev/wd/hub"
EXPLICIT_WAIT = 10  # sec
