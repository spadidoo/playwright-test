import pytest
from playwright.sync_api import sync_playwright, Page, expect
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage
# doesnt work when inside 'test' folder, but works outside of it

ANIMALS = [
    'panda',
    'koala',
    'sloth',
    'bear'
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    
    # Use pytest.mark.parametrize to run the test with different search phrases
    @pytest.mark.parametrize('phrase', ANIMALS)
    def test_basic_duckduckgo_search(page: Page,
        phrase: str,
        search_page: DuckDuckGoSearchPage,
        result_page: DuckDuckGoResultPage) -> None:
        #fixtures 


        # Given the DuckDuckGo home page is displayed
        search_page.load()

        #when the user searches for a phrase
        search_page.search(phrase)

        # Then the search result query is the phrase
        expect(result_page.search_input).to_have_value(phrase)
        
        # And the search result links pertain to the phrase
        assert result_page.results_link_titles_contain_phrase(phrase)

        # And the search result title contains the phrase
        expect(page).to_have_title(f'{phrase} at DuckDuckGo')


# --verbose : shows each test result with the browser and if passed or failed
# --device : emulate a specific device, such as 'iPhone 12' or 'Pixel 5'
# --output : specify a directory to save test results, such as screenshots and videos
# --report : generate a test report in a specific format, such as HTML or JSON
# --screenshot on : capture a screenshot after each test, or only on failure
# --video on : record a video of the test execution, or only on failure
# --video retain-on-failure : keep the video only if the test fails, otherwise discard it
# --trace on : capture a trace of the test execution, which includes network requests, console logs, and screenshots
# --trace retain-on-failure : keep the trace only if the test fails, otherwise discard
# -n : run tests in parallel using multiple workers, which can speed up test execution

