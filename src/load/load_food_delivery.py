import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# =========================
# Load Environment Variables
# =========================

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# =========================
# Database Connection
# =========================

engine = create_engine(
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

# =========================
# Read CSV
# =========================

file_path = "data/raw/food_delivery/food_orders.csv"

df = pd.read_csv(file_path)

print(f"Original Rows: {len(df)}")

# =========================
# Rename Columns
# =========================

df = df.rename(columns={
    "ID": "id",
    "Delivery_person_ID": "delivery_person_id",
    "Delivery_person_Age": "delivery_person_age",
    "Delivery_person_Ratings": "delivery_person_ratings",
    "Restaurant_latitude": "restaurant_latitude",
    "Restaurant_longitude": "restaurant_longitude",
    "Delivery_location_latitude": "delivery_location_latitude",
    "Delivery_location_longitude": "delivery_location_longitude",
    "Order_Date": "order_date",
    "Time_Orderd": "time_ordered",
    "Time_Order_picked": "time_order_picked",
    "Weatherconditions": "weather_conditions",
    "Road_traffic_density": "road_traffic_density",
    "Vehicle_condition": "vehicle_condition",
    "Type_of_order": "type_of_order",
    "Type_of_vehicle": "type_of_vehicle",
    "multiple_deliveries": "multiple_deliveries",
    "Festival": "festival",
    "City": "city",
    "Time_taken(min)": "time_taken_minutes"
})

# =========================
# Clean String Columns
# =========================

text_cols = [
    "id",
    "delivery_person_id",
    "weather_conditions",
    "road_traffic_density",
    "type_of_order",
    "type_of_vehicle",
    "festival",
    "city"
]

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# =========================
# Clean Numeric Columns
# =========================

df["delivery_person_age"] = pd.to_numeric(
    df["delivery_person_age"],
    errors="coerce"
)

df["delivery_person_ratings"] = pd.to_numeric(
    df["delivery_person_ratings"],
    errors="coerce"
)

df["multiple_deliveries"] = pd.to_numeric(
    df["multiple_deliveries"],
    errors="coerce"
)

# Extract number from "(min) 24"
df["time_taken_minutes"] = (
    df["time_taken_minutes"]
    .astype(str)
    .str.extract(r"(\d+)")[0]
)

df["time_taken_minutes"] = pd.to_numeric(
    df["time_taken_minutes"],
    errors="coerce"
)

# =========================
# Clean Dates
# =========================

df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="%d-%m-%Y",
    errors="coerce"
)

# =========================
# Remove Null Records
# =========================

df = df.dropna(
    subset=[
        "id",
        "delivery_person_id",
        "order_date",
        "time_taken_minutes"
    ]
)

# =========================
# Preview Clean Data
# =========================

print("\nCleaned Data Sample:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print(f"\nRows After Cleaning: {len(df)}")

# =========================
# Load Into PostgreSQL
# =========================

df.to_sql(
    "raw_food_orders",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print(f"\n{len(df)} rows loaded successfully into raw_food_orders")