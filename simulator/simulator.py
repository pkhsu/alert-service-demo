import requests
import random
import logging
from time import sleep, time  # make sure to import 'time'
from datetime import datetime, timedelta

# Set logging level and format
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Set the API endpoint URL (using the service name defined in Docker Compose)
api_url = 'http://alertmanager:9093/api/v2/alerts'

# Infinite loop to simulate periodic data sending
while True:
    # Randomly generate temperature and humidity data
    temperature = random.uniform(20, 30)
    humidity = random.uniform(30, 70)

    # Determine the severity based on the temperature
    if temperature > 28:
        severity = 'critical'
    elif temperature > 25:
        severity = 'warning'
    else:
        severity = 'info'

    # Get the current time as the start time
    starts_at = datetime.utcnow()
    # Set an example duration for the alert (e.g., 1 hour)
    ends_at = starts_at + timedelta(hours=1)

    # Format the start and end time in RFC3339 format
    starts_at_str = starts_at.isoformat() + "Z"
    ends_at_str = ends_at.isoformat() + "Z"

    # Create an alert payload
    unique_id = str(int(time()))
    alert_data = [
        {
            "labels": {
                "alertname": "TemperatureHumidityAlert",
                "sensor": "Sensor1",
                "severity": severity,
                "unique_id": unique_id,  # add unique label
            },
            "annotations": {
                "info": f"Temperature: {temperature}, Humidity: {humidity}",
            },
            "startsAt": starts_at_str,
            "endsAt": ends_at_str,
        }
    ]

    try:
        # Send the alert to AlertManager
        response = requests.post(api_url, json=alert_data)
        response.raise_for_status()

        # If sending was successful, log the information
        logging.info(f"Alert sent successfully: Temperature: {temperature}, Humidity: {humidity}, Severity: {severity}")
    except requests.exceptions.HTTPError as http_err:
        # Log HTTP error information
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        # Log other error information
        logging.error(f'An error occurred: {err}')

    # Pause for a while, e.g., send data every 30 seconds
    sleep(30)
