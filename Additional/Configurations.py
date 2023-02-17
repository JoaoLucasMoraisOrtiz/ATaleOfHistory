import json
from collections import namedtuple
from json import JSONEncoder


class Helper:

    def getConfigs():
        f = open('option.json')

        config = json.loads(f.read())
        return config

