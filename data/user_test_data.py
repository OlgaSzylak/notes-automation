import pytest


class InvalidEmails:
    MISSING_AT_SYMBOL = "userexample.com"
    MISSING_DOMAIN = "user@"
    MISSING_DOMAIN_EXTENSION = "user@example"
    EMPTY = ""


INVALID_EMAIL_CASES = [
    pytest.param(
        InvalidEmails.MISSING_AT_SYMBOL,
        id="missing-at-symbol",
    ),
    pytest.param(
        InvalidEmails.MISSING_DOMAIN,
        id="missing-domain",
    ),
    pytest.param(
        InvalidEmails.MISSING_DOMAIN_EXTENSION,
        id="missing-domain-extension",
    ),
]