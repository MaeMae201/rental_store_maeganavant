#opening and reading,writing, or amending a file can be only done in <><><>DISK!!<><><>
import core
def history_away():
    if party == '1':
        party_inventory = 'Mardi Gras Masks'
    if party == '2':
        party_inventory = 'Outdoor wooden dance floor'
    if party == '3':
        party_inventory = 'Can Lights'
    if party == '4':
        party_inventory = 'Mardi Gras Street Signs'
    if party == '5':
        party_inventory = 'Building Props'
    message = ('{}, {}, {}, {}'.format(items, amount_in_inventory, price))
    with open('history.txt','w') as file:
        file.write(message)
    return message

def make_history():
    inventory = []
    str_1 = ['items, days, price']
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], float(split_string[1]), float(split_string[2].strip().replace('$', ''))])
    return lines

def restock():
    str_1 = ['items, amount_in_invetory, price']
    inventory = []
    for item in inventory:
        if item[2] <= 500.0:
            item[2] = 500.0
        item[2] = str(item[2])
        item[3] = str(item[3])
        str_1.append(', '.join(str_1))
    message = '\n'.join(str_1)
    with open('inventory.txt','w') as file:
        file.write(message)
    return message

def add_in():
    str_l = ['items, amount_in_inventory, price']
    inventory = []
    for item in inventory:
       message = ('{}, {}, {}, {}'.format(items, amount_in_inventory, price))
    with open('inventory.txt','w') as file:
        file.write(message)
    return True

def revenue():
    inventory = write_in_the_history()
    price = 0 
    for item in inventory:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price