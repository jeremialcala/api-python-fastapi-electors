# -*- coding: utf-8 -*-
import json
from datetime import datetime
from faker import Faker
from bson import ObjectId
from pydantic import BaseModel, Field

fk = Faker()


class People(BaseModel):
    nationalId: str = Field(default="V-XXXXXXXX")
    name: str = Field(default=fk.name())
    state: str = Field(default="DTTO. CAPITAL")
    county: str = Field(default="MP. BLVNO LIBERTADOR")
    parrish: str = Field(default="PQ. COCHE")
    pollCenter: str = Field(default="UNIDAD EDUCATIVA BOLIVARIANA CORONEL CARLOS DELGADO CHALBAUD")
    address: str = Field(default="URBANIZACIÓN CARLOS DELGADO CHALBAUD FRENTE AVENIDA GUZMAN BLANCO. "
                                 "DERECHA CALLE CENTRAL. "
                                 "IZQUIERDA CALLE MIGUEL OTERO SILVA FRENTE A LA CANTV. EDIFICIO")

    @staticmethod
    def get_people_from_cne(_data: list):
        return People(
            nationalId=_data[3],
            name=_data[5],
            state=_data[7],
            county=_data[9],
            parrish=_data[11],
            center=_data[13],
            address=_data[15]
        )
