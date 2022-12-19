"""The Star Wars API lists 82 main characters in the Star Wars saga. For the first task,
we would like you to use a random number generator that picks a number between 1-82.
Using these random numbers you will be pulling 15 characters from the API using Python."""

import requests
from util.randgen import ProduceChars

start = 1
stop = 83

obj = ProduceChars(start, stop)
characters = []

for i in obj:
    characters.append(i)
print(characters)

if __name__ == "__main__":

    print("Current module getting executed")

    home_url = "https://swapi.dev"
    relative = "/api/people/{0}"

    for num_ in characters:
        absolute_url = home_url + relative.format(num_)
        print(f"fetching details using - {absolute_url} =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        print(response)
        print("**********" * 20)



