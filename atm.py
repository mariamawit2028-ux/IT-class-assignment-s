
balance = 1000.00

def calculate_withdrawal(withdrawal):
    if withdrawal > balance:
        print ("Insufficient funds!")
    if withdrawal== balance:
        print("Balance is going to be zero")    
    if withdrawal < balance:
        print("Withdrawal successfull!")
        new_balance = balance - withdrawal
        print(f"New balance: ${new_balance:.2f}")
print( "balance=1000.00")
amount = float(input("Enter the amount that you want to withdraw: "))    
calculate_withdrawal(amount)        
