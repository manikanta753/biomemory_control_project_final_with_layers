# BioMemory-Control

A safe software simulation project that combines:

1. Artificial DNA-style data storage
2. Mutation simulation during repeated cell division
3. Cancer-like abnormal growth detection
4. Streamlit dashboard visualization

This is a **computer simulation only**. It does not provide biological experimentation, gene editing, or wet-lab protocols.

## Features

- Convert text into DNA bases: A, T, C, G
- Decode DNA back into text
- Add checksum for data verification
- Simulate mutations during repeated cell divisions
- Detect cancer-like behavior using rule-based logic
- Show charts for mutation rate and division risk
- Simple Streamlit web app

## Installation

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

## Files

- `app.py` - Streamlit dashboard
- `dna_storage.py` - DNA encoding and decoding logic
- `cell_simulation.py` - Mutation and cell division simulation
- `detector.py` - Cancer-like growth detection logic
- `requirements.txt` - Python dependencies
