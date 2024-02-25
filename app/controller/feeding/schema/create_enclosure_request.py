from pydantic import BaseModel, Field
from typing import Optional

class Create_enclosure_request(BaseModel):
    location: str = Field(...,description="Animal enclosure location",min_length=5,max_length=100)