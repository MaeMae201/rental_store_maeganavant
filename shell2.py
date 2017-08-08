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
    print(
        slow_type('\n Welcome to Maegans New Oreleans Themed Party Rentals '))
    core2.options()
    choice = slow_type('\n What can I help you with today? \n')
    disk.inventory_()
    if choice == '1':
        rental_choice = slow_type('\n What item would you like to rent? \n')
    if choice == '2':
        rental_choice = slow_type('\n What will you be returning today? \n')

    if rental_choice == '1':
        rental_choice = 'Mardi Gras Masks'
        rental_price = 3.50
        tax = rental_price * 0.07
        replacement_value = 5.00
        deposit = 1.50
        total_price = rental_price + tax + deposit
        print('\n Total Refund:' + '$' + str(deposit) + '\n')
        print('\n Total Cost: ' + '$' + str(total_price) + ".", sep="" + '\n')

    if rental_choice == '2':
        rental_choice = 'Outdoor Wooden Dance Floor'
        rental_price = 50.00
        tax = rental_price * 0.07
        replacement_value = 100.00
        deposit = 10.00
        total_price = rental_price + tax + deposit
        print('\n Total Refund:' + '$' + str(deposit) + '\n')
        print('\n Total Cost: ' + '$' + str(total_price) + ".", sep="" + '\n')

    if rental_choice == '3':
        rental_choice = 'Can lights'
        rental_price = 2.50
        tax = rental_price * 0.07
        replacement_value = 5.00
        deposit = 1.75
        total_price = rental_price + tax + deposit
        print('\n Total Refund:' + '$' + str(deposit) + '\n')
        print('\n Total Cost: ' + '$' + str(total_price) + ".", sep="" + '\n')

    if rental_choice == '4':
        rental_choice = 'Mardi Gras Street Signs'
        rental_price = 5.00
        tax = rental_price * 0.07
        replacement_value = 10.00
        deposit = 2.00
        total_price = rental_price + tax + deposit
        print('\n Total Refund:' + '$' + str(deposit) + '\n')
        print('\n Total Cost: ' + '$' + str(total_price) + ".", sep="" + '\n')

    if rental_choice == '5':
        rental_choice = 'Building Props'
        rental_price = 25.00
        tax = rental_price * 0.07
        replacement_value = 45.00
        deposit = 8.00
        total_price = rental_price + tax + deposit
        print('\n Total Refund:' + '$' + str(deposit) + '\n')
        print('\n Total Cost: ' + '$' + str(total_price) + ".", sep="" + '\n')
        exit()

        disk.history()


if __name__ == '__main__':
    main()