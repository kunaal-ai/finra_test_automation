""" Test for Home Page only
"""
import re
from playwright.sync_api import Page, expect


def test_home_page_loaded(page: Page, goto_home_page):
    """confirmation if home page loaded sucessfully before running following test cases

    Args:
        page (Page):page context
        goto_home_page (fixture): go to https://www.finra.org/#/
    """    
    expect(page).to_have_title(re.compile("FINRA.org"))

def test_site_header_main_menu_items_clickable(
    page: Page,
    home_page, goto_home_page
):
    """Verify - if main header items are clickable - no page confirmation 

    Args:
        page (Page): page context
        home_page (fixture): Home page new context object
        goto_home_page (fixture): go to https://www.finra.org/#/
    """    
    home_page.rules_guidance_tab.click()
    home_page.registeration_tab.click()
    home_page.events_training_tab.click()
    home_page.filing_reporting_tab.click()
    home_page.compliance_tools_tab.click()
    page.wait_for_load_state("networkidle") # Wait until page loads
    home_page.for_investors_tab.click()
