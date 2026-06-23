-- RAW LAYER

CREATE TABLE raw_youtube (
    video_id TEXT,
    title TEXT,
    channel_name TEXT,
    published_at TIMESTAMP,
    views BIGINT,
    likes BIGINT,
    comments BIGINT,
    extracted_at TIMESTAMP
);

CREATE TABLE raw_food_orders (
    order_id TEXT,
    customer_id TEXT,
    restaurant_name TEXT,
    order_date TIMESTAMP,
    order_value NUMERIC(10,2),
    delivery_time INT
);

CREATE TABLE raw_healthcare (
    patient_id TEXT,
    hospital_name TEXT,
    admission_date TIMESTAMP,
    discharge_date TIMESTAMP,
    treatment_cost NUMERIC(10,2)
);

CREATE TABLE raw_food_orders (
    id TEXT,
    delivery_person_id TEXT,
    delivery_person_age INT,
    delivery_person_ratings NUMERIC(3,1),

    restaurant_latitude NUMERIC(10,6),
    restaurant_longitude NUMERIC(10,6),

    delivery_location_latitude NUMERIC(10,6),
    delivery_location_longitude NUMERIC(10,6),

    order_date DATE,
    time_ordered TIME,
    time_order_picked TIME,

    weather_conditions TEXT,
    road_traffic_density TEXT,
    vehicle_condition INT,

    type_of_order TEXT,
    type_of_vehicle TEXT,

    multiple_deliveries INT,
    festival TEXT,
    city TEXT,

    time_taken_minutes INT
);

CREATE TABLE raw_healthcare (
    patient_name TEXT,
    age INT,
    gender TEXT,
    blood_type TEXT,
    medical_condition TEXT,

    admission_date DATE,

    doctor TEXT,
    hospital TEXT,

    insurance_provider TEXT,

    billing_amount NUMERIC(12,2),

    room_number INT,

    admission_type TEXT,

    discharge_date DATE,

    medication TEXT,

    test_results TEXT
);