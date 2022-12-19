from util.fetch_url_data import fetch_all_data
from typing import Dict, List
import requests
from util.timimg import timeit

@timeit
def get_all_character_names(result: Dict) ->List:
    """
        returns only names of characters in film 1
        :param result: data of film 1
        :return: names of characters of film 1
    """
    char_urls = result.get("characters")
    char_data = fetch_all_data(char_urls) if char_urls else []
    char_names = [char.get("name") for char in char_data]
    return char_names


@timeit
def get_all_vehicle_names(result: Dict) -> List:
    """
    returns only names of vehicles in film 1
    :param result: data of film 1
    :return: names of vehicles of film 1
    """
    veh_urls = result.get("vehicles")
    veh_data = fetch_all_data(veh_urls) if veh_urls else []
    veh_names = [veh.get("name") for veh in veh_data]
    return veh_names

if __name__ == "__main__":
    url = "https://swapi.py4e.com/api/films/1/"

    payload = {}
    headers = {}
    # Two ways to get url data
    #response = requests.request("GET", url, headers=headers, data=payload)
    response = requests.get(url)
    result = response.json()

    char_names = get_all_character_names(result)
    veh_names = get_all_vehicle_names(result)

    print(char_names)
    print(veh_names)