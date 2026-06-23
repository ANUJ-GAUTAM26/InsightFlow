# InsightFlow Analytics Suite

## Overview

InsightFlow is a portfolio project that demonstrates end-to-end data analytics workflows using Python, PostgreSQL, SQL, Power BI, and the YouTube Data API.

The project consists of three business-focused analytics solutions:

* Healthcare Analytics Dashboard
* Food Delivery Analytics Dashboard
* YouTube Content Analytics Dashboard

The objective is to showcase skills in data extraction, transformation, modeling, analytics, and dashboard development.

---

## Tech Stack

### Programming

* Python

### Database

* PostgreSQL

### Data Processing

* Pandas
* SQLAlchemy

### APIs

* YouTube Data API v3

### Analytics

* SQL
* Power BI

### Environment Management

* Python Virtual Environment
* dotenv

---

## Project Architecture

```text
Data Sources
│
├── Healthcare CSV
├── Food Delivery CSV
└── YouTube API
        │
        ▼
Python Extraction & Loading
        │
        ▼
PostgreSQL Database
        │
        ▼
SQL Transformations & Views
        │
        ▼
Power BI Dashboards
```

---

## Repository Structure

```text
InsightFlow/
│
├── dashboards/
│   ├── Healthcare_Analytics_Dashboard.pbix
│   ├── Food_Delivery_Analytics_Dashboard.pbix
│   └── YouTube_Content_Analytics_Dashboard.pbix
│
├── data/
│   └── raw/
│
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   ├── dashboard_guide.md
│   ├── project_overview.md
│   └── sql_views.md
│
├── screenshots/
│   ├── Healthcare/
│   ├── Food Delivery/
│   └── YouTube/
│
├── sql/
│   └── schema/
│
├── src/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Dashboard Projects

## 1. Healthcare Analytics Dashboard

### Business Goal

Analyze patient demographics, hospital operations, and financial performance.

### Key Metrics

* Total Patients
* Total Revenue
* Average Billing Amount
* Average Length of Stay

### Insights

* Patient demographics
* Revenue distribution
* Admission trends
* Operational efficiency

---

## 2. Food Delivery Analytics Dashboard

### Business Goal

Analyze delivery operations and identify factors affecting delivery performance.

### Key Metrics

* Total Orders
* Average Delivery Time
* Driver Ratings
* Fast Delivery Percentage

### Insights

* Traffic impact on delivery
* Weather impact on delivery
* Driver performance analysis
* City-wise order distribution
* Vehicle performance comparison

---

## 3. YouTube Content Analytics Dashboard

### Business Goal

Analyze content performance and engagement using YouTube API data.

### Data Collection

Data is collected directly from the YouTube Data API.

Captured metrics include:

* Views
* Likes
* Comments
* Channel Information
* Publish Dates

### Insights

* Top performing videos
* Channel comparison
* Engagement analysis
* Content publishing trends

---

# Database Design

## Raw Layer

Tables:

* raw_healthcare
* raw_food_orders
* raw_youtube

Purpose:

Store original source data.

---

## Staging Layer

Tables:

* stg_healthcare
* stg_food_orders
* stg_youtube

Purpose:

Store cleaned and standardized data.

---

## Analytics Layer

Views:

### Healthcare

* vw_healthcare_patients
* vw_healthcare_finance
* vw_healthcare_operations

### Food Delivery

* vw_food_dashboard
* vw_delivery_performance

### YouTube

* vw_youtube_videos
* vw_youtube_analytics

Purpose:

Provide analytics-ready datasets for Power BI.

---

# Skills Demonstrated

### Data Analytics

* KPI Design
* Dashboard Development
* Data Visualization
* Business Intelligence

### SQL

* Data Modeling
* Aggregations
* Window Functions
* View Creation

### Python

* API Integration
* Data Extraction
* Data Cleaning
* ETL Development

### Database Management

* PostgreSQL
* Relational Data Modeling

---

# Dashboard Screenshots

## Healthcare Dashboard

Screenshots available in:

```text
screenshots/Healthcare/
```

## Food Delivery Dashboard

Screenshots available in:

```text
screenshots/Food Delivery/
```

## YouTube Dashboard

Screenshots available in:

```text
screenshots/YouTube/
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/yourusername/InsightFlow.git
cd InsightFlow
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
YOUTUBE_API_KEY=YOUR_API_KEY

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=insightflow
```

---

# Future Enhancements

* Apache Airflow Automation
* Incremental Loading
* AWS Deployment
* Real-Time Analytics Pipelines
* Advanced Data Quality Checks

---

# Author

Anuj Gautam

Data Analytics & Data Engineering Portfolio Project
