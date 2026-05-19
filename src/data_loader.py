"""
data_loader.py
--------------
Loads the RadioML 2016.10a dataset from a pickle file,
parses IQ samples and labels, and stores them in SQLite.
"""

import pickle
import numpy as np
import pandas as pd
from pathlib import Path
import yaml
import logging

# ─────────────────────────────────────────
# Logging setup
# ─────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────
# Load config
# ─────────────────────────────────────────
def load_config(config_path: str = "config.yaml") -> dict:
    """Load central project configuration from YAML file."""
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    logger.info("Config loaded successfully")
    return config


# ─────────────────────────────────────────
# Load raw dataset
# ─────────────────────────────────────────
def load_raw_data(file_path: str) -> dict:
    """
    Load the RadioML 2016.10a pickle file.
    
    Parameters
    ----------
    file_path : str
        Path to the .pkl dataset file
        
    Returns
    -------
    dict
        Raw dataset dictionary with (modulation, snr) keys
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at {file_path}")
    
    logger.info(f"Loading dataset from {file_path}")
    
    with open(path, "rb") as f:
        data = pickle.load(f, encoding="latin1")
    
    logger.info(f"Dataset loaded — {len(data)} modulation/SNR combinations")
    return data


# ─────────────────────────────────────────
# Parse into DataFrame
# ─────────────────────────────────────────
def parse_to_dataframe(data: dict) -> pd.DataFrame:
    """
    Convert raw RadioML dict into a clean Pandas DataFrame.
    
    Parameters
    ----------
    data : dict
        Raw dataset dictionary with (modulation, snr) keys
        
    Returns
    -------
    pd.DataFrame
        DataFrame with columns: modulation, snr, iq_samples
    """
    logger.info("Parsing dataset into DataFrame...")
    
    records = []
    for (modulation, snr), samples in data.items():
        for i, sample in enumerate(samples):
            records.append({
                "modulation": modulation,
                "snr": snr,
                "i_samples": sample[0].tolist(),  # In-phase
                "q_samples": sample[1].tolist(),  # Quadrature
            })
    
    df = pd.DataFrame(records)
    logger.info(f"DataFrame created — {len(df):,} rows, {df['modulation'].nunique()} modulation types")
    return df


# ─────────────────────────────────────────
# Summary statistics
# ─────────────────────────────────────────
def get_dataset_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a summary of the dataset by modulation type and SNR.
    
    Parameters
    ----------
    df : pd.DataFrame
        Parsed dataset DataFrame
        
    Returns
    -------
    pd.DataFrame
        Summary DataFrame with counts per modulation and SNR
    """
    summary = df.groupby(["modulation", "snr"]).size().reset_index(name="count")
    logger.info("Dataset summary generated")
    return summary