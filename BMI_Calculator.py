# Get results in Integer
# Add floats for weight and height
height = input("enter your height in m: ") 
weight = input("enter your weight in kg: ")
BMI = (float(weight)/(float(height)*float(height)))
print (int(BMI))