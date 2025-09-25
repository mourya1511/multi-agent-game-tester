# test_playwright.py
import asyncio
from playwright.async_api import async_playwright

# Windows-specific event loop
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://play.ezygamers.com/", wait_until="domcontentloaded")
        await page.screenshot(path="test.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
