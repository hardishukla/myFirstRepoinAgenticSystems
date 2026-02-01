#Age: 20  
#Has ID: True
age=int(input("Age: "))
id=bool(input("Has ID:").capitalize())
if age>18 and id == True:
    print("Entry allowed")
else:
    print("NOT ALLOWED")