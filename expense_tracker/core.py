"""Core domain logic for the expense tracker.

Refactored to keep ``ExpenseStore`` self-validating and to make the
public API explicit (docstrings + type hints) rather than relying on
callers to do the right thing.
"""

from dataclasses import dataclass, field
from typing import List

from expense_tracker.validation import validate_expense


@dataclass
class Expense:
    """A single expense entry."""

    amount: float
    category: str
    date: str
    note: str = ""


@dataclass
class ExpenseStore:
    """In-memory collection of :class:`Expense` records."""

    expenses: List[Expense] = field(default_factory=list)

    def add_expense(self, expense: Expense) -> None:
        """Validate and store a new expense, rounding the amount to cents."""
        validate_expense(expense.amount, expense.category, expense.date)
        expense.amount = round(expense.amount, 2)
        self.expenses.append(expense)

    def list_expenses(self) -> List[Expense]:
        """Return a copy of all recorded expenses."""
        return list(self.expenses)

    def total(self) -> float:
        """Return the sum of all recorded expenses."""
        return sum(e.amount for e in self.expenses)

    def total_by_category(self, category: str) -> float:
        """Return the sum of expenses for a single category."""
        return sum(e.amount for e in self.expenses if e.category == category)
