import re
from playwright.sync_api import Page, expect


def test_rules_guidance_page_loaded(page: Page, goto_home_page):
    expect(page).to_have_title(re.compile("FINRA.org"))


def test_rules_guidance_sidebar_links_verification(
    page: Page, home_page, goto_home_page, rule_guidance_page
):
    """page sidebar menu items clickable and url verification

    Args:
        page (Page): new page context
        home_page (object): new home page object
        goto_home_page (fixture): go to https://www.finra.org/#/
        rule_guidance_page (fixture - object): rule and guidance page object
    """    
    home_page.rules_guidance_tab.click()
    expect(page).to_have_url(re.compile("/rules-guidance"))

    rule_guidance_page.finra_manual_sidebarlink.click()
    expect(page).to_have_url(re.compile("/rulebooks"))

    rule_guidance_page.interpreting_rules_sidebarlink.click()
    expect(page).to_have_url(re.compile("/interpreting-rules"))

    rule_guidance_page.rulemaking_process_sidebarlink.click()
    expect(page).to_have_url(re.compile("/rulemaking-process"))

    rule_guidance_page.enforcement_sidebarlink.click()
    expect(page).to_have_url(re.compile("/enforcement"))

    rule_guidance_page.adjudication_sidebarlink.click()
    expect(page).to_have_url(re.compile("/adjudication-decisions"))
