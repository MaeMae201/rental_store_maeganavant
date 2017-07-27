#functions go in the core
import disk

def get_item_price():
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

def pay_after(party_inventory):
    """
    """
    items = float(input('You have chosen, {} , is this correct?'.format(8))
    price = float(history_txt(party_inventory,items, dollars))
    dollars = items * price
    print('\nYour total is: $', round(dollars, 2), sep='')
    return [dollars, items, party_inventory]

def prepay(party_inventory):
    """
    """
    money = float(input('\n How many items are you purchasing today?\n'))
    price = float(history_txt(party_inventory))
    items = money / price
    print('\nTotal amount of items purchased:\n', round(items, 2))
    return [money, items, party_inventory]

def revenue():
    inventory = in_the_history()
    price = 0 
    for item in inventory:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price

def calculate_totals(purchase):
    county_sales_tax = purchase * .025 
    state_sales_tax = purchase * .05
    total_sales_tax = county_sales_tax + state_sales_tax
    total_price = purchase + state_sales_tax

def history_txt():
    if party_inventory == '1':
        party_inventory = 'Mardi Gras Masks $3.50'
    if party_inventory == '2':
         party_inventory = 'Staging Rentals $30.50'
    if party_inventory == '3':
         party_inventory = 'Indoor Dance Floor $50.00'
    if party_inventory == '4':
         party_inventory = 'Outdoor wooden dance floor $50.00'
    if party_inventory == '5':
         party_inventory = 'Can lights $2.50'
    if party_inventory == '6':
         party_inventory = 'Mardi Gras Street Signs $5.00'
    if party_inventory == '7':
         party_inventory = 'Mardi Gras b-day card invitations $3.50'
    if party_inventory == '8':
         party_inventory = 'Design a room package $15.99'
    if party_inventory == '9':
         party_inventory = 'Building Prop $25.00'
    if party_inventory == '10':
         party_inventory = 'Street Props $3.19'
    message = '{}, {}, {}\n'.format(party_inventory, dollars, items)

    message = '{}, {}, {}\n'.format(party_inventory, dollars, items)
    with open('history.txt','a') as file:
        file.write(message)
    return party_inventory