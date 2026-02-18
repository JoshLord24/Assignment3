# Bank Loan Repayment Simulator

def main():

    # Loan inputs
    amount = float(input("Enter your Loan Amount: "))
    interest_rate = float(input("Enter your interest rate: "))
    monthly_payment = float(input("Enter your monthly repayment: "))

    # annualizing rate
    monthly_rate = interest_rate / 100 / 12

    balance = amount
    months = 0

    while balance > 0:
        balance = balance + (balance * monthly_rate)

        balance = balance - monthly_payment

        months += 1

    if balance > amount and months > 12:
        print("Payment to little, loan will not be paid off")
        return
    
    print(f"It will take {months} months to repay your loan.")
main()

    
    