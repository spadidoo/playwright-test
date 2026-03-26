from playwright.sync_api import Page

class DuckDuckGoSearchPage:
    URL = 'https://duckduckgo.com' # Warning: Base URLs should typically be passed into automation code as an input, not hard-coded in a page object. We are doing this here as a matter of simplicity for this tutorial.
     
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_button = page.locator("[type='submit']")
        self.search_input = page.locator("#searchbox_input")

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()

    