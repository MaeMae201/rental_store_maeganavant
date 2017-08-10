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
            replacement_cost = parts[3]
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
            price = parts[3]
            return price


def update_history(item, days, rental_price, total):
    """ -> (txt)
    Will print text in history.txt of every transaction made.
    """
    transaction = '{}, {}, {}, {} \n'.format(item, days, rental_price, total)
    with open('history.txt', 'a') as file:
        file.write(transaction)