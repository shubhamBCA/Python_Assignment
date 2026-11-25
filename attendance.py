# attendance.py

from validators import get_name, get_int, get_yes_no

attendance_records = {}


def attendance_percentage(present_days, total_days):
    return (present_days / total_days) * 100


def attendance_status(percent):
    if percent >= 75:
        return "Eligible"
    elif percent >= 60:
        return "Warning"
    else:
        return "Shortage"


def mark_attendance():
    print("\n===== MARK ATTENDANCE =====")

    total_days = get_int("Enter total working days: ", min_val=1)

    while True:
        name = get_name("Enter name: ")

        while True:
            roll_no = input("Enter roll number: ").strip()

            if roll_no == "":
                print("Roll number cannot be empty.")
            elif roll_no in attendance_records:
                print("Roll number already exists. Enter another.")
            else:
                break

        student_id = get_name("Enter ID: ")

        present_days = get_int(
            "Enter present days: ",
            min_val=0,
            max_val=total_days
        )

        percentage = attendance_percentage(present_days, total_days)
        status = attendance_status(percentage)

        attendance_records[roll_no] = {
            "name": name,
            "roll_no": roll_no,
            "id": student_id,
            "total_days": total_days,
            "present_days": present_days,
            "percentage": percentage,
            "status": status
        }

        print("Attendance saved successfully!")
        print(f"Attendance: {percentage:.2f}%")
        print("Status:", status)

        if not get_yes_no("Add another person? (yes/no): "):
            break


def attendance_summary():
    print("\n===== ATTENDANCE SUMMARY =====")

    if not attendance_records:
        print("No attendance records available.")
        return

    total_percentage = 0
    highest = None
    lowest = None

    eligible = 0
    warning = 0
    shortage = 0

    print(f"{'Name':<15}{'Roll No':<12}"
          f"{'Present':<10}{'Percentage':<14}{'Status'}")
    print("-" * 65)

    for roll_no, record in attendance_records.items():
        percent = record["percentage"]
        total_percentage += percent

        print(f"{record['name']:<15}"
              f"{roll_no:<12}"
              f"{record['present_days']:<10}"
              f"{percent:<14.2f}"
              f"{record['status']}")

        if highest is None:
            highest = record
            lowest = record
        else:
            if percent > highest["percentage"]:
                highest = record

            if percent < lowest["percentage"]:
                lowest = record

        if record["status"] == "Eligible":
            eligible += 1
        elif record["status"] == "Warning":
            warning += 1
        else:
            shortage += 1

    count = len(attendance_records)
    average = total_percentage / count

    print("\nTotal people:", count)
    print(f"Average attendance: {average:.2f}%")
    print(f"Highest: {highest['name']} "
          f"({highest['percentage']:.2f}%)")
    print(f"Lowest: {lowest['name']} "
          f"({lowest['percentage']:.2f}%)")

    print("Eligible:", eligible)
    print("Warning:", warning)
    print("Shortage:", shortage)


def highest_lowest_attendance():
    if not attendance_records:
        print("No attendance records available.")
        return

    highest = None
    lowest = None

    for record in attendance_records.values():
        if highest is None:
            highest = record
            lowest = record
        else:
            if record["percentage"] > highest["percentage"]:
                highest = record

            if record["percentage"] < lowest["percentage"]:
                lowest = record

    print("Highest attendance:",
          highest["name"], f"{highest['percentage']:.2f}%")

    print("Lowest attendance:",
          lowest["name"], f"{lowest['percentage']:.2f}%")