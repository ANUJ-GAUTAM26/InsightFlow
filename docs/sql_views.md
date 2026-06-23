# SQL Views Documentation

## Healthcare Views

### vw_healthcare_patients

Purpose:
Patient-level analytics and demographic analysis.

Contains:

* Age
* Gender
* Blood Type
* Medical Condition
* Admission Type

### vw_healthcare_finance

Purpose:
Financial and billing analytics.

Contains:

* Billing Amount
* Insurance Provider
* Revenue Metrics
* Financial Aggregations

### vw_healthcare_operations

Purpose:
Hospital operational performance.

Contains:

* Length of Stay
* Admissions
* Discharges
* Department Metrics

---

## YouTube Views

### vw_youtube_videos

Purpose:
Video-level analytics.

Contains:

* Video Title
* Channel Name
* Views
* Likes
* Comments
* Publish Date
* Engagement Rate

### vw_youtube_analytics

Purpose:
Aggregated channel analytics.

Contains:

* Channel Metrics
* Total Views
* Total Likes
* Total Comments
* Average Engagement

---

## Food Delivery Views

### vw_food_dashboard

Purpose:
Primary dashboard dataset.

Contains:

* Order Information
* Delivery Information
* Driver Information
* Vehicle Information
* Traffic Information
* Weather Information

### vw_delivery_performance

Purpose:
Delivery performance analysis.

Contains:

* Delivery Time Metrics
* Traffic Impact Metrics
* Weather Impact Metrics
* Vehicle Performance Metrics

---

## Data Flow

Raw Data

↓

Staging Tables

↓

SQL Transformations

↓

Analytics Views

↓

Power BI Dashboards

---

## Database Tables

### raw_healthcare

Stores original healthcare records.

### stg_healthcare

Stores cleaned healthcare data.

### raw_food_orders

Stores original food delivery records.

### stg_food_orders

Stores cleaned food delivery data.

### raw_youtube

Stores extracted YouTube API data.

### stg_youtube

Stores transformed YouTube analytics data.

---

## Dashboard Data Sources

Healthcare Dashboard:

* vw_healthcare_patients
* vw_healthcare_finance
* vw_healthcare_operations

YouTube Dashboard:

* vw_youtube_videos
* vw_youtube_analytics

Food Delivery Dashboard:

* vw_food_dashboard
* vw_delivery_performance
