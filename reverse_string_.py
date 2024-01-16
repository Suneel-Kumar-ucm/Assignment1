##A python program for inputing a string as a list of characters from console, delete at least 2 characters, reverse the
##resultant string and print it.

str=input('Enter string:  ')# enter a string
str=str[:-2:1]# deleting atleast 2 charaters
str=str[::-1]# reversing the result string
print(f'The reversed string after removal of 2 characters:  {str}')#displaying the final reversed string
