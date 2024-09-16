salary = 0 
numDependents = 0
stateTax = 0
federalTax = 0
dependentDeduction = 0 
totalWithholding = 0
takeHomePay = 0

# input statements
salary = float(input("Please enter your salary amount: ))
numDependents = float(input("Please enter your number of dependents: ))

# calculate taxes here
stateTax = salary * .28
print("Federal Tax: $" + str(federalTax))
print("Federal Tax: $" + str(federalTax))
dependentDeduction = (salary * 0.025) * numDependents
print("Dependents: $" + str(dependentDeduction))
totalWithhodling = stateTax + federalTax + dependentDeduction 

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
