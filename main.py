from typing import Any
import requests
import json
import logging
import os
from dotenv import load_dotenv
from colorama import Fore
from custom_exception import *


## Decorateur
## Debut de projet en FastAPI
## 
logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

load_dotenv()
key = os.getenv("WEATHER_API_KEY")


class CityWeather:
    """Class to store weather information for a city"""
    def __init__(
        self, city, country, region, local_time, temp, icon, description, wind_speed
    ):
        self.city = city
        self._country = country
        self.region = region
        self.local_time = local_time
        self._temp = temp
        self.icon = icon
        self.description = description
        self.wind_speed = wind_speed

    def display_infos(self):
        """Display all weather information"""
        for i in vars(self):
            print(f"{i} : {vars(self)[i]}")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if not isinstance(value, str) or value == "":
            logging.error("Invalid country value")
            raise EmptyStringError("Country should not be empty or non-string")
        else:
            self._country = value

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if not isinstance(value, (int, float)):
            logging.error("Invalid temperature value provided")
            raise ValueError("Temperature must be a number")
        else:
            self._temp = value


class WeatherFinder:
    def __init__(self) -> None:
        pass

    def get_city(self, city: str) -> CityWeather:
        """Get city informations from the WeatherStack API

        Args:
            city (str): city name

        Returns:
            CityWeather: Object cityWeather to store the informations
        """
        try:
            ### localhost/user/
            ### definir une fonction -> appele quand on fait un get sur /toto/

            response = requests.get(
                f"http://api.weatherstack.com/current",
                params={
                    "access_key":key,
                    "query": city,
                }
            )
            response.raise_for_status()
            r = response.json()
            logging.info("Success")

            name = r.get("location", {}).get("name") ################
            country = r.get("location").get("country")
            region = r.get("location").get("region")
            local_time = r.get("location").get("localtime")
            temp = r.get("current").get("temperature")
            icon = r.get("current").get("weather_icons")
            description = r.get("current").get("weather_descriptions")
            wind_speed = r.get("current").get("wind_speed")

            return CityWeather(
                name, country, region, local_time, temp, icon, description, wind_speed
            )

        except requests.exceptions.HTTPError as err:
            logging.exception(err)
            raise
        except AttributeError as e:
            logging.exception(e)
            raise


class History:
    """Class To save history into Json format"""

    def __init__(self):
        self._records = []
        self._file_path = "history.json"
        self.read_from_file()

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if not isinstance(value, list):
            logging.error(ValueError)
            raise ValueError
        else:
            self._records = value

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if value.endswith(".json"):
            self._file_path = value
        else:
            logging.error(FileExtensionError)
            raise FileExtensionError

    def update_json(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
            data.extend(self.records)
            with open(self.file_path, "w") as f:
                json.dump(data, f)
            self.records = []
        except FileNotFoundError as e:
            logging.exception(e)
            raise
        except PermissionError as e:
            logging.exception(e)
            raise

    def add(self, user_input: str):
        try:
            self.records.append(user_input)
        except Exception as e:
            logging.exception(e)
            raise

    def read_from_file(self):
        try:
            with open(self.file_path, "r") as f:
                self.records = json.load(f)
        except FileNotFoundError:
            logging.exception("Fichier introuvable")
        except json.JSONDecodeError:
            logging.exception("Erreur de décodage JSON")

    def print_history(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
            for i in data:
                print(i)
        except FileNotFoundError as e:
            logging.exception(e)
            raise
        except PermissionError as e:
            logging.exception(e)
            raise

    def clear_history(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([], f)
        except FileNotFoundError:
            logging.exception("Fichier introuvable")
        except json.JSONDecodeError:
            logging.exception("Erreur de décodage JSON")
