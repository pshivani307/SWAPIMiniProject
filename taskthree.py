import argparse

from resources.species import Species
from resources.films import Films
from resources.people import People
from resources.planets import Planets
from resources.starships import Starships
from resources.vehicles import Vehicles
from util.randgen import ProduceChars
from util.fetch_url_data import hit_url


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SWAPI Project CLI")
    parser.add_argument('task_list', help="task1: get count of all resources"
                                            "\ntask2 : get random 3 data"
                                            "\ntask3: get url of all resources")
    #parser.add_argument('task_2', help="get random 3 data from all resources")
    #parser.add_argument('task_3', help="get url of all resources")

    args = parser.parse_args()
    #print(args)
    if args.task_list == "task_1":
        print("Getting count of all resources")
        print(f"Species Count : {Species().get_count()}")
        print(f"Films Count : {Films().get_count()}")
        print(f"People Count : {People().get_count()}")
        print(f"Planets Count : {Planets().get_count()}")
        print(f"Starships Count : {Starships().get_count()}")
        print(f"Vehicles Count : {Vehicles().get_count()}")
    elif args.task_list == "task_2":
        obj = ProduceChars(1,20)
        for i in obj:
            url = People().home_url+(People()._relative_url)+"/"+str(i)
            print(url)
            res = hit_url(url)
            print(res.json())
        pass
    elif args.task_list == "task_3":
        print(f"People relative URL : {People()._relative_url}")
        print(f"Films relative URL : {Films()._relative_url}")
        print(f"Planets relative URL : {Planets()._relative_url}")
        print(f"Species relative URL : {Species()._relative_url}")
        print(f"Starships relative URL : {Starships()._relative_url}")
        print(f"Vehicles relative URL : {Vehicles()._relative_url}")

