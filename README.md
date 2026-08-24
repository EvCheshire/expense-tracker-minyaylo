# expense-tracker-minyaylo

Невеликий CLI-застосунок для обліку витрат. Навчальний проєкт для
лабораторної роботи №3 (Git internals, гілкування, code review).

## Модулі

- `expense_tracker/core.py` — доменна логіка (Expense, ExpenseStore)
- `expense_tracker/validation.py` — валідація вхідних даних
- `expense_tracker/cli.py` — обробка введення користувача (CLI)
- `tests/test_core.py` — unit-тести

## Запуск

```bash
python -m expense_tracker.cli add --amount 120.50 --category food --date 2026-08-24 --note "lunch"
python -m expense_tracker.cli list
python -m expense_tracker.cli total --category food
```

## Приклад виводу

```
$ python -m expense_tracker.cli total --category food
Total for food: 100.00
```

## Тести

```bash
pip install -r requirements-dev.txt
pytest
```
