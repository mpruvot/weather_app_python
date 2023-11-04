# Python Weather Application

This project is a part of my Python learning journey, focusing on API interaction and data management.

## Introduction

The application is designed to fetch real-time weather data using the WeatherStack API. It's a command-line tool that allows users to input a city name and receive current weather details for that location.

## Features

- **Real-time Weather Data**: Fetch weather information such as temperature, wind speed, and weather descriptions.
- **Error Handling**: Custom exceptions to handle specific error scenarios.
- **Data Persistence**: Save and retrieve historical weather data from a JSON file.
- **Environment Variables**: Use of `.env` for API key management to keep sensitive information secure.
- **Logging**: Implementation of logging to track operations and errors.

## Structure

- `custom_exception.py`: Defines custom exceptions for error handling.
- `main.py`: The main script that runs the application, containing the core functionality.
- `history.json`: A JSON file used to store historical weather data.
- `requirements.txt`: Lists all the Python dependencies required to run the application.

## Usage

To use this application:

1. Clone the repository to your local machine.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Run `main.py` and follow the prompts to input a city name.

## Dependencies

The application requires the following Python packages:

- `requests`: To make API calls.
- `python-dotenv`: To manage environment variables.
- `colorama`: To add color and style to the command-line output.

## Learning Reflection

Building this application has enhanced my understanding of:

- Consuming external APIs in Python.
- Exception handling and custom exceptions.
- File I/O in Python for reading and writing JSON.
- The use of environment variables for configuration.
