def inventory_():
    with open('inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
        for item in items:
            print(item)


def replacement_cost(num):
    """ (str) -> (int)
    Returns my replacement cost from
    inventory.txt
    """
    with open('inventory.txt', 'r') as file:
        file.readline()
        item = file.readlines()
    for i in item:
        if num in i:
            parts = i.split(', ')
            replacement_cost = parts[3].strip()
            return replacement_cost


def price(num):
    """(str) -> (int)
    Returns my price for the rent of
    the item from inventory.txt
    """
    with open('inventory.txt', 'r') as file:
        file.readline()
        item = file.readlines()
    for i in item:
        if num in i:
            parts = i.split(', ')
            price = parts[3].strip()
            return price


def update_history(item, days, rental_price, total):
    """ -> (txt)
    Will print text in history.txt of every transaction made.
    """
    transaction = '{}, {}, {}, {} \n'.format(item, days, rental_price, total)
    with open('history.txt', 'a') as file:
        file.write(transaction)


def update_inventory(item, quantity, price, replacement_cost):
    """ -> (txt)
    Will update when an item is purchased,
    and prints to inventory how many items
    are left
    """
    trans = '{}, {}, {}, {} \n'.format(quantity)
    with open('inventory.txt', 'a') as file:
        for quantity in quantities:
            if quantity <= 500:
                file.write(trans)
                return quantity