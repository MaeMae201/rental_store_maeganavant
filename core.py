#functions go in the core
def get_item_prices():
    """int -> float
    """
    if party_inventory == '1':
       return 3.50
    if party_inventory == '2':
       return 50.00
    if party_inventory == '3':
       return 2.50
    if party_inventory == '4':
       return 5.00
    if party_inventory == '5':
       return 25.00
    print('Try Again.')
    return None

def sales_tax():
    while True:
        for items in party_inventory:
            price = float(days) * price
        sales_tax = 0.07
        deposit = 25.00
        days = party_inventory
        tax = price * sales_tax + deposit
        total_price = price + tax + deposit
    return total_price

def deposit():
    deposit = 25.00
    total_price = sales_tax + price + deposit + replacement_value
    return total_price

# def replacement_value():
#     replacement == .10