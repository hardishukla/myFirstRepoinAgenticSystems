employee = (101, "Alice", "IT")
roles = {"editor", "viewer", "admin"}

print("Employee Information")
print("ID:", employee[0])
print("Name:", employee[1])
print("Department:", employee[2])

if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")
