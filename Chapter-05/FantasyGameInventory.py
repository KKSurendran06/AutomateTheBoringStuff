def displayInventory(dict):
    print('Inventory:')
    items_total = 0
    for k, v in dict.items():
        print(v, k)
        items_total += v
    print(f"Total number of items: {items_total}")    

        
inventory = {'arrow': 12,  'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
displayInventory(inventory)