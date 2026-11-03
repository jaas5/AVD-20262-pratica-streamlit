from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data(max_entries=1)
def load_data(path="data/clean/dataset.csv"):
    """Lê o dataset já tratado (exportado ao final do notebook de EDA)."""
    data_path = Path(path)
    if not data_path.is_absolute():
        data_path = Path(__file__).resolve().parents[1] / data_path
    return pd.read_csv(data_path)
