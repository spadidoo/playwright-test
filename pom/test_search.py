from playwright.sync_api import sync_playwright
from pageObj.SearchPage import SearchPage #folder and name of class in that folder

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")
    page.screenshot(path="screenshots/search.png")
    print(page.title())
    browser.close()

