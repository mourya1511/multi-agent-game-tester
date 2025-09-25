from playwright.sync_api import sync_playwright
import os

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

def execute_test_case_sync(test_case, test_id):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            for step in test_case.get("steps", []):
                if "Go to URL" in step:
                    page.goto("https://play.ezygamers.com/")
            screenshot_path = os.path.join(REPORTS_DIR, f"test_{test_id}.png")
            page.screenshot(path=screenshot_path, full_page=True)
            browser.close()
            return {"test_id": test_id, "verdict": "Pass", "artifacts": [screenshot_path]}
    except Exception as e:
        return {"test_id": test_id, "verdict": "Failed", "error": str(e), "artifacts": []}
