import datetime
now = datetime.datetime.now()
fname = input("Enter your first name : ")
lname = input("Enter your last name : ")
print("Hello "+ fname +" "+ lname)
print("Current date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))