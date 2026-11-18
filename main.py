# main.py

from expenses import add_expense, view_expenses, expense_summary, expenses
from attendance import mark_attendance, attendance_summary, attendance_records, highest_lowest_attendance
from grading import add_student, view_students, class_summary, students
from billing import generate_invoice, invoices
from reports import reports
from validators import get_int


def expense_menu():
    while True:
        print("\n===== EXPENSE MANAGEMENT =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Expense Summary")
        print("4. Back to Main Menu")

        choice = get_int("Enter your choice: ", 1, 4)

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            expense_summary()
        elif choice == 4:
            break


def attendance_menu():
    while True:
        print("\n===== ATTENDANCE MANAGEMENT =====")
        print("1. Mark Attendance")
        print("2. Attendance Summary")
        print("3. Highest and Lowest Attendance")
        print("4. Back to Main Menu")

        choice = get_int("Enter your choice: ", 1, 4)

        if choice == 1:
            mark_attendance()
        elif choice == 2:
            attendance_summary()
        elif choice == 3:
            highest_lowest_attendance()
        elif choice == 4:
            break


def grading_menu():
    while True:
        print("\n===== GRADING SYSTEM =====")
        print("1. Add Students and Marks")
        print("2. View All Students")
        print("3. Class Summary")
        print("4. Back to Main Menu")

        choice = get_int("Enter your choice: ", 1, 4)

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            class_summary()
        elif choice == 4:
            break


def billing_menu():
    while True:
        print("\n===== BILLING SYSTEM =====")
        print("1. Generate Invoice")
        print("2. Back to Main Menu")

        choice = get_int("Enter your choice: ", 1, 2)

        if choice == 1:
            generate_invoice()
        elif choice == 2:
            break


def main():
    while True:
        print("\n======================================")
        print(" EXPENSE, ATTENDANCE, GRADING & BILLING")
        print("======================================")
        print("1. Expense Management")
        print("2. Attendance Management")
        print("3. Grading System")
        print("4. Billing System")
        print("5. View All Reports")
        print("6. Exit")
        print("--------------------------------------")

        choice = get_int("Enter your choice (1-6): ", 1, 6)

        if choice == 1:
            expense_menu()

        elif choice == 2:
            attendance_menu()

        elif choice == 3:
            grading_menu()

        elif choice == 4:
            billing_menu()

        elif choice == 5:
            reports(
                expenses,
                attendance_records,
                students,
                invoices
            )

        elif choice == 6:
            print("\nThank you for using the system. Goodbye!")
            break


if __name__ == "__main__":
    main()