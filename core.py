#functions go in the core
import disk
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
    for items in party_inventory:
        price = float(days) * price
        sales_tax = 0.07
        deposit = 25.00
        days = party_inventory
        tax = price * sales_tax + deposit
        total_price = price + tax + deposit
        return total_price