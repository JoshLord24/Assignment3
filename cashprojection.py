# Business Growth Projection (10 Years)

def main():
    
    revenue = float(input("Enter Cash Flow: "))

    growth_rate = float(input("Enter Growth Rate: %"))

    growth = growth_rate / 100


    for year in range(1, 11 ):
        revenue  = revenue * (1 + growth)
        print(f"{year}\t${revenue: .2f}")
main()
