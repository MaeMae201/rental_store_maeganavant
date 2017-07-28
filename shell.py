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
    print(slow_type('I hope you find what you are looking for! Have a great party! 🎉'))
    deposit = slow_type('Each customer will have to pay a deposit of $25.00 for each sale')
    purchase = slow_type('Is this method okay with you?')
    if purchase == 'yes':
        print(slow_type('\nYour money will be returned once the product is inspected and not damaged\n'))
    elif purchase == 'no':
        print(slow_type('Sorry, you cant rent anything unless you pay the deposit.'))
        return None
    party_inventory = ['::::1.Mardi Gras Masks $3.50','::::2.Outdoor wooden dance floor $50.00', '::::3.Can lights $2.50','::::4.Mardi Gras Street Signs $5.00', '::::5.Building Props $25.00']
    print(*party_inventory,sep='\n')
    purchase = slow_type('\n To make a selection type in the number listed by the item. \n')
    purchase = slow_type('\n How many days will you be renting this product? \n')
    print(slow_type('\n Your total includes the deposit and sales tax. \n'))
    purchase = slow_type('\n Total cost: {:.2f}')
    print(slow_type('\n Thanks! Party On...w/out the voodoo \n'))
    
    write_in_the_history = core.sales_tax

    if purchase == 'restock':
        print(core.restock())
        return None
    if purchase == 'revenue':
        print('Your total revenue is ${:.2f}'.format(core.revenue()))
        return None


if __name__ == '__main__':
    main()