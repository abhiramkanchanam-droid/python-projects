books = []

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")

        books.append({
            "name": name,
            "status": "Available"
        })

        print("Book added successfully!")

    elif choice == "2":
        print("\n--- BOOK LIST ---")

        for book in books:
            print("Book:", book["name"])
            print("Status:", book["status"])

    elif choice == "3":
        name = input("Enter book name to issue: ")
        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")

                break

        if not found:
            print("Book not found!")

    elif choice == "4":
        name = input("Enter book name to return: ")
        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")

                break

        if not found:
            print("Book not found!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")