print('Hello, world')

 ## 1. State differences between Python 2 and Python 3 version.

 # Python2                                           Python3
 #Python 2’s print statement has been replaced by the print() function
 # print 'Hello, World!'                     print('Hello, World!')
 # Integer division
# This change is particularly dangerous if you are porting code, or if you are executing Python 3 code in Python 2,
# since the change in integer-division behavior can often go unnoticed (it doesn’t raise a SyntaxError).

# 3 / 2 = 1                             3 / 2 = 1.5
# the input() function was fixed in Python 3 so that it always stores the user inputs as str objects.
# In order to avoid the dangerous behavior in Python 2 to read in other types than strings, we have to use raw_input() instead.

 ## 2. Write a python program for the following:–
    ## Take the user first name and last name and print it in reversed form

firstname = 'chandrasekhar'
lastname = 'pentakota'
fullname = firstname + ' ' +lastname
str = ""
for i in fullname:
    str = i + str
print(str)

 # Take two numbers from user and perform arithmetic operations on them.

x,y = 3 , 5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)


##3.  Write a program that accepts a sentence and prints the number of letters and digits in Sentence.

teststr = 'Python CS 5590'
import re
teststr1 = re.sub('[\s+]','',teststr)
nletters = 0
ndidgits = 0

for i in teststr1:
    if(i.isdigit()):
        ndidgits += 1
    else:
        nletters += 1

print("Letters: ",nletters)
print("Digits: ",ndidgits)



