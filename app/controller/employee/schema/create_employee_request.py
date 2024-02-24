from pydantic import BaseModel, Field
from typing import Optional

class Create_employee_request(BaseModel):
    name :  str = Field(...,description="Name of employee",min_length=3,max_length=100)
    phone : Optional[int] = Field(None,description="Nomor handphone of employee")
    email : str = Field(...,description="Email of employee",min_length=3,max_length=100)
    role : Optional[str] = Field(None,description="Employee role")
    schedule : Optional[str] = Field(None,description="Schedule work of employee")