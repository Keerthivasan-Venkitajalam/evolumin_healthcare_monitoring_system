# Remote Health Care Monitoring System

## Overview

The **Remote Health Care Monitoring System** is a project designed to monitor and track vital health parameters remotely using an integrated setup of Arduino Nano 33 IoT and Raspberry Pi. This system collects and processes data such as heart rate, body temperature, oxygen levels, and other essential health metrics in real-time, providing valuable insights for healthcare professionals and caregivers.

The system features a user-friendly interface and secure cloud integration, enabling remote access and monitoring of patient health data. It is an ideal solution for home-based patient care, elderly care, and remote health monitoring scenarios.

## Features

- **Real-Time Monitoring**: Continuously tracks vital health parameters like heart rate, body temperature, and SpO2.
- **IoT Integration**: Uses Arduino Nano 33 IoT to send data to a central server.
- **Data Storage and Analysis**: Raspberry Pi processes data and stores it in a local or cloud database.
- **User Authentication**: Secure login for healthcare professionals and caregivers to access patient data.
- **Alerts and Notifications**: Configurable alerts for abnormal health readings via email or SMS.
- **Data Visualization**: Web dashboard for visualizing health trends over time.

## Project Structure

```
evolumin_healthcare_monitoring_system/
│
├── Binary_Classification_LSTM.ipynb   # Jupyter notebook for data analysis using LSTM model
├── CODES.zip                          # ZIP file containing various project codes
├── README.md                          # Project documentation (this file)
├── extract.py                         # Python script for data extraction
├── healthcare_monitoring_system.zip   # Complete healthcare monitoring system files
├── login.py                           # Python script for user authentication
└── ...                                # Additional project files and directories
```

## Hardware Requirements

- **Arduino Nano 33 IoT**
- **Raspberry Pi (any model with WiFi capability)**
- **Sensors**: Heart rate sensor, temperature sensor, SpO2 sensor, etc.
- **Jumper wires and Breadboard**
- **MicroSD Card (for Raspberry Pi OS)**
- **Power Supply for Raspberry Pi**

## Software Requirements

- **Arduino IDE**: For programming the Arduino Nano 33 IoT.
- **Python 3.x**: Required for running scripts on Raspberry Pi.
- **Raspbian OS**: Operating system for Raspberry Pi.
- **Jupyter Notebook**: For running the `Binary_Classification_LSTM.ipynb`.
- **Blynk App or Custom Dashboard**: For visualizing data.

## Setup Instructions

### 1. Arduino Nano 33 IoT Setup

1. Install the **Arduino IDE** and necessary libraries for the sensors being used.
2. Connect the sensors to the Arduino Nano 33 IoT using jumper wires.
3. Upload the Arduino sketch from the project files to the Nano 33 IoT to read sensor data and send it to the Raspberry Pi.

### 2. Raspberry Pi Setup

1. Install **Raspbian OS** on the Raspberry Pi.
2. Ensure Python 3 and the necessary libraries (`numpy`, `pandas`, `matplotlib`, `scikit-learn`, etc.) are installed.
3. Run `extract.py` to extract data from the Arduino and store it in a local or cloud database.
4. Set up a web server (e.g., Flask or Django) to create a dashboard for data visualization.

### 3. User Authentication

1. Use the `login.py` script to create a secure login page for accessing the dashboard.
2. Set up user roles and permissions for healthcare professionals and caregivers.

### 4. Data Analysis

1. Use the `Binary_Classification_LSTM.ipynb` notebook to analyze the collected data.
2. Train the LSTM model to predict potential health issues based on historical data trends.

## Usage

1. Ensure all hardware components are properly connected and powered.
2. Start the data collection script on the Arduino Nano 33 IoT.
3. Launch the data extraction and processing script on the Raspberry Pi.
4. Access the web dashboard to monitor real-time health data and receive alerts.

## Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request. Contributions are welcome in the form of bug fixes, new features, documentation improvements, or any other enhancements.


## Contact

For any questions, issues, or suggestions, feel free to reach out to [Keerthivasan Venkitajalam](mailto:keerthivasansv2006@outlook.com).

---

