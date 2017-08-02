#functions go in the core
class something():
    def get_item_prices(self):
        """
        """
        party_inventory = []
        if party_inventory == '1' or 'Mardi Gras Masks':
            return 3.50
        if party_inventory == '2' or 'Outdoor wooden dance floor':
            return 50.00
        if party_inventory == '3' or 'Can Lights':
            return 2.50
        if party_inventory == '4' or 'Mardi Gras Street Signs':
            return 5.00
        if party_inventory == '5' or 'Building Props':
            return 25.00
            print('Try Again.')
            s = something
            s.out()
            return None

def sales_tax_other():
    """ Returning the final cost of everything
    """
    amount_of_days = int(days) * float(price)
    replacement_value = .10
    sales_tax = 0.07
    deposit = 25.00
    tax = amount_of_days * sales_tax
    total_price = amount_of_days + tax + deposit + replacement_value
    return total_price