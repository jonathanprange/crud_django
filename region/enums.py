from enum import Enum

class RegionType(Enum):
    NEIGHBORHOOD = "NEIGHBORHOOD"
    CITY = "CITY"
    STATE = "STATE"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
        