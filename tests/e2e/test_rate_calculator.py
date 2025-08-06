from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

def test_001_Rate_Calculator(page, Malaysia, India):
    page.goto(os.getenv("RATE_CALCULATOR_URL"))
    page.wait_for_load_state("networkidle")

    # Select Malaysia
    page.select_option("select[name='from']", value=Malaysia)
    page.select_option("select[name='to']", value=India)

    # Enter amount
    page.fill("input[name='amount']", "1000")

    # Click calculate button
    page.click("button[type='submit']")

    # Wait for results to appear
    page.wait_for_selector(".result")

    # Verify the result
    result = page.inner_text(".result")
    assert "Exchange Rate" in result, "Exchange rate not displayed correctly"