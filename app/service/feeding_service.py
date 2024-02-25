from app.repositories.feeding_repo import Feeding_repo
from app.models.feeding import Feeding

class Feeding_service:
    def __init__(self):
        self.feeding_repo = Feeding_repo()

    def get_feedings(self):
        feedings = self.feeding_repo.get_list_feeding()
        return [feeding.as_dict() for feeding in feedings]
    
    def create_feeding(self, feeding_data_dto):
        feeding = Feeding()

        feeding.animal_id = feeding_data_dto.animal_id
        feeding.enclosure_id = feeding_data_dto.enclosure_id
        feeding.time = feeding_data_dto.time
        feeding.food = feeding_data_dto.food

        created_feeding = self.feeding_repo.create_feeding(feeding)
        return created_feeding.as_dict()
