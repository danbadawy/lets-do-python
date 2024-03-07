#!/usr/bin/env python
# coding: utf-8

# ## Min and Max scores

# In[1]:


scores = [97, 87, 92, 75, 87, 100, 83, 91, 88, 87, 69, 98, 89, 91, 100, 89, 87, 39, 20, 79, 85, 80]

# Ask user for min and max
min_score = float(input("Enter min score: "))
max_score = float(input("Enter max score: "))

# make sure min and max are in order
if max_score < min_score:
    print("Error: max score should be greater than or equal to the min score.")
else:
    # see how many scores fall within the inputs
    count = sum(1 for score in scores if min_score <= score <= max_score)
    print(f"The number of scores between {min_score} and {max_score} is: {count}")


# ## Question 2 Adding positive and negative integers 

# In[2]:


#variables for counting inputs
sum_pos = 0
sum_neg = 0
input_count = 0

# Ask for inout until sentinel is entered
while True:
    user_input = int(input("Enter integers ,enter 9999 at end: "))
    
    # make sure sentinel works 
    if user_input == 9999:
        break
    
    # add input count
    input_count += 1
    
    # Update sums based on inputs 
    if user_input >= 0:
        sum_pos += user_input
    else:
        sum_neg += user_input

# Display the results
print(f"Number of inputs processed (excluding sentinel): {input_count}")
print(f"Sum of positive inputs: {sum_pos}")
print(f"Sum of negative inputs: {sum_neg}")


# ## Question 3 Clothing tax calculation

# In[14]:


#prices
prices= [57.70, 13.75,39.00, 26.50, 11.95, 18.50, 47.90, 11.99]

total_cost= 0

# make a loop to calculate unique tax rates
for price in prices:
    total_cost += price
    if price < 15:
        total_cost += price * 0.017
    #higher tax rate
    else:
        total_cost+= price * 0.0765
# round total_cost 
total_cost = round(total_cost, 2)

# Output the total cost
print("Total cost of clothes is:", total_cost)


# ## Question four- taxable income

# In[15]:


def calculate_income_tax(income):
    if income<= 11000:
        tax= income * 0.10
    elif 11001 <= income <= 44725:
        tax= 1100 +(income - 11000) * 0.12
    elif 44726 <= income <= 95375:
        tax = 1100 + 4155 +(income -44725) *0.22
    elif 95376 <= income <= 182100:
        tax = 1100 + 4155+ 9618 + (income- 95375) *0.24
    elif 182101 <= income <= 231250:
        tax =1100 + 4155 +9618 +16906 +(income - 182100) *0.32
    elif 231251 <= income <= 578125:
        tax = 1100 +4155 + 9618 +16906+ 16537 + (income -231250) *0.34
    else:
        tax = 1100 + 4155 + 9618 + 16906 + 16537 + 114813 + (income - 578125) * 0.37
    return tax

# incomes list
taxable_incomes = [37250.00, 86400.00, 65750.00, 132325.00, 194800.00, 618525.00, 42824.00, 178270.00, 445250.00]

# Calculation and printing
for income in taxable_incomes:
    tax = calculate_income_tax(income)
    print(f"Taxable Income: ${income:.2f}, Income Tax: ${tax:.2f}")


#  ## QUESTION 5 POLYNOMIAL

# In[17]:


a = -10.0
b = 3.8
c = -2.5
d = 4.2

# define polynomial
def calculate_P(x):
    return a + b*x + c*x**2 + d*x**3

# Loop through odd integers from -10 to +20
for x in range(-9, 21, 2):
    P_x = calculate_P(x)
    print(f"x = {x}, P(x) = {P_x}")


# In[ ]:




