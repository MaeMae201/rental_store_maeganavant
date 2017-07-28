#functions go in the core
import disk
def get_item_price():
    """int -> float
    """
    if party_inventory == '1':
       return 3.50
    if party_inventory == '2':
       return 30.50
    if party_inventory == '3':
       return 50.00
    if party_inventory == '4':
       return 50.00
    if party_inventory == '5':
       return 2.50
    if party_inventory == '6':
       return 5.00
    if party_inventory == '7':
       return 25.00
    if party_inventory == '8':
       return 3.19
    print('Try Again.')
    return None

def payment_options():
    if purchase == 'pre-pay':
        party_inventory = core.prepay(party_inventory)
        return purchase
    elif purchase == 'pay after':
        party_inventory = core.pay_after(party_inventory)
        #core.history(party_inventory,items, dollars)
    return purchase

def sales_tax():
    for items in party_inventory:
        price = float(history_txt) + days
        sales_tax = 0.07
        deposit = 25.00
        days = party_inventory
        tax = price * sales_tax + deposit
        total_price = price + tax + deposit
        return total_price