import csv
import matplotlib.pyplot as plt
# Create sales data
sales = [
    ["Product", "Quantity", "Price"],
    ["Laptop", 5, 50000],
    ["Mobile", 10, 15000],
    ["Headphones", 20, 1000],
    ["Keyboard", 15, 800],
    ["Mouse", 25, 500]
]
# Store data in CSV file
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales)
# Read CSV file
products = []
total_sales = []
with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = float(row[2])

        amount = quantity * price

        products.append(product)
        total_sales.append(amount)

# Calculate total revenue
revenue = sum(total_sales)

print("--- RETAIL SALES REPORT ---")

for i in range(len(products)):
    print(products[i], "Sales:", total_sales[i])

print("Total Revenue: Rs.", revenue)

# Create bar chart
plt.bar(products, total_sales)

plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount (Rs.)")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Create pie chart
plt.pie(total_sales, labels=products, autopct="%1.1f%%")

plt.title("Product Sales Percentage")
plt.show()