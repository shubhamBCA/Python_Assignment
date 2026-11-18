# Integrated Expense, Attendance, Grading and Billing Manager

Console, menu-driven Python program (Python 3.8+, standard library only).

## How to run
    python main.py

## Features
1. Expense Management - add expenses by category, view table, category totals, highest/lowest
2. Attendance Management - percentage, status (Eligible >=75, Warning 60-74.99, Shortage <60), summary
3. Grading System - total/average/percentage, grade scale, subject-level fail rule (<35), class summary
4. Billing System - multi-item invoice, slab discount, 18% tax after discount, 2-decimal totals
5. Reports - per-module report with optional export to a .txt file

## Configurable constants (top of main.py)
TAX_RATE, PASS_MARK, ATTENDANCE_THRESHOLD, WARNING_LIMIT, CATEGORIES, DISCOUNT_SLABS, GRADE_SCALE

## Notes
- All input is validated and re-prompted; Ctrl+C exits gracefully.
- Data is kept in memory only (lost on exit unless a report is exported).
