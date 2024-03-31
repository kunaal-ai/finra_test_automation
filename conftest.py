"""Fixtures"""

import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.rules_guidance_page import RulesGuidancePage


@pytest.fixture
def home_page(page: Page):
    """Fixture - returns homepage object

    Args:
        page (Page): page context

    Returns:
        object: HomePage
    """
    return HomePage(page)


@pytest.fixture
def rule_guidance_page(page: Page):
    return RulesGuidancePage(page)


@pytest.fixture(scope="function", autouse=True)
def goto_home_page(page: Page):
    page.goto("https://www.finra.org/#/")
    yield
