# validators.py

def get_int(prompt, min_val=None, max_val=None):
    while True:
        value = input(prompt).strip()

        if value.isdigit():
            number = int(value)

            if min_val is not None and number < min_val:
                print("Value is too small. Try again.")
            elif max_val is not None and number > max_val:
                print("Value is too large. Try again.")
            else:
                return number
        else:
            print("Please enter a valid whole number.")


def get_float(prompt, min_val=None, max_val=None, decimal_places=2):
    while True:
        value = input(prompt).strip()

        # Allow one optional decimal point
        parts = value.split(".")

        valid = True

        if len(parts) > 2 or len(parts) == 0:
            valid = False
        elif parts[0] == "" or not parts[0].isdigit():
            valid = False
        elif len(parts) == 2:
            if parts[1] == "" or not parts[1].isdigit():
                valid = False
            elif len(parts[1]) > decimal_places:
                valid = False

        if valid:
            number = float(value)

            if min_val is not None and number < min_val:
                print("Value must be at least", min_val)
            elif max_val is not None and number > max_val:
                print("Value must not exceed", max_val)
            else:
                return number
        else:
            print("Enter a valid number with up to",
                  decimal_places, "decimal places.")


def get_name(prompt):
    while True:
        name = input(prompt).strip()

        if name != "" and any(ch.isalpha() for ch in name):
            return name

        print("Name cannot be empty.")


def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Please enter yes or no.")