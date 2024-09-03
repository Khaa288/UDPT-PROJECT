from dataclasses import dataclass
from src.models.category_model import Category
from src.models.brand_model import Brand 

@dataclass
class Gift():
    GiftId: int
    Name: str
    # Category: Category # type: ignore
    Brand: Brand # type: ignore
    Detail: [] # type: ignore
    
    def __init__(self, giftId, name, brand):
        self.GiftId = giftId
        self.Name = name
        # self.Category = category
        self.Brand = brand
        self.Detail = []

    

    
        