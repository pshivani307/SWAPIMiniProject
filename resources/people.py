from resources.base import ResourceBase
from util.fetch_url_data import hit_url


class People(ResourceBase):
    def __init__(self):
        super().__init__()
        self._relative_url = "api/people"
        self._char_range = [1, 82]

    @property
    def get_relative_url(self):
        return self._relative_url

    @property
    def get_home_url(self):
        return self.home_url

    @property
    def get_char_range(self):
        return self.__char_range

    @get_char_range.setter
    def get_char_range(self, rng):
        self.__char_range = rng

    def get_count(self):
        plural_people_url = self.home_url + self._relative_url
        response = hit_url(plural_people_url)
        result = response.json()
        return result.get("count")

    def get_resource_url(self, resource):
        pass
