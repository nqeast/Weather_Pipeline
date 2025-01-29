import requests
import pandas as pd

# API Key and Base URL
api_key = "fakeforsecuirty"
base_url = "http://api.openweathermap.org/data/2.5/forecast"

# Cities and their coordinates
cities = {
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Los Angeles": {"lat": 34.0522, "lon": -118.2437}
}

# Fetch data function
def fetch_forecast_data(city_name, lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        forecast_list = data["list"]
        processed_data = []
        for entry in forecast_list:
            processed_data.append({
                "city": city_name,
                "datetime": entry["dt_txt"],
                "temperature": entry["main"]["temp"],
                "humidity": entry["main"]["humidity"],
                "weather": entry["weather"][0]["description"]
            })
        return processed_data
    else:
        print(f"Failed to fetch data for {city_name}. Status Code: {response.status_code}")
        return None

# Collect data for all cities
all_forecast_data = []

for city, coords in cities.items():
    city_data = fetch_forecast_data(city, coords["lat"], coords["lon"])
    if city_data:
        all_forecast_data.extend(city_data)

# Convert to DataFrame
forecast_df = pd.DataFrame(all_forecast_data)

# Clean data: Ensure datetime is in proper format
forecast_df['datetime'] = pd.to_datetime(forecast_df['datetime'])

# Preview the DataFrame
print(forecast_df.head())

import psycopg2

# Database connection details
db_config = {
    "host": "fakeforsecuirty",         # Or your cloud DB host (e.g., Heroku)
    "database": "fakeforsecuirty",  # Database name
    "user": "fakeforsecuirty",     # Replace with your username
    "password": "fakeforsecurity"  # Replace with your password
}

# Function to insert data into PostgreSQL
def load_data_to_postgres(df, table_name):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Insert each row into the table
        for _, row in df.iterrows():
            cursor.execute(f"""
                INSERT INTO {table_name} (city, datetime, temperature, humidity, weather)
                VALUES (%s, %s, %s, %s, %s)
            """, (row['city'], row['datetime'], row['temperature'], row['humidity'], row['weather']))

        # Commit and close connection
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Data successfully loaded into {table_name}!")
    except Exception as e:
        print("Error while inserting data:", e)

# Load data to PostgreSQL
load_data_to_postgres(forecast_df, "forecast")
