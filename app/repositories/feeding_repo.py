
from app.models.feeding import Feeding
from app.utils.database import db

class Feeding_repo():
    def get_list_feeding(self):
        feedings = Feeding.query.all()
        return feedings
    
    def create_feeding(self, feeding):
        db.session.add(feeding)
        db.session.commit()
        return feeding