inventory = [{"name" : "Apple", "quantity" : 10, "price" : 1.5},
             {"name" : "Orange", "quantity" : 15, "price" : 1.0},
             {"name" : "Grapes", "quantity" : 7, "price" : 0.5}
             ]
def display_inventory():
    print("Current Inventory : \n")
    sorted_inventory = sorted(inventory, key = lambda x : x['name'])
    for item in sorted_inventory:
        print(f"{item['name']} - Quantity : {item['quantity']} - Price : {item['price']}")
    print()


def add_item(name, quantity, price):
    for item in inventory:
        if item['name'].lower() == name.lower():
            item[quantity] += quantity
            print(f"updated {name} quantity to {item[quantity]}")
            return
    inventory.append({"name" : name, "quantity" : quantity, "price" : price})
    print(f"Added {name} added to inventory")

def update_item(name, qunatity):
    for item in inventory:
        if item['name'].lower() == name.lower():
            item['quantity'] = qunatity
            print(f"updated {name} quantity to {quantity}.")
            return
    print(f"{name} not found in inventory")

def remove_out_of_stock():
    global inventory
    inventory = [item for item in inventory if item['quantity'] > 0]
    print("Removed out-of-stock items")


while True:
    print("\n1. Display Inventory")
    print("\n2. Add Item")
    print("\n3. Update Quantity")
    print("\n4. Remove Out Of Stock Item")
    print("\n5. Exit")

    choice = int(input("Enter you choice:"))

    if(choice == 1):
        display_inventory()

    elif (choice == 2):
        name = input("Enter Item name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter price: "))
        add_item(name, quantity, price)
    
    elif (choice == 3):
        name = input("Enter Item name: ")
        quantity = int(input("Update new Quantity: "))
        update_item(name, quantity)
    
    elif (choice == 4):
        remove_out_of_stock()

    elif (choice == 5):
        print("Exiting the program")
        break
    else:
        print("Inavalid choice! please try it again!")