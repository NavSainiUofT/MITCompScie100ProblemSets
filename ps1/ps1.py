#Navdeep Saini MIT OCW CS 1 PS1


#PART A
"""

portion_down_payment = 0.25 #25%


#annual returns
r = 0.04 #4%


annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of salary to save per month in decimal (0.1 = 10%): "))
total_cost = int(input("Enter the total cost of the home: "))

monthly_salary = annual_salary/12

current_savings = 0
counter = 0
while current_savings < total_cost*portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved

    counter +=1

print("It will take",counter,"months")
"""
#PART B
"""
portion_down_payment = 0.25 #25%


#annual returns
r = 0.04 #4%


annual_salary = int(input("PART B\nEnter your annual salary: "))
portion_saved = float(input("Enter the percentage of salary to save per month in decimal (0.1 = 10%): "))
total_cost = int(input("Enter the total cost of the home: "))
semi_annual_raise = float(input("Enter the semi-annual raise as a decimal: "))



current_savings = 0
counter = 0
while current_savings < total_cost*portion_down_payment:
    monthly_salary = annual_salary/12
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved

    counter +=1
    if counter%6 == 0:
        annual_salary += annual_salary*(semi_annual_raise)

print("It will take",counter,"months")
"""
#PART C
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25 #25%
total_cost = 1000000

months = 36

annual_salary = int(input("Please enter your salary: "))
monthly_salary = annual_salary/12

total_saved = 0

for n in range(1,months+1):
    monthly_salary = annual_salary/12
    total_saved += (total_saved*r/12) + (monthly_salary*x)

    if n%6==0:
        annual_salary += annual_salary*(1+semi_annual_raise)

#NEED TO SOLVE WHAT x WOULD MAKE THE ABOVE FOR LOOP = 
#total_cost*portion_down_payment DYNAMICALLY
#LOOK AT BISECTION SEARCH


