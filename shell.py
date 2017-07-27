#the built in functions input() and print() can only be called in the SHELL!!<<<>>>>
import core
import disk
import time,sys
typing_speed = 17
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()
def main():
    print(slow_type('\n 🎭Welcome to Maegans New Orleans Themed Party Rentals🎭 \n'))
    print(slow_type('\n Press "ENTER" to continue'))
    print(slow_type('We have many selections that will blow you away!'))
    print(slow_type('I hope you find what you are looking for! Have a great party! 🎉'))
    print(slow_type('Each customer will have to pay a deposit of $25.00 for each sale'))
    purchase = slow_type('Is this method okay with you?')
    if purchase == 'yes':
        print(slow_type('Your money will be returned once the product is inspected and not damaged'))
    elif purchase == 'no':
        print(slow_type('Sorry, you cant rent anything unless you pay the deposit.'))
        return None
    party_invetory = ['1.Mardi Gras Masks $3.50', '2.Staging Rentals $30.50', '3.Indoor Dance Floor $50.00', '4.Outdoor wooden dance floor $50.00', '5.Can lights $2.50','6.Mardi Gras Street Signs $5.00', '7.Building Prop $25.00', '8.Street Props $3.19']
    print(*party_invetory,sep='\n')
    purchase = slow_type('\n To make a selection type in the number listed by the item. \n')
    purchase = slow_type('\n Would you like to pre-pay or pay after? \n')
    # if purchase == party_invetory():
    #     print('You have chosen, {} , Total sales: ${:.2f}'.format(core.get_item_price))
    
    if purchase == 'refuel':
        print(core.refuel())
        return None
    
    if purchase == 'revenue':
        print('Your total revenue is ${:.2f}'.format(core.revenue()))
        return None

    if purchase == 'pre-pay':
        (dollars, party_invetory) = core.prepay(party_invetory)

    elif purchase == 'pay after':
        (dollars, party_invetory) = core.pay_after(party_invetory)
        core.history(party_invetory,items, dollars)

def main_tax():
     purchase = float(input('Enter the price of the purchase: '))
     calculate_totals(purchase)
     county_sales_tax = purchase * .025 
     state_sales_tax = purchase * .05
     total_sales_tax = county_sales_tax + state_sales_tax
     total_price = purchase + state_sales_tax + county_sales_tax

def display_totals(purchase, state_sales_tax, county_sales_tax, total_taxes, total_price):
  print('The purchase price is $, ')
  print('The county_sales_tax is $', \
    format (county_sales_tax, '.2f'))
  print('The state_sales_tax is $', \
    format (state_sales_tax, '.2f'))
  print('The total_sales_tax is $:, ')
  print('The total_price is $:, ')
  return main()


if __name__ == '__main__':
    main()