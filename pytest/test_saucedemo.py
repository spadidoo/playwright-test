from playwright.sync_api import Page
import pytest

#@pytest.mark.skip_browser("chromium")
#@pytest.mark.only_browser("chromium")
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"
   

def test_inventory(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."
 
# pytest
# --headed (to see the test running in a browser)
# --base-url (if u want to avoid writing the full URL in the test)
# --browser (to specify the browser to run the test on)
# --browser-chanel (uses actual chrome app installed in ur system)
# --tracing on (to capture trace of the test execution for debugging purposes)
# --tracing retain-on-failure (to capture trace only when the test fails)
# playwright show-trace .\location-of-trace.zip (to view the trace in a visual format)
# --slowmo (to slow down the test execution for better observation)
