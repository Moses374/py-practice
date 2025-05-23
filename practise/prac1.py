import json

class Customer:
    def __init__(self, name, fav_product):
        self.name = name
        self.fav_product = fav_product

    def __str__(self):
        return f"{self.name} - {self.fav_product}"

def customer_info():
    name = input("Enter your name: ")
    fav_product = input("Enter your favorite product: ")
    return name, fav_product

def save_info(customer: Customer):
    try:
        with open("data2.json", "r") as file:
            content = file.read().strip()
            customers = json.loads(content) if content else []
    except FileNotFoundError:
        customers = []

    customers.append({"name": customer.name, "fav_product": customer.fav_product})

    with open("data2.json", "w") as file:
        json.dump(customers, file, indent=4)

    print(f"Customer info for {customer.name} saved successfully.")

def display_info():
    try:
        with open("data2.json", "r") as file:
            customers = json.load(file)

        print("\n--- Customer Records ---")
        for customer in customers:
            print(f"{customer['name']} - {customer['fav_product']}")
        print("-------------------\n")

    except FileNotFoundError:
        print("No customer data found. Please add some first!\n")

def menu():
    while True:
        print("\n===== Customer Info Menu =====")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name, fav_product = customer_info()
            customer = Customer(name, fav_product)
            save_info(customer)
        elif choice == '2':
            display_info()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    menu()
