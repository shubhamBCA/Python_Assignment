# grading.py

from validators import get_name, get_int

students = []


def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    elif percent >= 35:
        return "E"
    else:
        return "F"


def add_student():
    print("\n===== GRADING SYSTEM =====")

    number_of_students = get_int(
        "How many students do you want to enter? ", min_val=1
    )

    subjects = get_int(
        "Enter number of subjects (default 5): ", min_val=1
    )

    for student_no in range(number_of_students):
        print("\nStudent", student_no + 1)

        name = get_name("Enter student name: ")

        while True:
            roll_no = input("Enter roll number: ").strip()

            if roll_no == "":
                print("Roll number cannot be empty.")
            elif any(s["roll_no"] == roll_no for s in students):
                print("Roll number already exists.")
            else:
                break

        while True:
            values = input(
                f"Enter {subjects} marks separated by spaces: "
            ).split()

            if len(values) != subjects:
                print("Please enter exactly", subjects, "marks.")
                continue

            valid = True

            for value in values:
                parts = value.split(".")

                if len(parts) > 2 or parts[0] == "":
                    valid = False
                    break

                if not parts[0].isdigit():
                    valid = False
                    break

                if len(parts) == 2:
                    if parts[1] == "" or not parts[1].isdigit():
                        valid = False
                        break

            if not valid:
                print("Enter valid numeric marks.")
                continue

            marks = list(map(float, values))

            if all(0 <= mark <= 100 for mark in marks):
                break
            else:
                print("Marks must be between 0 and 100.")

        total = sum(marks)
        average = total / subjects
        percentage = average

        grade = calculate_grade(percentage)

        if any(mark < 35 for mark in marks):
            result = "FAIL"
        else:
            result = "PASS"

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks,
            "total": total,
            "average": average,
            "percentage": percentage,
            "grade": grade,
            "result": result
        }

        students.append(student)

        generate_report_card(student)

    class_summary()


def generate_report_card(student):
    print("\n========== REPORT CARD ==========")
    print("Student:", student["name"])
    print("Roll Number:", student["roll_no"])

    print("-" * 35)
    print(f"{'Subject':<15}{'Marks':>10}")
    print("-" * 35)

    for i, mark in enumerate(student["marks"], start=1):
        print(f"{'Subject ' + str(i):<15}{mark:>10.2f}")

    print("-" * 35)
    print(f"Total       : {student['total']:.2f}")
    print(f"Average     : {student['average']:.2f}")
    print(f"Percentage  : {student['percentage']:.2f}%")
    print("Grade       :", student["grade"])
    print("Result      :", student["result"])
    print("=" * 35)


def view_students():
    print("\n===== ALL STUDENTS =====")

    if not students:
        print("No student records available.")
        return

    print(f"{'Name':<18}{'Roll No':<12}"
          f"{'Percentage':<14}{'Grade':<8}{'Result'}")
    print("-" * 65)

    for student in students:
        print(f"{student['name']:<18}"
              f"{student['roll_no']:<12}"
              f"{student['percentage']:<14.2f}"
              f"{student['grade']:<8}"
              f"{student['result']}")


def class_summary():
    print("\n===== CLASS SUMMARY =====")

    if not students:
        print("No student records available.")
        return

    total_percentage = 0
    topper = students[0]
    passed = 0
    failed = 0

    for student in students:
        total_percentage += student["percentage"]

        if student["percentage"] > topper["percentage"]:
            topper = student

        if student["result"] == "PASS":
            passed += 1
        else:
            failed += 1

    class_average = total_percentage / len(students)

    print("Total students:", len(students))
    print(f"Class average: {class_average:.2f}%")
    print("Topper:", topper["name"],
          f"({topper['percentage']:.2f}%)")
    print("Pass count:", passed)
    print("Fail count:", failed)