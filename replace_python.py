##a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’

string=input("Enter the sentance:\n")#for accepting a sentance
string=string.lower()#for ignoring upper case and converting upper case to lower case
string=string.replace("python","pythons")#replacing the python with pythons by using replace() function
print(f'The sentance after replacing\n{string} \n')#displaying the replaced sentence
