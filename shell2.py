import core2
import disk
import time, sys
typing_speed = 12


def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


def main():
    print('\n Welcome to Maegans New Oreleans Themed Party Rentals ')
    time.sleep(1.3)
    core2.options()

    choice = slow_type('\n What can I help you with today? \n')
    print('\n\nDisplaying inventory...')
    time.sleep(1)

    if choice == '1':
        disk.inventory_()
        rental_choice = slow_type('\nWhat item would you like to rent today? ')

        if rental_choice == '1':
            item = 'Mardi Gras Mask'
            days = slow_type(
                '\nHow many days would you like to rent this item? ')
            rental_price = disk.price(rental_choice)
            rental_replacement_cost = disk.replacement_cost(rental_choice)
            total = core2.total_cost(rental_price, days,
                                     rental_replacement_cost)
            print('Total Cost: $', total)

            disk.update_history(item, days, rental_price, total)

        if rental_choice == '2':
            item = 'Outdoor Wooden Dance Floor'
            days = slow_type(
                '\nHow many days would you like to rent this item? ')
            rental_price = disk.price(rental_choice)
            rental_replacement_cost = disk.replacement_cost(rental_choice)
            total = core2.total_cost(rental_price, days,
                                     rental_replacement_cost)
            print('Total Cost: $', total)

            disk.update_history(item, days, rental_price, total)

        if rental_choice == '3':
            item = 'Can Lights'
            days = slow_type(
                '\nHow many days would you like to rent this item? ')
            rental_price = disk.price(rental_choice)
            rental_replacement_cost = disk.replacement_cost(rental_choice)
            total = core2.total_cost(rental_price, days,
                                     rental_replacement_cost)
            print('Total Cost: $', total)

            disk.update_history(item, days, rental_price, total)

        if rental_choice == '4':
            item = 'Mardi Gras Street Signs'
            days = slow_type(
                '\nHow many days would you like to rent this item? ')
            rental_price = disk.price(rental_choice)
            rental_replacement_cost = disk.replacement_cost(rental_choice)
            total = core2.total_cost(rental_price, days,
                                     rental_replacement_cost)
            print('Total Cost: $', total)

            disk.update_history(item, days, rental_price, total)

        if rental_choice == '5':
            item = 'Building Props'
            days = slow_type(
                '\nHow many days would you like to rent this item? ')
            rental_price = disk.price(rental_choice)
            rental_replacement_cost = disk.replacement_cost(rental_choice)
            total = core2.total_cost(rental_price, days,
                                     rental_replacement_cost)
            print('Total Cost: $', total)

            disk.update_history(item, days, rental_price, total)
            disk.update_inventory(trans)


if __name__ == '__main__':
    main()