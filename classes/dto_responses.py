# -*- coding: utf-8 -*-
from datetime import datetime
from pydantic import BaseModel, Field
from constants import PROCESS_OK
from .dto_people import People


class ResponseData(BaseModel):
    code: int = Field(default=200, examples=[201, 204, 400, 401, 403])
    message: str = Field(default=PROCESS_OK)
    data: dict | list | object | None = Field(default=People())
    timestamp: datetime = datetime.now()
