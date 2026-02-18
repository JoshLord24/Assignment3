# Customer Loyalty Tiers

def main():
    
    #Customer Dictionary
    customers =[
        {"Name": "Alice", "total": 5000},
        {"Name": "John", "total": 2000},
        {"Name": "Anthony", "total": 10000},
        {"Name": "Uncle Jun", "total": 700},
        {"Name": "Bill", "total": 3500}
    ]
    #Tier Dictionary
    loyalty_tiers = {
        "Bronze": 0,
        "Silver": 0,
        "Gold": 0
    }

    # determines what tier each customer falls in and counts it
    for customer in customers:
        amount = customer["total"]

        if amount < 1000:
            loyalty_tiers["Bronze"] += 1
        elif amount < 5000:
            loyalty_tiers["Silver"] += 1
        else:
            loyalty_tiers["Gold"] += 1

    # Summary of results
    print("Summary:")
    for tier, count in loyalty_tiers.items():
        print(f"{tier}: {count}")

main()

    

    