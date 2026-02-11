def check(a):
    if a % 2 == 0 :
        return "Number is Even"
    else:
        return "Number is odd"
    
a = int(input("enter first number : "))
print(check(a))