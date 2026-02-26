import sys
from pathlib import Path

ORIGINAL_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ORIGINAL_DIR))
