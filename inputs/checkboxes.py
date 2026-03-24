import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        #context: isolated incognito-alike seesion within browser instance
        context = await browser.new_context()
        #new context can start tracing; kind of like a log file that captures a screenshot of all the steps and actions performed during the test execution, which can be used for debugging and analysis purposes
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()

        await page.set_viewport_size({"width": 1800, "height":1200})
        await page.goto("https://demoqa.com/checkbox")

        #actions
        await page.check('span.rc-tree-checkbox')
        await page.screenshot(path="screenshots/checkboxes.png")

        #assertions
        await page.is_checked('span.rc-tree-checkbox') is True
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopdocumentsdownloadsnotescommandsworkspaceofficewordFileexcelFilereactangularveupublicprivateclassifiedgeneral")

        #stop tracing
        await context.tracing.stop(path = "logs/trace.zip")

        #closing browser
        await browser.close()

asyncio.run(main())