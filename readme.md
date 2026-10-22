# 🌱 Sustainable Crop Yield Predictor

An interactive machine learning web application built with **Python**, **scikit-learn**, and **Streamlit** that predicts agricultural crop yield (in tons per hectare) from key environmental and cultivation inputs. Developed originally for the **Sustainability & Green Skilling Competition 2024**, the project helps optimize agricultural output while promoting localized water conservation.

**Repository:** [utkarshrajput3914/sustainable-crop-yield-predictor](https://github.com/utkarshrajput3914/sustainable-crop-yield-predictor)

## Key Capabilities

* **Interactive Streamlit Web Dashboard (`app.py`):** Provides real-time sidebar controls for rainfall, temperature, fertilizer application, and cultivation area to generate instant yield predictions in **Ton/Hectare**.
* **Automated Sustainability Guidance:** Evaluates environmental inputs and surfaces targeted irrigation recommendations (such as localized irrigation when rainfall drops below 100 mm) to reduce water waste.
* **End-to-End Model Training Pipeline (`train_model.py`):** Standardizes numerical features using `StandardScaler` and trains a 100-estimator `RandomForestRegressor` (`random_state=42`) on a 2,000-record agricultural dataset, exporting serialized `.pkl` artifacts via `joblib`.
* **Historical Multi-Country Evaluation (`crop_yield.py`):** Includes a secondary benchmarking pipeline trained on 28,242 historical country-level records across 101 countries and 10 major crops (1990–2013) using categorical label encoding.

## Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend & UI** | [Streamlit](https://streamlit.io/) | Interactive web interface, sidebar parameter sliders, and real-time result cards |
| **Machine Learning** | [scikit-learn](https://scikit-learn.org/) | `RandomForestRegressor`, `StandardScaler`, `LabelEncoder`, `train_test_split`, and evaluation metrics |
| **Data Processing** | [pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/) | Tabular dataset ingestion, feature matrix construction, and numerical transformations |
| **Model Serialization** | [Joblib](https://joblib.readthedocs.io/) | Saving and loading pre-trained model (`crop_yield_model.pkl`) and feature scaler (`scaler.pkl`) |
| **Runtime** | [Python 3.10+](https://www.python.org/) | Core execution environment |

## Repository Structure

| File / Folder | Description |
| :--- | :--- |
| `app.py` | Main Streamlit web application loading `crop_yield_model.pkl` and `scaler.pkl` for interactive inference |
| `train_model.py` | Training script that fits `StandardScaler` and `RandomForestRegressor` on `yield_dataset_2000.csv` and saves `.pkl` files |
| `crop_yield.py` | Secondary evaluation script training a Random Forest model on historical country-level crop yield records |
| `yield_dataset_2000.csv` | Primary dataset (2,000 rows, 5 columns) containing environmental features and target yield in tons per hectare |
| `crop_yield_model.pkl` | Pre-trained `RandomForestRegressor` model artifact (`n_estimators=100`, `random_state=42`) |
| `scaler.pkl` | Fitted `StandardScaler` artifact used to normalize user inputs prior to prediction |
| `yield_df.csv/yield_df.csv` | Merged historical dataset (28,242 rows) spanning 101 countries and 10 crop types from 1990 to 2013 |
| `pesticides.csv` | Raw historical pesticide usage dataset (4,349 records in tonnes of active ingredients) |
| `rainfall.csv` | Raw historical average annual rainfall dataset by country and year (6,727 records) |
| `temp.csv.zip`, `yield.csv.zip`, `yield_df.csv.zip` | Compressed archives of raw historical temperature and crop yield datasets |
| `requirements.txt` | Python package dependencies (`streamlit`, `pandas`, `numpy`, `scikit-learn`, `joblib`) |
| `.gitignore` | Excludes local virtual environments (`venv/`, `.venv/`) and `__pycache__/` from version control |

## Datasets & Feature Specifications

### 1. Primary Environmental Dataset (`yield_dataset_2000.csv`)

Used by `train_model.py` and `app.py`. Contains **2,000 records** across four input features and one continuous target variable:

| Column Name | Role | Unit | Dataset Range (Min – Max) | Dataset Mean ± SD | Streamlit UI Input Range |
| :--- | :--- | :--- | ---: | ---: | ---: |
| `Rainfall_mm` | Input Feature | mm | 80.55 – 249.95 | 164.77 ± 49.68 | 50.0 – 300.0 (default: 150.0) |
| `Temperature_C` | Input Feature | °C | 20.00 – 39.99 | 29.93 ± 5.77 | 15.0 – 45.0 (default: 25.0) |
| `Fertilizer_kg` | Input Feature | kg | 50.00 – 199.90 | 124.44 ± 43.19 | 50.0 – 250.0 (default: 120.0) |
| `Area_hectare` | Input Feature | Hectare | 1.00 – 10.00 | 5.39 ± 2.59 | 1.0 – 20.0 (default: 5.0) |
| `Yield_ton_per_hectare` | **Target (`y`)** | Ton/Hectare | 1.24 – 12.77 | 7.20 ± 2.37 | Predicted Output |

### 2. Historical Multi-Country Dataset (`yield_df.csv`)

Used by `crop_yield.py`. Contains **28,242 records** from **1990 to 2013** across **101 countries** and **10 crop varieties** (`Maize`, `Potatoes`, `Rice, paddy`, `Sorghum`, `Soybeans`, `Wheat`, `Cassava`, `Sweet potatoes`, `Plantains and others`, and `Yams`):

* **Features:** `Area` (country, label-encoded), `Item` (crop type, label-encoded), `Year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, and `avg_temp`.
* **Target:** `hg/ha_yield` (hectograms per hectare).

## Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/utkarshrajput3914/sustainable-crop-yield-predictor.git
cd sustainable-crop-yield-predictor
```

### 2. Create and Activate a Virtual Environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train / Refresh Model Artifacts

Rebuilding the model artifacts ensures `crop_yield_model.pkl` and `scaler.pkl` match your local `scikit-learn` and `numpy` versions:

```bash
python train_model.py
```

### 5. Launch the Streamlit Application

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser, adjust the environmental parameters in the left sidebar, and click **Predict Yield**.

## Running the Secondary Historical Script (Optional)

Because `yield_df.csv` is stored inside the `yield_df.csv/` subfolder, copy or extract it into the root folder before running `crop_yield.py`, or update line 8 of `crop_yield.py` to read `'yield_df.csv/yield_df.csv'`:

```powershell
python -c "import pandas as pd; df = pd.read_csv('yield_df.csv/yield_df.csv')"
```

## Deploying to Streamlit Community Cloud

1. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with your GitHub account.
2. Click **Create app** and select `utkarshrajput3914/sustainable-crop-yield-predictor`.
3. Set the **Branch** to `main` and the **Main file path** to `app.py`.
4. Click **Deploy!** to publish a live web URL.
