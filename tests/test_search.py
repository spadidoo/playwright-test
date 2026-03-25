# Example 1
# DuckDuckGo

from playwright.sync_api import sync_playwright, Page, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    def test_basic_duckduckgo_search(page: Page) -> None:
        # Given the DuckDuckGo home page is displayed
        # Can add a wait command: 'wait_until="networkidle"' to ensure the page is fully loaded before proceeding
        page.goto("https://duckduckgo.com/")

        # When the user searches for a phrase
        page.locator("#searchbox_input").fill('panda')
        page.locator("[type='submit']").click()

        # Then the search result query is the phrase
        page.wait_for_timeout(9000)
        expect(page.locator("#search_form_input")).to_have_value('panda')
        
        # And the search result links pertain to the phrase
        #                selector for result links 
        page.locator('a[data-testid="result-title-a"]').nth(4).wait_for()
        # wait_for: method that waits for the element to be visible
        # this code waits for the 5th search result link to be visible before proceeding with the next assertion

        # Get the text contents of all matching elements
        titles = page.locator('a[data-testid="result-title-a"]').all_text_contents()
        matches = [t for t in titles if 'panda' in t.lower()]

        # Assert that there is at least one match in the search results
        assert len(matches) > 0
       
        # And the search result title contains the phrase
        expect(page).to_have_title('panda at DuckDuckGo')
