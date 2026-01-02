hight = float(input("enter your hight in cm: "))
weight = float(input("enter your weight in kg: "))
BMI = weight/(hight/100)**2
print("your BMI is " , BMI)
if BMI <= 18.4:
    print("u are underweight")
elif BMI<=24.9:
    print ("u are healthy")
elif BMI<=29.9:
    print("u are overweight")
else:
    print("u are obese")