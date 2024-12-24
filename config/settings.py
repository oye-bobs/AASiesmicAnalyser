# config/settings.py
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"

# Processing settings
SAMPLE_RATE = 0.002  # 2ms
MAX_FREQUENCY = 250.0  # Hz
MIN_FREQUENCY = 1.0  # Hz

# Quality control thresholds
QC_SETTINGS = {
    'min_completeness_ratio': 0.95,
    'max_noise_level': 0.1,
    'min_snr': 10.0
}
