from enum import Enum

class criterion_choice(str, Enum):
    """Class to define criterion options"""
    pending = "pending"
    completed = "completed"
    canceled = "canceled"
    all = "all"