def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return total_amount

def compound_interest(principal, rate, periods, time):
    amount = principal * (1 + (rate / periods)) ** (periods * time)
    return amount

def annuity_plan(payment, rate, time, periods):
    amount = payment * (((1 + (rate / periods)) ** (periods * time)) - 1) / (rate / periods)
    return amount

def main():
    while True:
        print("Choose a financial plan to calculate:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Annuity Plan")
        print("4. Exit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            P = float(input("Enter principal amount: "))
            r = float(input("Enter interest rate (as a decimal): "))
            t = float(input("Enter time period (in years): "))
            result = simple_interest(P, r, t)
            print("Total amount (including simple interest):", result)

        elif choice == 2:
            P = float(input("Enter principal amount: "))
            r = float(input("Enter interest rate (as a decimal): "))
            t = float(input("Enter time period (in years): "))
            n = float(input("Enter the number of periods (n): "))
            result = compound_interest(P, r, n, t)
            print("Total amount (including compound interest):", result)

        elif choice == 3:
            PMT = float(input("Enter periodic payment (PMT): "))
            r = float(input("Enter interest rate (as a decimal): "))
            t = float(input("Enter the time period (in years): "))
            n = int(input("Enter number of periods (n): "))
            result = annuity_plan(PMT, r, t, n)
            print("Annuity amount:", result)

        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
