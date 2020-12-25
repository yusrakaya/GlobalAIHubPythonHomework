
fname=input("Please enter the first name:")
lname=input("Please enter the last name:")
age=float(input("Please enter the age:"))
bday=int(input("Please enter the date of birth(just year):"))
#The user inputs a name, last name, age and birth year then Python stores those values in variables fname,lname,age and bday.
print(f"User's information:\n{fname}\n{lname}\n{age}\n{bday}")
UserIdentification=[]
UserIdentification.append(fname)# 'fname' is appended to the UserIdentification list
UserIdentification.append(lname)# 'lname' is appended to the UserIdentification list
UserIdentification.append(age)# 'age' is appended to the UserIdentification list
UserIdentification.append(bday)# 'bday' is appended to the UserIdentification list
if age < 18:
    print("You can't go out because it's dangerous")
else:
    print("You can go out to the street")