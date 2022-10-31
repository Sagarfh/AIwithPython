#Program to Enter Basic Salary and Calculate Gross Salary of an Employee

# Give the basic salary as static input and store it in a variable.
basic_salary = float(input("Enter the basic salary : "))

# Calculate the value of da from the above given mathematical formula and store
# it in another variable.
gvn_da = (float)(15 * basic_salary) / 100.0

# Calculate the value of hr from the above given mathematical formula and store
# it in another variable.
house_rent_allowance = (float)(10 * basic_salary) / 100.0

# Calculate the value of da-on-ta from the above given mathematical formula and store
# it in another variable.
gvn_da_on_ta = (float)(3 * basic_salary) / 100.0

# Calculate the gross salary using the above given mathematical formula and store
# it in another variable.
gros_sal = basic_salary + gvn_da + house_rent_allowance + gvn_da_on_ta

# Print the Gross salary of an employee from the given basic salary.
print("The Employee's Gross salary from the given basic salary {", basic_salary, "} =", gros_sal)