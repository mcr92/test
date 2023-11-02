from pydantic import BaseModel, Field
from enum import Enum
from decimal import Decimal 

class status_choice(str, Enum):
    """Class to define status options"""
    pending = "pending"
    completed = "completed"
    canceled = "canceled"
    
class Orders(BaseModel):
    """Class to define the parameters of the Orders"""  
    id: int = Field(gt=0, description="An integer representing the order ID")
    item: str = Field(description="A string representing the item name")
    quantity: int = Field(ge=0, description="An integer representing the number of items in the order")
    price: Decimal = Field(gt=0, max_digits=11, decimal_places=2, description="The price must be greater than zero")
    status : status_choice = Field(description="A string representing the order status")