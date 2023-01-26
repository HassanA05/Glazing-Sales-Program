
def bonusCalculation(sales_cash):

    if sales_cash > 5000.00:

        bonus = sales_cash * 0.20

    elif sales_cash >= 2000.00:

        bonus = sales_cash * 0.10
        
    else:
        
        bonus = 0.00

    return bonus


def percentDecimal (percentage):

    percent_decimal = (float(percentage) / 100)

    return percent_decimal


#test prog for functions

#sales = float(raw_input("practice sales amount - "))
#sales_bonus = bonusCalculation(sales)
#print sales_bonus

#tax = int(raw_input("practice tax integer - "))
#percent = percentDecimal (tax)
#print percent
