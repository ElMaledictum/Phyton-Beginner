

def display_inventory(stuff):
    item_total = 0
    print ("Inventory: ")

    for key,value in stuff.items():
        print (f'{key} - {value}')
        item_total += stuff[key]

    return (f'Total number of item: {item_total}')

def addToInventory (inventory,addedItems): 
     
    for objects in addedItems:
        inventory.setdefault(objects,0)
        inventory[objects] += 1 #unique_items is neew dict of dragonloot
    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope', 'arrow'] #added items
loots = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

print (display_inventory(loots))

print (display_inventory((addToInventory(loots, dragonLoot))))

