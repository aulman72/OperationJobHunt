# sets the amount you are looking to invest
sum_of_investment = input("Enter the total amount your looking to spend.")
sum_of_investment = int(sum_of_investment)

# sets the price of the stock you are looking to purchase
stock_price = input("Enter the price of the stock.")
stock_price = float(stock_price)

# Finds 2% of the total amount invested
number_shares = sum_of_investment * .02

# checks to make sure the stock is not more than 2% of the total investment and then prints the desired information
if number_shares > stock_price:
    number_shares = number_shares / stock_price
    number_shares = round(number_shares)
    print("You should purchase " + str(number_shares) + " shares.")
    total_transaction_price = number_shares * stock_price
    print("The total amount you are spending towards this transaction is " + str(total_transaction_price))
    thirty_eight_n_half_profit = stock_price * .385
    print("Your profit per share at 38.5% is " + str(thirty_eight_n_half_profit))
    thirty_eight_n_half_sell = (stock_price * .385) + stock_price
    print("Should sell when security gets to or above " + str(thirty_eight_n_half_sell) + " for 38.5% profit")
    thirty_eight_n_half = thirty_eight_n_half_sell * (number_shares / 2)
    fifty_profit = stock_price * .5
    print("Your profit per share at 50% is " + str(fifty_profit))
    fifty_sell = (stock_price * .5) + stock_price
    print("Should sell when security gets to or above " + str(fifty_sell) + " for 50% profit")
    fifty = fifty_sell * (number_shares / 2)
    total_profit = thirty_eight_n_half_profit + fifty_profit * number_shares
    print("Total profit of this transaction is " + str(total_profit))

# if the stock is more than the desired 2%, prints the following statement
else:
    print("Share was more than the 2% risk")
