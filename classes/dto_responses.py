# -*- coding: utf-8 -*-
import json

from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, Field

from constants import PROCESS_OK
from .dto_people import People


class ResponseData(BaseModel):
    code: int = Field(default=200, examples=[201, 204, 400, 401, 403])
    message: str = Field(default=PROCESS_OK)
    data: dict | list | object | None = Field(default=People())
    timestamp: datetime = datetime.now()

    def to_json(self):
        return json.dumps(
            {k: self.to_string(v) for k, v in self.__dict__.items() if v},
            sort_keys=False, indent=4, separators=(',', ': ')
        )

    @staticmethod
    def to_string(value: any) -> str:
        return str(value) if type(value) is ObjectId or type(value) is datetime else value
