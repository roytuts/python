# asking for input from the users  
the_height = float(input("Enter the height in cm: "))  
the_weight = float(input("Enter the weight in kg: "))  
# defining a function for BMI  
the_BMI = the_weight / (the_height/100)**2  
# printing the BMI  
print("Your Body Mass Index is", the_BMI)  
# using the if-elif-else conditions  
if the_BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif the_BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif the_BMI <= 29.9:  
    the_print("Eee! You are over weight.")  
else:  
    print("Seesh! You are obese.")  
