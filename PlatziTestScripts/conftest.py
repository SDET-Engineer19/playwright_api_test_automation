from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext

from EndPoints.platziEnpoints import EndPoints


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
                           base_url=EndPoints.platzi_base_url)
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def api_request_baseurl(api_request_context):
    request_context = api_request_context

# api_request_context.
