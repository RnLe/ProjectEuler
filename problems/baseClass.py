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
            metadata["title"]       = data[id-1]["title"]
            metadata["description"] = data[id-1]["description"]
            metadata["answer"]      = data[id-1]["answer"]
            metadata["difficulty"]  = data[id-1]["difficulty"]
            metadata["solved"]      = data[id-1]["solved"]
            metadata["time"]        = data[id-1]["time"]
            
        return metadata
    
    def solve(self, func):
        return func()