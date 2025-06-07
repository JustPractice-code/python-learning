# #even or odd
# num = int(input("Enter any number : "))
# if num%2==0:
#     print(num," is even")
# else:
#     print(num," is odd")

#leap year or not
# year = int(input("Enter year : "))
# if year%4==0 and (year%100!=0 or year%400==0):
#     print(year, " is a leap year")
# else:
#     print(year, " is not a leap year")

#login simulator
username = input("Enter username : ")
password = input("Enter password : ")
if username!="admin" and password!="1234":
    print("Wrong credentials")
else:
    print("Login successful")