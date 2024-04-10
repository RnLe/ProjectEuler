import json
from abc import ABC, abstractmethod

class Problem:
    def __init__(self, id: int):
        self.id = id
        self.metadata = self.getMetadataFromId(id)
        
    def getMetadataFromId(self, id: int):
        metadata = {}
        with open('../metadata/titlesAndDescriptions.json') as json_file:
            data = json.load(json_file)
            # TODO: Check format of data and check if function can be made more dynamic
            metadata["title"] = data[str(id)]["title"]
            metadata["description"] = data[str(id)]["description"]
            metadata["answer"] = data[str(id)]["answer"]
            metadata["difficulty"] = data[str(id)]["difficulty"]
            metadata["solved"] = data[str(id)]["solved"]
            metadata["time"] = data[str(id)]["time"]
            
        return metadata
    
    def solve(self, func):
        return func()