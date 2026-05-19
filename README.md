# 📡 RF Signal Classification

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

An end-to-end data science pipeline to classify Radio Frequency (RF) signals 
by their modulation type using the RadioML 2016.10a dataset.

---

## 🎯 Problem Statement
Modern wireless systems need to automatically identify signal modulation types 
in real time. This project builds a complete pipeline — from raw IQ samples to 
a deployed classifier — mimicking what engineers build in telecom, defense, and IoT.

---

## 📊 Dataset
- **Source:** RadioML 2016.10a (DeepSig)
- **Signals:** 11 modulation types (AM, FM, BPSK, QPSK, 8PSK, QAM16, QAM64, WBFM, AM-DSB, AM-SSB, CPFSK)
- **SNR range:** -20dB to +18dB
- **Total samples:** 220,000 IQ signals

---

## 🛠️ Tech Stack
| Category | Tools |
|---|---|
| Language | Python 3.12 |
| Data Processing | NumPy, Pandas, SciPy |
| Signal Processing | FFT, PSD, Constellation diagrams |
| Database | SQLite, SQLAlchemy |
| Machine Learning | Scikit-learn, XGBoost, Optuna |
| Explainability | SHAP |
| Visualization | Plotly, Seaborn, Bokeh |
| Web App | Streamlit |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Publishing | Quarto Book |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12
- pyenv
- Git

### Installation
```bash
git clone https://github.com/charldelaoa/rf-signal-classifier.git
cd rf-signal-classifier
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Download Dataset
```bash
pip install gdown
cd data/raw
gdown "https://drive.google.com/uc?id=0B4OkPDkSMJKGWlBadTlwemVCZGs"
```

---