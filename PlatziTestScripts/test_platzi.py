from playwright.sync_api import APIRequestContext

from EndPoints.platziEnpoints import EndPoints
import EndPoints.logger as log


def test_get_product_api_details(api_request_context: APIRequestContext) -> None:

    product_headers = {"Content-Type": "application/json"}
    product_response = api_request_context.get(url=EndPoints.get_all_products_endpoint, headers=product_headers)
    assert product_response.status == 200
    response = product_response.json()
    log.logger.info("Get Product API Response:\n{}".format(response))


def test_create_new_product(api_request_context: APIRequestContext) -> None:

    product_body = {

        "title": "Platzi Create New Product",
        "price": 1000,
        "description": "Platzi Create Product",
        "categoryId": 1,
        "images": ["https://placeimg.com/640/480/any"]
    }
    product_headers = {"Content-Type": "application/json"}
    product_response = api_request_context.post(url=EndPoints.create_product_endpoint,
                                                headers=product_headers,
                                                data=product_body)
    assert product_response.status == 201
    response = product_response.json()
    log.logger.info("New Product Response:\n".format(product_response.json()))

    assert response.get("title") == product_body.get("title")
    assert response.get("price") == product_body.get("price")

