#functions go in the core
def calculate_totals(purchase):
    days = 365
    prices = 0.00
    replacement_value = .10
    deposit = 5.00
    sales_tax = purchase * .07
    total_price = purchase + sales_tax + deposit + replacement_value
    print('\n 𝓣𝓸𝓽𝓪𝓵 𝓒𝓸𝓼𝓽: '+ '$' + str(total_price) + ".",sep="" + '\n')

def shopping_inven():
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