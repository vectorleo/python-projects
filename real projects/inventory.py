Inventory = {'arrow':12,"gold coin":42, "rope":1 ,"torch":6 ,"dagger":1 }

def displayinventory(inven=dict):
    print("INVENTORY:")
    total_item = 0
    for k,v in inven.items():
        print(f"{str(v)} {k}")
        total_item += v
    print(f"Total items: {total_item}")

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',"bomb","bomb"]

def addToInventory(inventory1=dict, addedItems=list):
    for item in addedItems:
        if item not in inventory1:
            inventory1[item]=1
        elif item in inventory1 and item == item :
            inventory1[item] += 1
            
displayinventory(Inventory)
print("\n After dragon loot... \n")
addToInventory(Inventory,dragonLoot)
displayinventory(Inventory)
