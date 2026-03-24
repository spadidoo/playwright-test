# CODEGEN
# playwright codegen "url"
# playwright codegen --device="name of device" "url"
# playwright codegen --viewport-size=width,height "url"
# "" --color-scheme=dark/light (changes color scheme inside the url) "url"
# "" --timezone=zone (changes timezone inside the url) 
# "" --geolocation=lat,long (changes geolocation inside the url)
# "" --lang=language (changes language inside the url)

import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.pause()

    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()


# INSPECTOR
# page.pause() = to pause the test execution and open the inspector to see the state of the page at that moment

#DEBUGGING SELECTORS
# playwright.$("selector") = to find the first element matching the selector
# playwright.$$("selector") = to find all elements matching the selector
# playwright.inspect("selector") = goes to the element that matches the selector and highlights it in the browser, also shows the selector in the console