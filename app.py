# -*- coding: utf-8 -*-
import logging
import time
from inspect import currentframe

from fastapi import FastAPI, Request, Response, status

from classes import Settings, ResponseData
from constants import (APPLICATION_JSON, CONTENT_TYPE, PROCESSING_TIME, TAGS_METADATA, TITLE, SUMMARY, TERMS, CONTACT,
                       DESCRIPTION)
from controller import get_person_by_id_from_cne
from utils import configure_logging

settings = Settings()
log = logging.getLogger(settings.environment)

app = FastAPI(
    openapi_tags=TAGS_METADATA,
    on_startup=[configure_logging],
    title=TITLE,
    description=DESCRIPTION,
    summary=SUMMARY,
    version=settings.version,
    terms_of_service=TERMS,
    contact=CONTACT,
    license_info={
      "name": "Apache 2.0",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.middleware("http")
async def interceptor(request: Request, call_next):
    log.info(f"Starting: {currentframe().f_code.co_name}")
    log.info(f"This is a new request {request.client}")
    s_time = time.time()
    body = ResponseData(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="INTERNAL SERVER ERROR", data=None)

    response = Response(
        content=body.json(exclude_none=True),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        headers={CONTENT_TYPE: APPLICATION_JSON}
    )

    try:
        log.info(request.url.path)
        log.info(request.query_params)

        [log.debug(f"Header! -> {hdr}: {val}") for hdr, val in request.headers.items()]
        response = await call_next(request)

        log.info(f"response_body= {response[0].decode()}")
    except Exception as e:
        log.error(e.__str__())
    finally:
        process_time = "{:f}".format(time.time() - s_time)
        response.headers[PROCESSING_TIME] = str(process_time)

        [log.debug(f"Header! -> {hdr}: {val}") for hdr, val in response.headers.items()]
        log.info(f"Ending: {currentframe().f_code.co_name} code:{response.status_code} time: {process_time}")

        return response


@app.get(path="/electors", tags=["Electors"], response_model=ResponseData)
async def get_elector_data(nid: int, nid_type: str = "V"):
    """

    :param nid: This is the National Identification number
    :param nid_type: Identify the type of citizen Venezuelan national or foreign national
    :return:
    """
    log.info(f"Starting: {currentframe().f_code.co_name}")
    try:
        log.info(f"Ending: {currentframe().f_code.co_name}")
        return await get_person_by_id_from_cne(nid=nid, nid_type=nid_type)
    except Exception as e:
        log.error(e.__str__())
        raise Exception(e.__str__())
