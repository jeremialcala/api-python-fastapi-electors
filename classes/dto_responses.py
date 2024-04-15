# -*- coding: utf-8 -*-
import json

from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, Field

from constants import PROCESS_OK
from .dto_people import People


class ResponseData(BaseModel):
    code: int = Field(default=200)
    message: str = Field(default=PROCESS_OK)
    data: dict | list | None = Field(default={
        "nationalId": "V-16084690",
        "name": "JEREMI JESUS ALCALA MENESES",
        "state": "DTTO. CAPITAL",
        "county": "MP. BLVNO LIBERTADOR",
        "parrish": "PQ. COCHE",
        "pollCenter": "UNIDAD EDUCATIVA BOLIVARIANA CORONEL CARLOS DELGADO CHALBAUD",
        "address": "URBANIZACIÓN CARLOS DELGADO CHALBAUD FRENTE AVENIDA GUZMAN BLANCO. DERECHA CALLE CENTRAL. "
                   "IZQUIERDA CALLE MIGUEL OTERO SILVA FRENTE A LA CANTV. EDIFICIO"
    })
    timestamp: datetime = datetime.now()

    def to_json(self):
        return json.dumps(
            {k: self.to_string(v) for k, v in self.__dict__.items() if v},
            sort_keys=False, indent=4, separators=(',', ': ')
        )

    @staticmethod
    def to_string(value: any) -> str:
        return str(value) if type(value) is ObjectId or type(value) is datetime else value
