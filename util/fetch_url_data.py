import requests
from typing import List


def hit_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response


def fetch_all_data(urls: List) -> List:

    # Two ways to get url data
    # response = requests.request("GET", url, headers=headers, data=payload)
    data = []
    for url in urls:
        response = requests.get(url)
        data.append(response.json())
    return data
