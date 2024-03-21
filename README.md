
# alert-service-demo
Demo alert service with Prometheus AlertManager &amp; Grafana.
This project implements an alert system for monitoring temperature and humidity using Prometheus Alertmanager, a simulator for generating metrics, and a local SMTP server for email notifications. 

## Architecture Diagram

![Architecture Diagram](https://i.imgur.com/ZWwJ5u9.png)

## Overview

The system simulates temperature and humidity data, sending alerts based on predefined thresholds. Alertmanager handles these alerts, routing them to appropriate receivers based on severity and other conditions. For local testing, a Docker-based SMTP server is included to capture outgoing emails.

## Components

- **Alertmanager**: Alertmanager is configured to process alerts based on their severity, with specific routing for critical, warning, and info levels. A unique inhibition rule is set to silence info level alerts when critical alerts are active. Alertmanager is also configured to send notifications via a local SMTP server for testing purposes.
- **Simulator**: The simulator generates temperature and humidity readings, sending alerts to Alertmanager with varying severities. It includes logic to uniquely identify each alert instance for precise tracking.
- **Local SMTP Server**: A lightweight SMTP server is used to intercept and log email notifications sent by Alertmanager, facilitating easy testing of email alerts.

## Usage

To start all components of the system, navigate to the directory containing your `docker-compose.yml` file and run the following command:

```bash
docker compose up -d
```

After starting the project, you can interact with the Alertmanager UI by visiting:
```html
http://localhost:9093
```
You can simulate alerts by running the simulator script, which will automatically send temperature and humidity data to the Alertmanager.
To stop all running services and clean up, use the following command:

```bash
docker compose down
```

## Testing Alerts

Trigger an alert by executing the simulator script. The simulator will automatically send temperature and humidity data to Alertmanager, which in turn routes alerts based on their configured logic.

## Viewing Email Alerts

Instructions on how to view captured email alerts within the SMTP server logs.

