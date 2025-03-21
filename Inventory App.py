# Inventory App
inventory = {}

def add_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    print(f"Added {quantity} of {name} to inventory.")

def remove_item(name, quantity):
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
            print(f"Removed {quantity} of {name} from inventory.")
        else:
            print(f"Not enough {name} in inventory to remove.")
    else:
        print(f"{name} not found in inventory.")

def show_inventory():
    if inventory:
        print("Inventory:")
        for name, quantity in inventory.items():
            print(f"{name}: {quantity}")
    else:
        print("Inventory is empty.")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show Inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            add_item(name, quantity)
        elif choice == "2":
            name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            remove_item(name, quantity)
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
