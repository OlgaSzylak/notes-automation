import re

import unicodedata
from playwright.sync_api import expect, Locator


class SoftAssert:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SoftAssert, cls).__new__(cls)
            cls._instance.errors = []
        return cls._instance

    def assert_visible(self, locator, message=""):
        try:
            expect(locator).to_be_visible()
        except AssertionError as e:
            error_message = f"{message} - {str(e)}" if message else str(e)
            self.errors.append(error_message)

    def assert_not_visible(self, locator, message=""):
        try:
            expect(locator).not_to_be_visible()
        except AssertionError as e:
            error_message = f"{message} - {str(e)}" if message else str(e)
            self.errors.append(error_message)

    def assert_to_be_equal(self, actual_value, expected_value, message=""):
        try:
            assert (actual_value == expected_value)
        except AssertionError as e:
            error_message = f"{message} - {str(e)}" if message else str(e)
            self.errors.append(error_message)

    def assert_enabled(self, locator, message=""):
        try:
            expect(locator).to_be_enabled()
        except AssertionError as e:
            error_message = f"{message} - {str(e)}" if message else str(e)
            self.errors.append(error_message)

    def assert_disabled(self, locator, message=""):
        try:
            expect(locator).to_be_disabled()
        except AssertionError as e:
            error_message = f"{message} - {str(e)}" if message else str(e)
            self.errors.append(error_message)

    def verify(self):
        if self.errors:
            all_errors = "\n".join(self.errors)
            self.errors.clear()
            raise AssertionError(f"Soft assert failed with the following errors:\n{all_errors}")

    @staticmethod
    def normalize_text(text: str) -> str:
        return unicodedata.normalize("NFKD", text) \
            .replace("’", "'") \
            .replace("“", '"') \
            .replace("”", '"') \
            .strip().lower()

    @staticmethod
    def expect_text_to_match(locator: Locator, pattern: str, case_insensitive: bool = True):
        actual = SoftAssert.normalize_text(locator.inner_text())
        expected = SoftAssert.normalize_text(pattern)
        if expected not in actual:
            raise AssertionError(f"Expected pattern:\n  {expected}\nnot found in actual text:\n  {actual}")

    @staticmethod
    def instance():
        return SoftAssert()
