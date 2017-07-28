#opening and reading,writing, or amending a file can be only done in <><><>DISK!!<><><>
import core
def take_away(party_inventory, items):
    str_l = ['code, items, amount_in_inventory, price']
    for item in inventory:
        if item[1] == party_inventory:
            if dollars > item[2]:
                print("Sorry, we dont have no more of that item in stock.")
                return False
        str_l.append('{}, {}, {}, {}'.format(item[0], item[1], item[2], item[3]))
        message = '\n'.join(str_l)
    with open('inventory.txt','w') as file:
        file.write(message)
    return True

def in_the_history():
    inventory = []
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], float(split_string[1]), float(split_string[2].strip().replace('$', ''))])
    return inventory

def all_inventory():
    inventory = []
    with open('inventory.txt','r') as file:
        file.readline()
        str_inventory = file.readlines()
    for item in str_inventory:
        sub_list = item.strip().split(', ')
        inventory.append([sub_list[0], sub_list[1], float(sub_list[2]), float(sub_list[3])])
    return inventory

def refuel():
    str_1 = ['code, items, amount_in_invetory, price']
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