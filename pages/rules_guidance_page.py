import os
from playwright.sync_api import Page


class RulesGuidancePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.finra_manual_sidebarlink = page.locator(
            "#block-finra-bootstrap-sass-system-main"
        ).get_by_role("link", name="FINRA Manual")

        self.interpreting_rules_sidebarlink = page.locator("#sidebar_first").get_by_role(
            "link", name="Interpreting the Rules"
        )

        self.rulemaking_process_sidebarlink = page.locator("#sidebar_first").get_by_role(
            "link", name="The Rulemaking Process"
        )

        self.enforcement_sidebarlink = page.locator("#sidebar_first").get_by_role("link", name="Enforcement")
        
        self.adjudication_sidebarlink = page.locator("#block-finra-bootstrap-sass-system-main").get_by_role(
            "link", name="Adjudication & Decisions"
        )
