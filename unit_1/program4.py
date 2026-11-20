"""Generate an electricity bill using meter readings."""

DUTY_RATE = 0.05
METER_CHARGE = 100.0

def main():
    print("\n======= ELECTRICITY BILL GENERATOR =======")

    name = input("Enter Customer Name: ")
    customer_id = input("Enter Customer ID: ")

    old_reading = float(input("Enter Previous Meter Reading: "))
    new_reading = float(input("Enter Current Meter Reading: "))
    rate = float(input("Enter Cost Per Unit (INR): "))

    if new_reading < old_reading:
        print("Error: Invalid meter reading!")
        return

    if rate < 0:
        print("Error: Cost cannot be negative!")
        return

    units = new_reading - old_reading

    energy_cost = units * rate
    duty = energy_cost * DUTY_RATE

    total_bill = energy_cost + duty + METER_CHARGE

    print("\n========== ELECTRICITY BILL ==========")
    print("Customer Name       :", name)
    print("Customer ID         :", customer_id)
    print("Units Consumed      :", units, "kWh")
    print("Energy Charges      : INR", round(energy_cost, 2))
    print("Electricity Duty    : INR", round(duty, 2))
    print("Meter Charges       : INR", METER_CHARGE)
    print("--------------------------------------")
    print("Total Bill Amount   : INR", round(total_bill, 2))
    print("======================================")

if __name__ == "__main__":
    main()
