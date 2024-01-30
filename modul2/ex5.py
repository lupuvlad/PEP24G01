# Get user input for monthly income
# Calculate the 50/30/20 rule:
# - 50% of the income for the necessities
# - 30% of the income for the recreation activities
# - 20% of the income for the debts and savings

# User input for income
income = int(input("Income: "))

# Create variables and store the result for the calculations
necessities = income * 0.5
recreation = income * 0.3
debtsAndSavings = income * 0.2

# Print the results
print(f"""
Income: {income}

Necessities: {necessities}
Recreation activities: {recreation}
Debts and savings: {debtsAndSavings}
""")
