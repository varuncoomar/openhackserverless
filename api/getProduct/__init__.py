import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function getProduct processed a request.')

    name = req.params.get('productId')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('productId')

    if name:
        return func.HttpResponse(f"The product name for your product id {name} is Starfruit Explosion")
    else:
        return func.HttpResponse(
             "AVACADO, It is a scam fruit!!!.",
             status_code=200
        )
