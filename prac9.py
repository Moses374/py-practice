import json
from importlib.resources import contents

contacts={}
def add_contact():
    contact_name=input("Enter contact name: ").strip()
    try:
        contact_no=int(input("Enter contact number: ").strip())
    except ValueError:
        print("Enter valid contact number: ")
        return
    if contact_name:
        contacts[contact_name]=contact_no
        print("Contact info saved.")
    else:
        print("Contact name not entered.")
    save_contacts_to_file()

def save_contacts_to_file():
    try:
        with open("contacts.json","w")as file:
            json.dump(contacts,file,indent=4)
        print("Contacts saved to file")
    except Exception as e:
        print(f"An error occured while saving contacts: {e}")

def view_contacts():
    try:
        with open("contacts.json","r")as file:
            loaded_contacts=json.load(file)
        if not loaded_contacts:
            print("No contacts found.")
            return

        print("---Customer Contacts---")

        for name,number in loaded_contacts.items():
            print(f"{name}:{number}")
    except FileNotFoundError:
        print("File is not available")
    except json.JSONDecodeError:
        print("Contact file is corrupted or empty.")

def clear_contacts():

        with open("contacts.json","w")as file:
            json.dump({},file,indent=4)
        print("All contacts have been cleared")

def remove_contact():
     try:
         with open("contacts.json","r")as file:
            loaded_contacts=json.load(file)
         if not loaded_contacts:
            print("No contacts have been entered.")

         contact_to_be_deleted=input("Enter contact name to be deleted: ").strip()

         if contact_to_be_deleted in loaded_contacts:
             del loaded_contacts[contact_to_be_deleted]
             with open("contacts.json","w")as file:
                 json.dump(loaded_contacts,file,indent=4)
             print(f"{contact_to_be_deleted} deleted successfully.")
         else:
             print("Contact not found")
     except FileNotFoundError:
         print("File not found")
     except json.JSONDecodeError:
         print("The contact file is empty or corrupted.")

def menu():
    while True:
        print("\n--- Contact Manager Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Clear All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            clear_contacts()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")

def load_contacts_from_file():
    global contacts
    try:
        with open("contacts.json","r")as file:
            contacts=json.load(file)
    except(FileNotFoundError,json.JSONDecodeError):
        contacts={}

if __name__=="__main__":
    load_contacts_from_file()

    menu()

