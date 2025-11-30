print("Name = Ritesh Dhekane")


class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest  # interest rate (e.g., 0.05 for 5%)

    def value_after(self, n):
        value = self.principal * (1 + self.interest) ** n
        return value


# Example usage:
p = float(input("Enter principal amount: "))
i = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))
years = int(input("Enter number of years: "))

inv = Investment(p, i)
final_value = inv.value_after(years)

print(f"\nValue after {years} years = {final_value:.2f}")
