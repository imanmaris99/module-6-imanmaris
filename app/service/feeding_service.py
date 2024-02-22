
from app.repositories import feeding_repo

def get_feedings():
    feedings = feeding_repo.get_list_feeding()
    return [feeding.as_dict() for feeding in feedings], 200