import csv
csv_file = "employee_payroll.csv"
with open(csv_file, "w", newline="") as f:
  csv_writer = csv.writer(f)
  csv_writer.writerow(["Name", "Basic Salary", "Bonus", "Total"])
  num_employees = int(input("Enter number of employees: "))
  for _ in range(num_employees):
    emp_name = input("Enter employee name: ")
    basic_pay = float(input("Enter basic salary: "))
    emp_bonus = float(input("Enter bonus: "))
    total_pay = basic_pay + emp_bonus
    csv_writer.writerow([emp_name, basic_pay, emp_bonus, total_pay])
with open(csv_file, "r", newline="") as f:
  csv_reader = csv.reader(f)
  print("\nPayroll Details:")
  for record in csv_reader:
    print(record)