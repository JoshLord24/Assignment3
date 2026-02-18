# Sales Commission Calculator

def main():
    
    sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

    commissions = {}

    for employee, amount in sales.items():
        commissions[employee] = amount * .1
    
    ranked = sorted(commissions.items(), key=lambda x: x[1], reverse=True)

    print("Commission Leaderboard:")
    for rank, (employee, commissions) in enumerate(ranked, start=1):
        print(f"{rank}, {employee}, ${commissions:.2f}")
main()

