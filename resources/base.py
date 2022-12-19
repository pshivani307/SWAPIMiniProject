from abc import ABC, abstractmethod
not_implemented_error_msg = "This method is has not been implemented"


class ResourceBase(ABC):

    resources = [
        "Films", "People", "Planets", "Species", "Starships", "Vehicles"]

    def __init__(self):
        self.home_url = "https://swapi.dev/"

    @abstractmethod
    def get_count(self):
        raise NotImplementedError(not_implemented_error_msg)

    @abstractmethod
    def get_resource_url(self, resource):
        raise NotImplementedError(not_implemented_error_msg)
