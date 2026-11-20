while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        file = open("students.txt", "a")

        file.write(name + "," + roll + "," + marks + "\n")

        file.close()

        print("Student details saved successfully!")

    elif choice == "2":
        file = open("students.txt", "r")

        print("\n--- STUDENT DETAILS ---")

        for line in file:
            print(line, end="")

        file.close()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")