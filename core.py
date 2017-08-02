#functions go in the core
def sales_tax_other():
    """
    """
    amount_of_days = int(days) * float(prices)
    replacement_value = .10
    sales_tax = 0.07
    deposit = 25.00
    tax = int(amount_of_days) * float(sales_tax)
    total_price = int(amount_of_days) + tax + float(deposit) + float(replacement_value)
    #return total_price
    print('\n 𝓣𝓸𝓽𝓪𝓵 𝓒𝓸𝓼𝓽:${:.2f} \n')

def shopping_inven(items):
    stock = {
        "Mardi Gras Masks":500, 
        "Outdoor Wooden Dance Floor":500, 
        "Can Lights":500,
        "Mardi Gras Street Signs":500, 
        "Building Props":500
        }
    prices = {
        "Mardi Gras Masks":3.50,
        "Outdoor Wooden Dance Floor":50.00,
        "Can Lights":2.50,
        "Mardi Gras Street Signs":5.00,
        "Building Props":25.00
    }

def compute_bill(items):
    total = 0 
    if stock[items] > 0:
            total += prices[items]
            stock[items] -= 1    
    return total