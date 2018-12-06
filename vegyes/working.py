inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Displays the inventory.
def display_inventory(inv):
    print("Inventory:")
    for k, v in inv.items():
        print(v, k)
    total = sum(inv.values())
    print("Total number of items: ", total)

display_inventory(inv)

added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']



def add_to_inventory(inv, added_items):      
    to_add = {}
    b = inv 
    for items in added_items: 
        to_add[items] = added_items.count(items)
        a = to_add
    for k in b: #for key in added_items
        if k in a: #if key is in inv
            b[k] = b[k] + a[k] #added_items key = added_items key + inv key
    c = {**a, **b}
    inv.update(c)
    return inv

def print_table(inv, order=None):
    order = input("Order? ")
    count = 0
    for i in inv:
        if len(i) > count:
            count = len(i)
            x = len(i)
    print("Inventory:")
    print("Count".rjust(10), "Item name".rjust(x+10))
    print(("-") * (x+21))
    if order == "count, asc":
        for k, v in sorted(inv.items(), key=lambda x: x[1]):
            a = str(k)
            b = str(v)
            print(b.rjust(10), a.rjust(x+10))
    elif order == "count, desc":
        for k, v in sorted(inv.items(),reverse=True, key=lambda x: x[1]):
            a = str(k)
            b = str(v)
            print(b.rjust(10), a.rjust(x+10))
    else:
        order == "None"
        for k, v in inv.items():
            a = str(k)
            b = str(v)
            print(b.rjust(10), a.rjust(x+10))
    total = sum(inv.values())
    c = str(total)
    print(("-") * (x+21))
    print("Total number of items: ", c.rjust(x-3))

add_to_inventory(inv, added_items)
display_inventory(inv)
print_table(inv)