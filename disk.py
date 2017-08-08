def inventory_():
    with open('inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
        for item in items:
            print(item)


def inventory():
    with open('inventory.txt', 'w') as file:
        file.writeline()
        Quantity = file.writelines()
        for item in Quantity:
            if Quantity < 500:
                return 500


def history():
    with open('history.txt', 'w') as file:
        file.writelines()
        str_1 = ['Items:', 'Total:', 'Refund:']
        print(str_1)
