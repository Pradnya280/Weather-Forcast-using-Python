# -*- coding: utf-8 -*-
"""weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WL0ziunMPowSVW9nk6MxYFxrfakgP6co
"""

import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Failed to fetch weather data.")
        return []

def get_weather_by_date(data, target_date):
    for item in data:
        if item["dt_txt"].startswith(target_date):
            return item["main"]["temp"]
    return None

def get_wind_speed_by_date(data, target_date):
    for item in data:
        if item["dt_txt"].startswith(target_date):
            return item["wind"]["speed"]
    return None

def get_pressure_by_date(data, target_date):
    for item in data:
        if item["dt_txt"].startswith(target_date):
            return item["main"]["pressure"]
    return None

def main():
    data = get_weather_data()

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            target_date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_by_date(data, target_date)
            if temperature is not None:
                print(f"Temperature on {target_date}: {temperature}°C")
            else:
                print("Weather data not available for the specified date.")
        elif choice == "2":
            target_date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed on {target_date}: {wind_speed} m/s")
            else:
                print("Wind speed data not available for the specified date.")
        elif choice == "3":
            target_date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(data, target_date)
            if pressure is not None:
                print(f"Pressure on {target_date}: {pressure} hPa")
            else:
                print("Pressure data not available for the specified date.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()