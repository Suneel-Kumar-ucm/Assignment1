#Use the if statement conditions to write a program to print the letter grade based on an input class score. Use
#the grading scheme we are using in this class.

perc=float(input("Enter your percentage :"))#for accepting the float value
#To calculate the grade based on percentage and displaying the grades...
if perc>=90 and perc<=100:
    print("Your grade is A")
elif perc>=80 and perc<90:
    print("Your grade is B")
elif perc>=70 and perc<80:
    print("Your grade is C")
elif perc>=60 and perc<70:
    print("Your grade is D")
elif perc>=0 and perc<60:
    print("Your grade is F")