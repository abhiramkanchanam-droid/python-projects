import csv

# Create CSV file and store employee details
with open("payroll.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Basic Salary", "HRA", "DA", "Total Salary"])

    while True:
        name = input("Enter employee name: ")

        basic = float(input("Enter basic salary: "))
        hra = basic * 0.20
        da = basic * 0.10

        total = basic + hra + da

        writer.writerow([name, basic, hra, da, total])

        print("Salary calculated:", total)

        choice = input("Add another employee? (yes/no): ")

        if choice.lower() != "yes":
            break

# Display payroll details
print("\n--- PAYROLL DETAILS ---")

with open("payroll.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)