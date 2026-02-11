dic = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Sushma": "9988776655"
}
print(dic)
user_name= input("enter user name: ").capitalize()
if user_name in dic:
    print(dic[user_name])
else:
    print("Contact not found")