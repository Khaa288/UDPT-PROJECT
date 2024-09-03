from dataclasses import dataclass

@dataclass
class Brand():
    Id: int
    Title: str
    
    def __init__(self, id, title):
        if (id == "0" or id is None):
            self.Id = id
            self.Title = 'Unkown'

        self.Id = id
        self.Title = title
        