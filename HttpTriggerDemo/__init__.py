import logging

import azure.functions as func
from urllib.request import Request, urlopen
import xmltodict, json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    urls = req.params.get('url')
    requests = Request(
        url=urls, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(requests).read()

    x = json.dumps(xmltodict.parse(webpage))


    if not urls:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            urls = req_body.get('url')

    if urls:
        return func.HttpResponse(x)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully.",
             status_code=200
        )
