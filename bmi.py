def bmi_calculator():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.2f}")
    if bmi<18.5:
        print ("You are under weight! Time to get some meat on your bones")
    if 15.5<= bmi<=24.9:
        print ("You are the right weight. Good job!")
    if 25<=bmi<=29.9:
        print("You are overweight. Time to lose weight")    
    if bmi>= 30:
        print("You are obese")
bmi_calculator()
