from expense_tracker.core import Expense, ExpenseStore


def test_total_sums_all_expenses():
    store = ExpenseStore()
    store.add_expense(Expense(amount=100.0, category="food", date="2026-08-01"))
    store.add_expense(Expense(amount=50.5, category="transport", date="2026-08-02"))

    assert store.total() == 150.5
