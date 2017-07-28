#the built in functions input() and print() can only be called in the SHELL!!<<<>>>>
import disk
import time,sys
typing_speed = 12
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()
def main():
    print(slow_type('\n 🎭Welcome to Maegans New Orleans Themed Party Rentals🎭 \n'))
    print(slow_type('\n Press "ENTER" to continue'))
    print(slow_type('I hope you find what you are looking for! Have a great party! 🎉'))
    print(slow_type('Each customer will have to pay a deposit of $25.00 for each sale'))
    purchase = slow_type('Is this method okay with you?')
    if purchase == 'yes':
        print(slow_type('\nYour money will be returned once the product is inspected and not damaged\n'))
    elif purchase == 'no':
        print(slow_type('Sorry, you cant rent anything unless you pay the deposit.'))
        return None
    party_inventory = ['::::1.Mardi Gras Masks $3.50', '::::2.Staging Rentals $30.50', '::::3.Indoor Dance Floor $50.00', '::::4.Outdoor wooden dance floor $50.00', '::::5.Can lights $2.50','::::6.Mardi Gras Street Signs $5.00', '::::7.Building Prop $25.00', '::::8.Street Props $3.19']
    print(*party_inventory,sep='\n')
    purchase = slow_type('\n To make a selection type in the number listed by the item. \n')
    purchase = slow_type('\n How many days will you be renting this product? \n')
    purchase = slow_type('\n Would you like to pre-pay or pay after? \n')


    if purchase == 'refuel':
        print(core.refuel())
        return None
    if purchase == 'revenue':
        print('Your total revenue is ${:.2f}'.format(core.revenue()))
        return None

if __name__ == '__main__':
    main()