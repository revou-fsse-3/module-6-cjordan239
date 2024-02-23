from pydantic import BaseModel, Field
from typing import Optional

class Create_animal_request(BaseModel):
      name: str = Field(...,description="animal name",min_length=3,max_length=50)
      gender: str = Field(None ,description="animal gender")
      age: int = Field(None ,description="animal age")
      diet: str = Field(None ,description="animal diet")