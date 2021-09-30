# This file is for the pokemon object

class Pokemon:
    name = ""
    id = ""
    types = []
    encounter_locations = []
    methods = []
    stats = {}

    def __str__(self) -> str:
        return self.name

    def get_info(self) -> str:
        # TODO:
        # return a string representation of relevant info
        return self.name