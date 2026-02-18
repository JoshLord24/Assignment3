# This is a Portfolio Tracker

def main():

    portfolio = {}

    #input information about stock
    while True: 
        stock = input("Enter Stock Ticker('done' to finish): ")
        if stock == "done":
            break 

        shares = float(input("How many shares do you own?: "))
        price = float(input("What is the current share price?: "))
            
        portfolio[stock] = {"shares": shares, "price": price} 

    # total value calculator for the portfolio
    def total_portfolio_value(portfolio):
        total_value = 0 
       
        for stock, data in portfolio.items():
            value = data["shares"] * data["price"]
            total_value += value
        return total_value

    print(f"Portfolio Value: ${total_portfolio_value(portfolio):.2f}")

main()