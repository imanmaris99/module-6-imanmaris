from pydantic import BaseModel, Field
from typing import Optional

class Create_feeding_request(BaseModel):
    animal_id: int = Field(...,description="Animal id")
    enclosure_id: int = Field(..., description="Enclosure id of the animal")
    time: str = Field(...,description="Time to give a feed for animal")
    food: str = Field(...,description="Animal food types",min_length=3,max_length=100)