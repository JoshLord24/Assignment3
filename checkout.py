#This Program Simulates checking out in a Retail store

def main():

# Appendix for the prices Entered
    prices = []

    print("Enter the price of each item. Type 0 when finished.")

# Loops to get the price of each item until the user enters 0
    while True:
        price = float(input("Price: "))
        if price == 0:
            break
        prices.append(price)

# Calculates the total items, total cost, and average cost per item
    total_items = len(prices)
    total_cost = sum(prices)
    average_cost = total_cost / total_items if total_items > 0 else 0

# Prints the results
    print(f"Total items: {total_items}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Average cost per item: ${average_cost:.2f}")
        
main()