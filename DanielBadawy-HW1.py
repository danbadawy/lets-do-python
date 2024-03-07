#!/usr/bin/env python
# coding: utf-8

# ## Question 1: water temp 

# In[2]:


#user inputs water weight
weight= float(input("Enter amount of water in Kg: "))

#user gives temp
initial_temp = float(input("Enter initial temperature: "))

#user gives final temp
final_temp = float(input("Enter final temperature: "))

#enter formula
energy = weight*(final_temp-initial_temp)*4184

#printing the final output
print("joules needed to heat water is:", energy)



# ## Question 2: BMI 

# In[4]:


#ask users for height and weight 
height = float(input("Enter height in inches: "))
weight = float(input("Enter weight in pounds: "))
#enter BMI calculation 
BMI = (weight * 703) / (height * height)

print("BMI is {:.2f}".format(BMI))
#classify and display users BMI based on inputs
if BMI < 18.5:
    print("Under weight")
elif BMI < 25:
    print("Normal weight")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")


# ## Question 3: Clothing tax and price

# In[13]:


#clothing item price
price = float(input("Please enter clothing item price: "))
    #Check price is less than 15
if(price < 15):
        #Sales tax is 1.7% when cost is less than 15
        salesTax = (price * 1.7)/100
        #final price add tax to regular price
        FinalPrice = price + salesTax
        #Format the price in currency format. Upto 2 decimals
        formattedFinalPrice = '${:,.2f}'.format(FinalPrice)
else:
        #Sales tax = 7.65% when cost > 15
        salesTax = (price * 7.65)/100
        #final price is Price + Sales Tax
        FinalPrice = price + salesTax
        #Format the price as currency 
        formattedFinalPrice = '${:,.2f}'.format(FinalPrice)
        
    #Display the total price to user
print("Total price of purchased clothing : " ,formattedFinalPrice)


# ## Question 4: President's scholarship

# In[14]:


# take year input
year = input("Enter your year as Senior or Junior: ")  
# take gpa input
gpa = float(input("Enter your gpa: ")) 

# check the condition for Senior and gpa >=3.3
if(year=="Senior" and gpa>=3.3):
    print("Eligible for a scholarship")
# check the condition for Junior and gpa >= 3.6
elif(year=="Junior" and gpa>=3.6):
    print("Eligible for a scholarship")
else:
    print("Not eligible for scholarship")


# ## Question 5: Road trip

# In[19]:


# Get input from the user
while True:
       try:
           miles = float(input("Enter the miles driven on the trip: "))
           speed = float(input("Enter the speed of the car (mph): "))
           if miles <= 0 or speed <= 0:
               print("Error: Miles and speed must be positive numbers.")
           else:
               break
       except ValueError:
           print("Error: Please enter valid numerical values.")

   # Calculate time
time_hours = miles / speed
time_minutes = (time_hours - int(time_hours)) * 60
time_hours = int(time_hours)
time_minutes = int(round(time_minutes))

# Display the result
print(f"Estimated time to complete the trip: {time_hours} hours and {time_minutes} minutes.")


# In[ ]:




