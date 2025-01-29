# Weather Pipeline Project

## Overview
This project demonstrates data engineering skills by building an end-to-end weather data pipeline. The pipeline collects weather forecast data from the OpenWeatherMap API, processes and transforms the data, stores it in a PostgreSQL database, and visualizes the results. 

## Features
- **Data Collection**: Fetches real-time weather forecast data for London and Los Angeles from the OpenWeatherMap API.
- **ETL Process**:
  - **Extract**: Retrieves JSON data from the API.
  - **Transform**: Normalizes and cleans data, extracting key features (temperature, humidity, weather conditions).
  - **Load**: Stores the transformed data into a PostgreSQL database.
- **Automation**: The ETL process can be scheduled to run automatically using Python's `schedule` library or a cron job.
- **Visualization**: Data is analyzed and visualized using Matplotlib and Seaborn.

## Technologies Used
- **Python**: For scripting the ETL pipeline.
- **PostgreSQL**: For storing historical weather data.
- **Pandas**: For data transformation and analysis.
- **Requests**: For fetching data from the API.
- **Matplotlib & Seaborn**: For creating data visualizations.
- **Git & GitHub**: For version control and collaboration.
- **Jupyter Notebook**: Used for initial testing and prototyping.

## Data Visualization
Once data is stored in PostgreSQL, visualizations can be generated using:

**Example plots:**
- Temperature trends over time.
- Weather condition frequency.
- Comparison of humidity levels between cities.

## Future Enhancements
- Deploy a Streamlit dashboard for real-time weather analytics.
- Extend the pipeline to collect data for more cities.
- Implement Airflow for advanced scheduling and monitoring.
