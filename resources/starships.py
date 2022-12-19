from resources.base import ResourceBase
from util.fetch_url_data import hit_url


class Starships(ResourceBase):
    def __init__(self):
        super().__init__()
        self._relative_url = "api/starships"

    @property
    def get_relative_url(self):
        return self.__relative_url

    def get_count(self):
        plural_people_url = self.home_url + self._relative_url
        response = hit_url(plural_people_url)
        result = response.json()
        return result.get("count")

    def get_resource_url(self, resource):
        pass
