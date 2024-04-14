# -*- coding: utf-8 -*-

TITLE = "CNE Elector Inquiry"

SUMMARY = "Our API uses BeautifulSoup to scrape a php service response with this citizen poll site information."

TERMS = "https://web-ones.com/terms"

DESCRIPTION = """

We are building an API that inquires about electors from the national council site. 
This API will be developed in Python using FastAPI as the REST framework. 
For now, our API will get elector data from the National Electoral Council of Venezuela (CNE), 
given a national ID number and type, and will find if this person has a valid registration 
to vote and where is the poll center for this citizen.

"""

TAGS_METADATA = [
    {
        "name": "Electors",
        "description": "Data for elector information ",
    }
]

CONTACT = {
    "name": "Jeremi Alcala",
    "url": "https://jeremi.web-ones.com",
    "email": "jeremialcala@gmail.com",
}

