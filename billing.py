# billing.py

from validators import get_name, get_float, get_int

invoices = []

TAX_RATE = 0.18


def calculate_discount(subtotal):
    if subtotal >= 10000:
        return 0.15
    elif subtotal >= 5000:
        return 0.10
    elif subtotal >= 1000:
        return 0.05
    else:
        return 0


def generate_invoice():
    print("\n===== GENERATE INVOICE =====")

    customer_name = get_name("Enter customer name: ")

    items = []

    while True:
        item_name = input(
            "Enter item name (type done to stop): "
        ).strip()

        if item_name.lower() == "done":
            break

        if item_name == "":
            print("Item name cannot be empty.")
            continue

        price = get_float("Enter unit price: ", min_val=0.01)
        quantity = get_int("Enter quantity: ", min_val=1)

        line_total = price * quantity

        items.append({
            "name": item_name,
            "unit_price": price,
            "quantity": quantity,
            "line_total": line_total
        })

        print("Item added successfully.")

    if not items:
        print("No items added. Invoice not generated.")
        return

    subtotal = 0

    for item in items:
        subtotal += item["line_total"]

    discount_rate = calculate_discount(subtotal)
    discount = subtotal * discount_rate

    taxable_amount = subtotal - discount
    tax = taxable_amount * TAX_RATE

    grand_total = taxable_amount + tax

    bill_no = "B-" + str(len(invoices) + 1).zfill(4)

    invoice = {
        "bill_no": bill_no,
        "customer_name": customer_name,
        "items": items,
        "subtotal": subtotal,
        "discount_rate": discount_rate,
        "discount": discount,
        "taxable_amount": taxable_amount,
        "tax": tax,
        "grand_total": grand_total
    }

    invoices.append(invoice)

    print("\n=============== INVOICE ===============")
    print("Bill No:", bill_no)
    print("Customer:", customer_name)

    print("-" * 55)
    print(f"{'Item':<15}{'Price':>10}{'Qty':>6}{'Total':>12}")
    print("-" * 55)

    for item in items:
        print(f"{item['name']:<15}"
              f"{item['unit_price']:>10.2f}"
              f"{item['quantity']:>6}"
              f"{item['line_total']:>12.2f}")

    print("-" * 55)
    print(f"{'Subtotal':<35}{subtotal:>12.2f}")
    print(f"{'Discount':<35}{discount:>12.2f}")
    print(f"{'Taxable Amount':<35}{taxable_amount:>12.2f}")
    print(f"{'Tax (18%)':<35}{tax:>12.2f}")
    print("-" * 55)
    print(f"{'GRAND TOTAL':<35}{grand_total:>12.2f}")
    print("=" * 55)
    print("Thank you for your purchase!")