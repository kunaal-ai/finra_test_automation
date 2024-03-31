import os
from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page

        self.rules_guidance_tab = (
            page.get_by_role("banner", name="Site header")
            .get_by_role("link", name="Rules & Guidance")
        )
        self.registeration_tab = (
            page.get_by_role("banner", name="Site header")
            .get_by_role("link", name="Registration, Exams & CE")
        )
        self.events_training_tab = (
            page.get_by_role("banner", name="Site header")
            .get_by_role("link", name="Events & Training")
        )
        self.filing_reporting_tab = (
            page.get_by_role("banner", name="Site header")
            .get_by_role("link", name="Filing & Reporting")
        )
        self.compliance_tools_tab = (
            page.get_by_role("banner", name="Site header")
            .get_by_role("link", name="Compliance Tools")
        )
        self.for_investors_tab = (
            page.get_by_role("banner", name="Site header")
            .get_by_role("link", name="For Investors")
        )        