from enum import Enum


class Messages(str, Enum):
    REGISTRATION_SUCCESS = "User account created successfully"


class ErrorMessages(str, Enum):
    INVALID_EMAIL_MSG = "Email address is invalid"
    INVALID_PASSWORD_MSG = "Password should be between 6 and 30 characters"
    INVALID_PASSWORD_MATCH_MSG = "Passwords don't match!"
    INVALID_USERNAME_MSG = "User name should be between 4 and 30 characters"
    MISSING_USERNAME_MSG = "User name is required"
    MISSING_PASSWORD_MSG = "Password is required"
    MISSING_CONFIRM_PASSWORD_MSG = "Confirm Password is required"
    MISSING_EMAIL_MSG = "Email address is required"
    EMAIL_TAKEN_MSG = "An account already exists with the same email address"
