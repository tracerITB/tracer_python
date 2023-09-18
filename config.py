import json

class Config:
    def __init__(self, filename):
        f = open(filename)
        self.config = json.load(f)
    
    def get_config(self):
        return self.config