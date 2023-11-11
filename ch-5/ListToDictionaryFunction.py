import copy


def displayInventory(inventory):
    items_total = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(v, k)
        items_total += v
    print()
    print(f"Total number of items: {items_total}") 
    
    

def addToInventory(inventory, addedItems):
    new_inventory = copy.deepcopy(inventory)
    
    for item in addedItems:
        new_inventory[item] = new_inventory.get(item, 0) + 1

    return new_inventory

    
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
