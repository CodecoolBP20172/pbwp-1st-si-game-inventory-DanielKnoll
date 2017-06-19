"""CodeCool - BP 2017.2 Knoll Dani - 2017.06.18.
Assignment description:
https://codecool.instructure.com/courses/64/assignments/1409?module_item_id=8193
"""
import sys


def display_inventory(inventory):
    """Displays the inventory.
    Goes through on inventory in a loop and prints out each item. value first key after.
    Lastly sums up the inventory item numbers and print out.
    """
    print("Inventory:")
    for key in inventory:
        print("{} {}".format(inventory[key], key))
    print("Total number of items: ", sum(inventory.values()))


def add_to_inventory(inventory, added_items):
    """Adds to the inventory dictionary a list of items from added_items.
    Loops through on the added_items list and if finds the same string in the dict key then
    increases that key's value by one. If there is no such key in the dict it adds that as a key
    with a value of one.
    One liner solution:
    return inventory[i] += 1 if i in inventory else inventory.update({i: 1}) for i in added_items
    """
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i: 1})
    return inventory


def print_table(inventory, order=None):
    """Creates a more readable layout, including sorted item list.
    """
    sorted_inv = []
    indent_value = 0
    indent_item = 0

    for key in inventory.keys():
        if len(key) > indent_item:
            indent_item = len(key)
        if len(str(inventory[key])) > indent_value:
            indent_value = len(str(inventory[key]))
        sorted_inv.append([inventory[key], key])

    indent_item += 4  # To make a better layout on output
    indent_value += 4

    if order == "count,asc":
        bubble_sort(sorted_inv)
    elif order == "count,desc":
        bubble_sort(sorted_inv)
        sorted_inv = sorted_inv[::-1]

    print("Inventory:")
    print("{}{}".format("count".rjust(indent_value), "item name".rjust(indent_item)))
    print("-" * (indent_value + indent_item))

    for i in sorted_inv:
        print("{}{}".format(str(i[0]).rjust(indent_value), i[1].rjust(indent_item)))

    print("-" * (indent_value + indent_item))
    print("Total number of items: ", sum(inventory.values()))


def import_inventory(inventory, filename="import_inventory.csv"):
    """Imports new inventory items from a file
    When the program reads the file it automaticly separates it too with the split built-in method.
    """
    imported_inv = ""
    try:
        with open(sys.path[0] + '/' + filename, "r") as f:  # Not a csv reader it will fail at item names with ','
            imported_inv = f.read().split(",")
    except FileNotFoundError:
        print("The file is missing.")

    inventory = add_to_inventory(inventory, imported_inv)
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    """Exports the inventory into a .csv file.
    In a double for loop it appends the the item to the export_inv list.
    One line version of the for loop:
    export_inv = ",".join(key + ("," + key) * (inventory.get(key)-1) for key in inventory)
    """
    export_inv = []
    for key in inventory:
        for value in range(inventory.get(key)):
            export_inv.append(key)
    export_inv = ",".join(export_inv)
    try:
        with open(filename, "w") as f:
            f.write(export_inv)
    except FileNotFoundError:
        print("The file is missing.")


def drop_item(inventory, key, value="All"):
    """This function allows to drop some or all specific items from inventory.
    Lets pretend that from an input function this receives the valid inventory key but an unchecked value.
    """
    if key not in inventory:  # Just to be sure I make a test
        return inventory
    elif value == "All":
        del inventory[key]
    elif value > 0:
        correct_input_given = False
        while not correct_input_given:
            try:
                value = int(value)
                correct_input_given = True
            except ValueError:
                value = input("Please use an integer number: ")
                continue
            if abs(value) < inventory[key]:
                inventory[key] -= abs(value)  # Negative number cheating is evaded.
            else:
                del inventory[key]

    return inventory
