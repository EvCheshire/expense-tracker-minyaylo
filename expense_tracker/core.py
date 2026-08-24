"""Core domain logic for the expense tracker."""

from dataclasses import dataclass, field


@dataclass
class Expense:
    amount: float
    category: str
    date: str
    note: str = ""


@dataclass
class ExpenseStore:
    expenses: list = field(default_factory=list)

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def list_expenses(self) -> list:
        return list(self.expenses)

    def total(self) -> float:
        return sum(e.amount for e in self.expenses)

    def total_by_category(self, category: str) -> float:
        return sum(e.amount for e in self.expenses)
