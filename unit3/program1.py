contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])

    elif choice == "3":
        search = input("Enter name to search: ")

        found = False
        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                found = True

        if not found:
            print("Contact not found!")

    elif choice == "4":
        print("Exiting Contact Book")
        break

    else:
        print("Invalid choice!")