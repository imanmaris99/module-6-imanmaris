
from pydantic import BaseModel, Field
from typing import Optional

class Update_animal_request(BaseModel):
    species: Optional[str] = Field(None,description="Animal species")
    age: Optional[int] = Field(None, description="Enter the age of the animal")
    gender: Optional[str] = Field(None,description="Animal gender")
    special_requirement: str = Field(...,description="Animal special requirement",min_length=3,max_length=100)