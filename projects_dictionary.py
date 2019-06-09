inventory = {"sword": 1, "gold": 140, "arrows": 120, "potions": 4}


def displayInventory(inventory):
    item_count = 0
    for k, v in inventory.items():
        item_count = item_count + int(v)
        print(str(v) + " " + k)
    print("\nTotal number of items: " + str(item_count))


displayInventory(inventory)
