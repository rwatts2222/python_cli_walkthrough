# And Import Statement to make code from other files available
from models.item import Item  # Imports class from item.py
import csv  # Imports csv (comma separated values file format)

next_id = 0  # starts id number at 0
items = []  # This will be used to store items

def menu():  # Prints Menu Options for the user
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")


def list_items():  # Writes all items to the Terminal
    """
    1) Read the file into Python
    2) Parse the file into usable data
    3) Print out each item in the file
    """

    with open('inventory.csv', 'r') as file:  # opens inventory.csv in 'r' readable format (stream from beginning) as the variable, "file"
        csv_reader = csv.DictReader(file)  # create variable that performs csv.DictReader function on "file"
        for row in csv_reader:  # DictReader sorts file elements into rows, so we use "row" to refer to file elements.
            message = f"ID: { row['id'] }\tName: { row['name'] }\tCondition: {row['condition'] }"  # assign variable to our row info
            print(message)


def new_item():  # Gets user input for all needed fields for an Item
    """
    1) Open and parse the file into CSV
    2) Detect what the next id will be
    3) Prompt the user for new item data (name, condition)
    4) Add this item to the inventory.csv file
    """

    with open('inventory.csv', 'r+') as file:  # opens inventory.csv in 'r+' read/write format (stream from beginning) as the variable, "file"
        current_items = list(csv.DictReader(file))  # create variable that performs csv.DictReader function on "file"
        try:
            last_id = int(current_items[-1]['id'])  # determines what next item id will be, based on the last item's id.
        except IndexError:
            last_id = -1   # if last item id is 0, it will not assign an id of -1

    with open('inventory.csv', 'a+', newline='') as file:  
        name = input('Name: > ')
        condition = input('Condition: > ')
        item = {
            "id": last_id + 1,
            "name": name,
            "condition": condition
        }
        writer = csv.DictWriter(file, ["id", "name", "condition"])
        if last_id == -1:
            writer.writeheader()
        writer.writerow(item)

    # global next_id  # Allows us access to the next_id number

    # name = input("Name: ")
    # cond = input("Condition: ")
    # # Uses the global counter to give a Unique Id for each "Item"
    # item_id = next_id

    # next_id += 1  # Updates Id with new value so next one is 1 more

    # # This is the Class -> Item from the other file we imported
    # tmp = Item(item_id, name, cond)  # Builds An Item/Stores it in tmp

    # items.append(tmp)  # Adds Item to global items array


def update_existing():  # Update Existing Item
    print("inside update existing")
    if not items:
        print("You have no items to update")
        return
    list_items()
    try:
        item_id_to_update = int(input("What is the item id you wish to update\n> "))
    except Exception:
        print("Not a valid number.")
        return

    for item in items:
        if item.item_id == item_id_to_update:
            item.name = input("Name: ")
            item.condition = input("Condition: ")
            break
    else:
        print("We didn't find a match")


# Delete Item (By item id)
def delete_item():
    if not items:
        print("You have no items to delete")
        return
    list_items()
    try:
        item_id_to_delete = int(input("What is the item id you wish to update\n> "))
    except Exception:
        print("Not a valid number.")
        return

    for index, item in enumerate(items):
        if item.item_id == item_id_to_delete:
            index_to_remove = index
            break
    else:
        print("We didn't find a match")
        return
    removed_item = items.pop(index_to_remove)
    print(f"Found:\n{removed_item} it has been removed")


def main():  # Starts the Program off, holds the loop until exit.
    # Detect if the inventory.csv file exists. Create it if not.
    open("inventory.csv", 'a+').close()
    while True:
        menu()  # Prints the Options to the Terminal
        choice = input("> ")  # Takes use choice

        # The Conditional Options: hands off the work to the functions above.
        if choice == "1":
            list_items()
        elif choice == "2":
            new_item()
        elif choice == "3":
            update_existing()
        elif choice == "4":
            delete_item()

        elif choice == "5":  # Exit
            exit()
        else:  # User gave us bad input we let them know then loop again.
            input("Invalid Input!\n(Press Enter to try again)")


# TODO Make the File Saving stuff

if __name__ == "__main__":
    main()