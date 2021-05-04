import pprint
eq = {'rope':1, 'torch':6, 'gold coin':42, 'dagger': 1, 'arrow':12, 'knife':2}

def properName(item, amount):
    plural_item = item
    if amount > 1:
        if plural_item[-2:] == 'ch':
            return plural_item + 'es'
        elif plural_item[-2:] == 'fe':
            return plural_item[:-2] + 'ves'
        else:
            return plural_item + 's'
    return item

def displayEq(inventory):
    print("Inventory: ")
    item_total = 0
    for item, amount in inventory.items():
        print(properName(item, amount) + ' = ' + str(amount))
        item_total += amount
    print("Total number of items: " + str(item_total))

displayEq(eq)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToEq(inventory, addedItems):
    for k in addedItems:
        if k in inventory:
            inventory[k] += 1
        else:
            inventory[k] = 1
    return inventory

updatedEq = addToEq(eq, dragonLoot)
displayEq(updatedEq)
