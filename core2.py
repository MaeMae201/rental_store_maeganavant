def options():
    ''' -> str
    Prints options to user
    '''
    options = ['\n1. Rent an item', '\n2. Returning an item']

    for choice in options:
        print(choice)


def total_cost(price, days, replacement_cost):
    """ (float, int, int) -> (float)
    Returns total cost of the rental for the
    days rented with tax and all.
    """
    tax = 0.07
    deposit = 0.10

    cost = float(price) * float(days)
    cost_w_tax = cost * tax + cost
    depos = replacement_cost * int(deposit)
    total_rental_cost = str(cost_w_tax) + str(depos)

    return str(total_rental_cost)