# Contact Management System

contacts = {}

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\n===== CONTACT LIST =====")
            for name, details in contacts.items():
                print("Name  :", name)
                print("Phone :", details["phone"])
                print("------------------------")

    # Search Contact
    elif choice == "3":
        search = input("Enter name or phone number to search: ").lower()
        found = False

        for name, details in contacts.items():
            if search in name.lower() or search in details["phone"]:
                print("\nContact Found!")
                print("Name   :", name)
                print("Phone  :", details["phone"])
                print("Email  :", details["email"])
                print("Address:", details["address"])
                found = True

        if not found:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            contacts[name]["phone"] = input("Enter new phone number: ")
            contacts[name]["email"] = input("Enter new email: ")
            contacts[name]["address"] = input("Enter new address: ")

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using Contact Management System!")
        break

    else:
        print("Invalid choice! Please try again.")