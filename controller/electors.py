# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from classes import People, ResponseData
from classes import Settings
from fastapi import status, Response
from datetime import datetime
from constants import APPLICATION_JSON, CONTENT_TYPE, CONTENT_LENGTH
from inspect import currentframe

import requests
import logging

settings = Settings()
log = logging.getLogger(settings.environment)


async def get_person_by_id_from_cne(nid_type: str, nid: int) -> Response:
    log.info(f"Starting: {currentframe().f_code.co_name}")
    resp = Response()
    body = ResponseData(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message="There is an error on our side",
        timestamp=datetime.now()
    )
    try:
        payload = {}
        headers = {}
        url = Settings().national_id_url.format(nid_type, nid)
        log.info(url)
        response = requests.request(method="GET", url=url, headers=headers, data=payload)
        html_text = response.text
        info = []
        soup = BeautifulSoup(html_text, features='html.parser')
        table = soup.find("table")

        for line in table:
            data = line.getText().strip()
            if len(data) != 0:
                [info.append(line) for line in data.split('\n') if len(line) > 0]

        if info[1] != "DATOS DEL ELECTOR":
            log.error(info[2])
            body = ResponseData(
                code=status.HTTP_400_BAD_REQUEST,
                message=f"the national id {nid} is invalid",
                timestamp=datetime.now()
            )
        else:
            person = People.get_people_from_cne(_data=info)
            body = ResponseData(
                code=status.HTTP_200_OK,
                message=f"the national id {nid} is a valid one",
                data=person.__dict__,
                timestamp=datetime.now()
            )

    except Exception as e:
        log.error(e.__str__())

    finally:
        resp.status_code = body.code
        resp.body = body.to_json()
        resp.headers[CONTENT_LENGTH] = str(len(body.to_json()))
        resp.headers[CONTENT_TYPE] = APPLICATION_JSON
        log.info(f"Ending: {currentframe().f_code.co_name}")
        return resp
