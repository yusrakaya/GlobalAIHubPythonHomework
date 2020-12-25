List='value1','value2','value3','value4','value5'
value1=input("Please enter a value:") #Gets needed input
print(f"First value is {value1}") #The {value1} means it puts the variable name there
print("Entered first value:{}".format(type(value1)))
value2=int(input("Please enter a value:"))
print(f"Second value is {value2}")
print("Entered second value:{}".format(type(value2)))
value3=float(input("Please enter a value:"))
print(f"Third value is {value3}")
print("Entered third value:{}".format(type(value3)))
value4=str(input("Please enter a value:"))
print(f"Fourth value is {value4}")
print("Entered forth value:{}".format(type(value4)))
value5=bool(input("Please enter a value:"))
print(f"Fifth value is {value5}")
print("Entered fifth value:{}".format(type(value5)))
