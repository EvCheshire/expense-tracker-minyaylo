"""Command-line interface for the expense tracker."""

import argparse
import json
import os

from expense_tracker.core import Expense, ExpenseStore
from expense_tracker.logging_config import setup_logging

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data.json")


def load_store() -> ExpenseStore:
    store = ExpenseStore()
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for row in json.load(f):
                store.add_expense(Expense(**row))
    return store


def save_store(store: ExpenseStore) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([e.__dict__ for e in store.list_expenses()], f, indent=2)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="expense-tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="add a new expense")
    add_p.add_argument("--amount", type=float, required=True)
    add_p.add_argument("--category", type=str, required=True)
    add_p.add_argument("--date", type=str, required=True)
    add_p.add_argument("--note", type=str, default="")

    sub.add_parser("list", help="list all expenses")

    total_p = sub.add_parser("total", help="show total expenses")
    total_p.add_argument("--category", type=str, default=None)

    return parser


def main(argv=None) -> None:
    setup_logging()
    parser = build_parser()
    args = parser.parse_args(argv)
    store = load_store()

    if args.command == "add":
        store.add_expense(
            Expense(amount=args.amount, category=args.category, date=args.date, note=args.note)
        )
        save_store(store)
        print("Expense added.")
    elif args.command == "list":
        for e in store.list_expenses():
            print(f"{e.date} | {e.category:12} | {e.amount:>10.2f} | {e.note}")
    elif args.command == "total":
        if args.category:
            print(f"Total for {args.category}: {store.total_by_category(args.category):.2f}")
        else:
            print(f"Total: {store.total():.2f}")


if __name__ == "__main__":
    main()
