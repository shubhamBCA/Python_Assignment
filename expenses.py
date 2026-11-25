# expenses.py

from validators import get_name, get_float, get_yes_no

expenses = []

CATEGORIES = ("Food", "Travel", "Utilities", "Stationery", "Other")


def add_expense():
    print("\n===== ADD EXPENSE =====")

    while True:
        description = get_name("Enter description: ")

        print("Categories:", ", ".join(CATEGORIES))

        while True:
            category = input("Enter category: ").strip().lower()

            matched_category = None

            for item in CATEGORIES:
                if item.lower() == category:
                    matched_category = item
                    break

            if matched_category is not None:
                category = matched_category
                break
            else:
                print("Choose a category from the given list.")

        amount = get_float("Enter amount: ", min_val=0.01)

        expenses.append({
            "description": description,
            "category": category,
            "amount": amount
        })

        print("Expense added successfully!")

        if not get_yes_no("Add another expense? (yes/no): "):
            break


def view_expenses():
    print("\n===== ALL EXPENSES =====")

    if not expenses:
        print("No expense records available.")
        return

    print(f"{'Description':<20}{'Category':<15}{'Amount':>12}")
    print("-" * 47)

    for expense in expenses:
        print(f"{expense['description']:<20}"
              f"{expense['category']:<15}"
              f"{expense['amount']:>12.2f}")


def expense_summary():
    print("\n===== EXPENSE SUMMARY =====")

    if not expenses:
        print("No expense records available.")
        return

    category_totals = {}

    total = 0
    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

        total += amount

        if amount > highest["amount"]:
            highest = expense

        if amount < lowest["amount"]:
            lowest = expense

    print(f"{'Category':<20}{'Total':>12}")
    print("-" * 32)

    for category, amount in category_totals.items():
        print(f"{category:<20}{amount:>12.2f}")

    print("-" * 32)
    print(f"{'Grand Total':<20}{total:>12.2f}")

    print("\nHighest single expense:",
          highest["description"], f"({highest['amount']:.2f})")

    print("Lowest single expense:",
          lowest["description"], f"({lowest['amount']:.2f})")