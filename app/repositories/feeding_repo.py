
from app.models.feeding import Feeding

def get_list_feeding():
    feedings = Feeding.query.all()
    return feedings