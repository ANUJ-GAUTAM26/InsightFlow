import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# =========================
# Load Environment Variables
# =========================

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

# =========================
# Read CSV
# =========================

df = pd.read_csv(
    "data/raw/healthcare/healthcare_dataset.csv"
)

print(f"Original Rows: {len(df)}")

# =========================
# Rename Columns
# =========================

df = df.rename(columns={
    "Name": "name",
    "Age": "age",
    "Gender": "gender",
    "Blood Type": "blood_type",
    "Medical Condition": "medical_condition",
    "Date of Admission": "date_of_admission",
    "Doctor": "doctor",
    "Hospital": "hospital",
    "Insurance Provider": "insurance_provider",
    "Billing Amount": "billing_amount",
    "Room Number": "room_number",
    "Admission Type": "admission_type",
    "Discharge Date": "discharge_date",
    "Medication": "medication",
    "Test Results": "test_results"
})

# =========================
# Clean Strings
# =========================

text_cols = [
    "name",
    "gender",
    "blood_type",
    "medical_condition",
    "doctor",
    "hospital",
    "insurance_provider",
    "admission_type",
    "medication",
    "test_results"
]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# =========================
# Clean Numeric Columns
# =========================

df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)

df["billing_amount"] = pd.to_numeric(
    df["billing_amount"],
    errors="coerce"
)

df["room_number"] = pd.to_numeric(
    df["room_number"],
    errors="coerce"
)

# =========================
# Convert Dates
# =========================

df["date_of_admission"] = pd.to_datetime(
    df["date_of_admission"],
    errors="coerce"
)

df["discharge_date"] = pd.to_datetime(
    df["discharge_date"],
    errors="coerce"
)

# =========================
# Remove Null Records
# =========================

df = df.dropna(
    subset=[
        "name",
        "age",
        "date_of_admission",
        "discharge_date"
    ]
)

print(f"Rows After Cleaning: {len(df)}")

# =========================
# Load to PostgreSQL
# =========================

df.to_sql(
    "raw_healthcare",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print(
    f"{len(df)} rows loaded successfully into raw_healthcare"
)