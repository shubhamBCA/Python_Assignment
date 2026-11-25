# reports.py


# 1. Expense Report
def print_expense_report(expenses):

    print("\n========== EXPENSE REPORT ==========")

    if not expenses:
        print("No expense records available.")
        return

    total = 0
    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        total += amount

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    print(f"{'Description':<18}{'Category':<15}{'Amount':>10}")
    print("-" * 43)

    for expense in expenses:

        print(
            f"{expense['description']:<18}"
            f"{expense['category']:<15}"
            f"{expense['amount']:>10.2f}"
        )

    print("-" * 43)
    print(f"Grand Total: {total:.2f}")

    print("\nCategory-wise Total:")

    for category, amount in category_totals.items():

        print(f"{category:<18}{amount:>10.2f}")


# 2. Attendance Report
def print_attendance_report(attendance):

    print("\n========== ATTENDANCE REPORT ==========")

    if not attendance:
        print("No attendance records available.")
        return

    total_percentage = 0

    highest = None
    lowest = None

    print(
        f"{'Name':<15}"
        f"{'Roll No':<12}"
        f"{'Percentage':<14}"
        f"{'Status'}"
    )

    print("-" * 55)

    for roll_no, record in attendance.items():

        percentage = record["percentage"]

        total_percentage += percentage

        if highest is None:
            highest = record
            lowest = record

        else:

            if percentage > highest["percentage"]:
                highest = record

            if percentage < lowest["percentage"]:
                lowest = record

        print(
            f"{record['name']:<15}"
            f"{roll_no:<12}"
            f"{percentage:<14.2f}"
            f"{record['status']}"
        )

    average = total_percentage / len(attendance)

    print("\nTotal people:", len(attendance))

    print(f"Average attendance: {average:.2f}%")

    print(
        "Highest attendance:",
        highest["name"],
        f"({highest['percentage']:.2f}%)"
    )

    print(
        "Lowest attendance:",
        lowest["name"],
        f"({lowest['percentage']:.2f}%)"
    )


# 3. Grading Report
def print_grading_report(students):

    print("\n========== GRADING REPORT ==========")

    if not students:
        print("No student records available.")
        return

    total_percentage = 0

    passed = 0
    failed = 0

    topper = students[0]

    print(
        f"{'Name':<18}"
        f"{'Roll No':<12}"
        f"{'Percentage':<14}"
        f"{'Grade':<8}"
        f"{'Result'}"
    )

    print("-" * 65)

    for student in students:

        percentage = student["percentage"]

        total_percentage += percentage

        if percentage > topper["percentage"]:
            topper = student

        if student["result"] == "PASS":
            passed += 1

        else:
            failed += 1

        print(
            f"{student['name']:<18}"
            f"{student['roll_no']:<12}"
            f"{percentage:<14.2f}"
            f"{student['grade']:<8}"
            f"{student['result']}"
        )

    average = total_percentage / len(students)

    print("\nTotal students:", len(students))

    print(f"Class average: {average:.2f}%")

    print(
        "Topper:",
        topper["name"],
        f"({topper['percentage']:.2f}%)"
    )

    print("Pass count:", passed)

    print("Fail count:", failed)


# 4. Billing Report
def print_invoice_report(invoices):

    print("\n========== BILLING REPORT ==========")

    if not invoices:
        print("No invoice records available.")
        return

    total_sales = 0

    for invoice in invoices:

        print("\nBill No:", invoice["bill_no"])

        print("Customer:", invoice["customer_name"])

        print("-" * 45)

        print(
            f"{'Item':<18}"
            f"{'Qty':>6}"
            f"{'Total':>12}"
        )

        print("-" * 45)

        for item in invoice["items"]:

            print(
                f"{item['name']:<18}"
                f"{item['quantity']:>6}"
                f"{item['line_total']:>12.2f}"
            )

        print("-" * 45)

        print(f"Subtotal: {invoice['subtotal']:.2f}")

        print(f"Discount: {invoice['discount']:.2f}")

        print(f"Tax: {invoice['tax']:.2f}")

        print(f"Grand Total: {invoice['grand_total']:.2f}")

        total_sales += invoice["grand_total"]

    print("\nTotal invoices:", len(invoices))

    print(f"Total sales: {total_sales:.2f}")


# 5. Main Reports Function
def reports(expenses, attendance, students, invoices):

    print("\n======================================")

    print("          ALL SYSTEM REPORTS")

    print("======================================")

    print_expense_report(expenses)

    print_attendance_report(attendance)

    print_grading_report(students)

    print_invoice_report(invoices)

    print("\n======================================")

    print("       ALL REPORTS COMPLETED")

    print("======================================")