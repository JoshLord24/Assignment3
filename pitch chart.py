# This is a Startup Pitch Deck Visualiser

def main():

    # Sample projected revenues
    revenues = [3, 5, 8, 7, 10, 11, 12, 14]

    print("Projected Revenue by Year: \n")

    # Generates the "Year [x]" values and ties it to the revenues
    for year, value in enumerate(revenues, start= 1):
        bar = "#" * value
        print(f"Year {year}: {bar}")
main() 

