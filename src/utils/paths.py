"""
Centralised project paths.

This module provides a single source of truth for all directories used
throughout the PayFlow Intelligence Platform.

Author: SimbaraShe Munatsi
Project: PayFlow Intelligence Platform
"""

from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
LANDING_DATA_DIR = DATA_DIR / "landing"
STAGING_DATA_DIR = DATA_DIR / "staging"
WAREHOUSE_DATA_DIR = DATA_DIR / "warehouse"

# Logs
LOGS_DIR = PROJECT_ROOT / "logs"

# Documentation
DOCS_DIR = PROJECT_ROOT / "docs"

# Create directories automatically if they don't exist
DIRECTORIES = [
    LANDING_DATA_DIR,
    STAGING_DATA_DIR,
    WAREHOUSE_DATA_DIR,
    LOGS_DIR,
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)