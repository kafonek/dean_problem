from typing import List, Optional

from pydantic import BaseModel, Field


class Animal(BaseModel):
    id: int = Field(alias="animal_ID")
    weight: int = Field(alias="weight_lbs")
    zoo_id: int = Field(alias="zoo_ID")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Zoo(BaseModel):
    id: int = Field(alias="zoo_ID")
    name: str = Field(alias="zoo_name")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
