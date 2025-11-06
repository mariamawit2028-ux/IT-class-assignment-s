number = int(input("Provide any number, please?"))
    
def check_divisibility(number):
    if number % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number isn't divisible by 5.")
    
check_divisibility(number)
