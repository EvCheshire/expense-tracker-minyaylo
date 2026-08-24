"""Input validation for the expense tracker."""

import re

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ValidationError(ValueError):
    """Raised when expense input data is invalid."""


def validate_amount(amount: float) -> None:
    if amount <= 0:
        raise ValidationError("amount must be a positive number")


def validate_category(category: str) -> None:
    if not category or not category.strip():
        raise ValidationError("category must not be empty")


def validate_date(date: str) -> None:
    if not DATE_RE.match(date):
        raise ValidationError("date must be in YYYY-MM-DD format")


def validate_expense(amount: float, category: str, date: str) -> None:
    validate_amount(amount)
    validate_category(category)
    validate_date(date)
