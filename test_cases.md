# Test Log (D3) - 12 normal + 8 edge cases

Run on 13-11-2026 with `python main.py` logic (automated run + manual re-check recommended).

## Normal test cases

| TC | Module | Input used | Expected | Actual | Pass/Fail |
|----|--------|-----------|----------|--------|-----------|
| N-01 | Menu | main menu: choose 1 then Back, then 6 | Opens Expense module; exits with goodbye | Output showed 'EXPENSE MANAGEMENT', 'Goodbye' | Pass |
| N-02 | Expense | Lunch / Food / 250.50 | Expense added successfully | Output showed 'Expense added successfully!' | Pass |
| N-03 | Expense | Food 250.50, Travel 120, Utilities 890.75, then summary | Grand total 1261.25; highest Utilities 890.75 | Output showed '1261.25', 'Utilities - 890.75' | Pass |
| N-04 | Attendance | Total 40, Asha present 38 | 95.00% -> Eligible | Output showed '95.00', 'Eligible' | Pass |
| N-05 | Attendance | Total 40, Ravi present 27 | 67.50% -> Warning | Output showed '67.50', 'Warning' | Pass |
| N-06 | Attendance | Total 40, Meena present 20 | 50.00% -> Shortage | Output showed '50.00', 'Shortage' | Pass |
| N-07 | Attendance | Asha 38, Ravi 27, Meena 20 of 40, then summary | Avg 70.83%, highest Asha, lowest Meena, 1/1/1 status counts | Output showed '70.83%', 'Asha (95.00%)', 'Meena (50.00%)', 'Eligible: 1 / Warning: 1 / Shortage: 1' | Pass |
| N-08 | Grading | Marks 92,88,79,85,95 | 439/500, avg 87.80, grade A, PASS | Output showed '439.00 / 500', '87.80', 'Grade      : A', 'PASS' | Pass |
| N-09 | Grading | Marks 65,60,70,62,68 | 325/500, 65.00%, grade C, PASS | Output showed '325.00 / 500', '65.00%', 'Grade      : C', 'PASS' | Pass |
| N-10 | Billing | 1 item, 500 x 1 | No discount, tax 90.00, total 590.00 | Output showed 'Discount (0%)', '90.00', '590.00' | Pass |
| N-11 | Billing | 1000 x 2 (subtotal 2000) | 5% discount 100.00, tax 342.00, total 2242.00 | Output showed 'Discount (5%)', '100.00', '1900.00', '342.00', '2242.00' | Pass |
| N-12 | Reports | Add expense via main menu, open Expense report, skip export | Report shows grand total; returns to menu and exits | Output showed 'GRAND TOTAL', '250.50', 'Goodbye' | Pass |

## Edge test cases

| TC | Module | Input used | Expected | Actual | Pass/Fail |
|----|--------|-----------|----------|--------|-----------|
| E-01 | Menu | Empty input and spaces only at menu | Error message each time, re-prompt, no crash | Output showed 'Invalid choice' x2, 'Goodbye' | Pass |
| E-02 | Expense | Amount: inf, nan, 0.001, -0, then 10 | All rejected; only 10.00 accepted | Output showed 'Invalid amount' x4, 'Expense added successfully!', '10.00' | Pass |
| E-03 | Attendance | Total days: 4.5, 0, -3, then 40 | First three rejected; 40 accepted | Output showed 'Enter a whole number of at least 1.' x3 | Pass |
| E-04 | Attendance | Present = total (40/40) and present = 0 (0/40) | 100.00% Eligible and 0.00% Shortage | Output showed '100.00', '0.00', 'Eligible', 'Shortage' | Pass |
| E-05 | Grading | All marks exactly 35, then one subject 34.99 | 35% -> E, PASS; 34.99 in one subject -> FAIL | Output showed 'Grade      : E', 'PASS', 'FAIL' | Pass |
| E-06 | Billing | Subtotal 999.99 (just below slab) | 0% discount; tax 180.00; total 1179.99 | Output showed 'Discount (0%)', '180.00', '1179.99' | Pass |
| E-07 | Billing | Customer name: R2, A, 41 letters, then Ro | Three rejected; 'Ro' accepted | Output showed 'Name must contain 2-40 letters.' x3, 'Customer: Ro' | Pass |
| E-08 | Reports | Open all 4 reports with no data | 'No records available.' for each report | Output showed 'No records available.' x4 | Pass |

