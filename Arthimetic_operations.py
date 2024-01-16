#A python to take two numbers from user and performing 4 arithmetic operations.

a1=int(input("Enter 1st integer:  "))#To take first number
a2=int(input("Enter 2nd integer:  "))#To take second number
adds=a1+a2#addition
multi=a1*a2#multiplication
subs=a1-a2#substraction
divide=a1/a2#division
#Displaying the values
print("The addition of 2 values is {}".format(adds))
print("The multiplication of 2 values is {}". format(multi))
print("The substraction of 2 values is {}".format(subs))
print("The division of 2 values is {}".format(divide))