name = input("Enter student name: ")

m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\n--- STUDENT RESULT ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("Invalid marks entered!")

elif average >= 90:
    print("Grade: A")

elif average >= 80:
    print("Grade: B")

elif average >= 70:
    print("Grade: C")

elif average >= 60:
    print("Grade: D")

elif average >= 40:
    print("Grade: E")

else:
    print("Grade: F (Fail)")