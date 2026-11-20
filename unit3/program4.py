students = []

number_of_students = int(input("Enter the number of students: "))

for i in range(number_of_students):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")
    attendance = input("Enter attendance (P for Present, A for Absent): ").strip().upper()

    while attendance not in ("P", "A"):
        print("Please enter P or A.")
        attendance = input("Enter attendance (P for Present, A for Absent): ").strip().upper()

    status = "Present" if attendance == "P" else "Absent"
    students.append((name, status))

print("\n--- ATTENDANCE REPORT ---")
for name, status in students:
    print(name, "-", status)
