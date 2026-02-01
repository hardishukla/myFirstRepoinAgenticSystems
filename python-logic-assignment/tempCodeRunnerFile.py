#Secure Transaction Validator
"""Balance: 5000  
Withdrawal: 3000  
Verified: True
"""
balance=int(input("Balance: "))
withdraw=int(input("Withdrwal:"))
verify=bool(input("Verified:").capitalize)

if withdraw<=balance and verify== True:
    print("Withdrawal successful")
else:
    print("Withdrawal Denied")
    