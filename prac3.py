from datetime import datetime
def log_message(msg):
    time=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    with open("log.txt","a")as log_file:
        log_file.write(f"[{time}] {msg}\n")

def add_message():
    msg=str(input("Enter message:"))
    log_message(msg)
    print("Message loaded successfully")

def read_log():
    try:
        with open("log.txt","r")as file:
            content=file.readlines()
            if content:
                print("\n--- Log Contents ---")
                for line in content:
                    print(line.strip())
                print("---------------------\n")
            else:
                print("Log is empty.\n")
    except FileNotFoundError:
        print("Log file not found.\n")

def clear_log():
    with open("log.txt","w")as file:
        pass
    print("Log has been cleared.\n")
def menu():
    while True:
        print("=== Log Menu ===")
        print("1. Add Message")
        print("2. View Log")
        print("3. Clear Log")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_message()
        elif choice == '2':
            read_log()
        elif choice == '3':
            clear_log()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()