
from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import ClassVar
class Spieler(BaseModel):
    anzahl_Spieler : ClassVar[int] = 0
    name : str = Field(default="None")
    position : str = Field(default="None")
    motivation : int = Field(default=5, ge=1, le=10)

    def model_post_init(self, __context):
        Spieler.anzahl_Spieler += 1
        print(Spieler.anzahl_Spieler)

    model_config = {"validate_assignment": True}
    

#s = Spieler(name="Jan", position="Sturm", motivation=10)
#print(s.model_dump)
