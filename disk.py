#opening and reading,writing, or amending a file can be only done in <><><>DISK!!<><><>
import core
def make_history():
    quantity = {"Mardi Gras Masks":500, "Outdoor Wooden Dance Floor":500, "Can Lights":500,"Mardi Gras Street Signs":500, "Building Props":500}
    inventory = []
    str_1 = ['items, days, price']
    with open('history.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], float(split_string[1]), float(split_string[2].strip().replace('$', ''))])
    return quantity


def make_history_2():
    inventory = []
    with open('history.txt','w') as file:
        file.writelines()
        lines = file.writelines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], float(split_string[1], float(split_string[2].strip().replace('$', '')))])
    return inventory

def restock():
    str_1 = ['items, quantity, price']
    inventory = []
    for items in inventory:
        if items[2] <= 500.0:
            items[2] = 500.0
        items[2] = str(items[2])
        str_1.append(', '.join(str_1))
    message = '\n'.join(str_1)
    with open('inventory.txt','w') as file:
        file.write(message)
    return message

def add_in():
    str_l = ['items, quantity, price']
    inventory = []
    for items in str_l:
       message = ('{}, {}, {}, {}'.format(items, quantity, price))
    with open('inventory.txt','w') as file:
        file.write(message)
    return True

# def revenue():
#     inventory = make_history()
#     price = 0
#     for items in inventory:
#         items[2] = float(items[2]) + float(items[2])
#         price += items[2]
#     return price