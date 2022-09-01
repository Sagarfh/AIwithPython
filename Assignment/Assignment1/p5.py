#Program for compound interest
def compound_interest(principle, rate, time):
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)

principle = int(input("Enter value of principle : "))
rate = float(input("Enter value of rate : "))
time = int(input("Enter value of time : "))

compound_interest(principle, rate, time)