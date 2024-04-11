import json
from abc import ABC, abstractmethod
import time

# Example metadata format
"""{
    "id": "",
    "title": "",
    "description": "",
    "answer": "",
    "difficulty": "",
    "solved": "",
    "time": ""
}"""

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
        # Time the function in ms
        start = time.time()
        result = func()
        end = time.time()
        
        final_time = (end-start)*1000
        
        if result == int(self.metadata["answer"]):
            print("Correct answer!")
            # TODO: Write time to metadata and json file
        else:
            print("Incorrect answer!")
            
        print("Result: ", result)
        print("Correct answer: ", self.metadata["answer"])
        print("Time taken: ", final_time, "ms")
        
        return result, final_time