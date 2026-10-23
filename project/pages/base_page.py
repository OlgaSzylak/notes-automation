from abc import ABC
from typing import Literal, Optional
import allure
from playwright.sync_api import Page, expect


class BasePage(ABC):
    TIMEOUT = 15000
    WAIT_UNTIL: Literal["load", "domcontentloaded", "networkidle", "commit"] = "load"
    TIMEOUT_CONST = 90000

    def __init__(self, page: Page):
        self.page = page
        self.context = page.context

    def navigate_to_url(self, url: str):
        with allure.step(f"Navigate to {url}"):
            self.page.goto(url)

    def verify_page_title(self, title):
        with allure.step(f"Verify page has title: {title}"):
            expect(self.page).to_have_title(title)

    def verify_page_opened(self, locator):
        self.page.wait_for_selector(locator)
        expect(self.page.locator(locator)).to_be_visible()

    def wait_for_visible_state(self, locator):
        self.page.wait_for_selector(locator, state="visible")

    def open_new_tab_and_get_page(self, action: callable) -> Page:
        with allure.step("Open new tab and get page"):
            with self.context.expect_page() as page_info:
                action()
            new_page = page_info.value
            new_page.wait_for_load_state("domcontentloaded", timeout=self.TIMEOUT)
            return new_page

    def press_key(self, key: str, locator: Optional[str] = None):
        with allure.step(f"Press '{key}' key"):
            if locator:
                element = self.page.locator(locator)
                expect(element).to_be_visible(timeout=self.TIMEOUT_CONST)
                element.press(key)
            else:
                self.page.keyboard.press(key)

    def verify_element_text(self, locator: str, expected_text: str):
        with allure.step(f"Verify '{locator}' contains text '{expected_text}'"):
            expect(self.page.locator(locator)).to_have_text(expected_text)