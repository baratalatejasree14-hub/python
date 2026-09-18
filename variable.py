#program 1:Display personal details using variables
#getting the input from user
name=input("enter your name")
age=int(input("enter your age"))
height=float(input("enter your height"))
#printing the values
print(name)
print(age)
print(height)

#program 2:personalized Greeting
name=input("enter your name")
print(F"Hello,{name}!")

#program 3:Add Two numbers read as strings
#taken the input as a string
a=input("enter first number")
b=input("enter second number")
#converting the string into integer
a=int(a)
b=int(b)
#Find the sum 
total=a+b
#print the result
print(total)

#program 4:Float to integer conversion
#float:numbers with decimal value 
#int:whole numbers without any decimal or fractional value
#reading a float value from the user 
n=float(input())
#print the float value
print(n)
#convert the float into integer:decimal point values will be removed
new =int(n)
#print the result
print(new)

#program 5:sum using arithmetic operator
#reading 2 integers from the user
a=int(input())
b=int(input())
#finding the sum and printing the result
print(a+b)

#program 6:area of a rectangle
#reading input from the user 
length=float(input())
breadth=float(input())
#calculating the area of a rectangle
area=length*breadth
#print the result
print(area)

#program 7:quotient and remainder
#user inputs 
a=int(input())
b=int(input())
#find the quotient
q=a/b
#find the remainder
r=a%b
#print the result
print(q)
print(r)

#program 8:power calculation
#reading user input
base=int(input())
exponent=int(input())
#calculate the power of and print the result
print(base**exponent)

#program 9:average of three numbers 
#taking 3 integer numbers from the user 
n1=int(input())
n2=int(input())
n3=int(input())
#find the total
total = n1+n2+n3
#find the average 
avg=total/3#division operator/-->always gives the result as a float.
#print the average
print(avg)

#program 10:greater than comparison
#read 2 integer numbers from user
a=int(input())
b=int(input())
#checker wether the 1st number is greater than the 2nd number
print(a>b)

#program 11:equality check
#check whether both the numbers are same or not 
#if the numbers are same-true
#if the numbers are different-false
#reading the input from the user
n1=int(input())
n2=int(input())
print(n1==n2)

#program 12:both numbers positive check
#if the number is greater than 0
#logical and -->if all the combining conditions are true,result is true
#reading the input from the user
n1=int(input())
n2=int(input())
print(n1>0 and n2>0)

#program 13:at least one even number
#even number:if the number is division by 2(without any remainder)
#logical or -->if any one of the combining condition is true,then the result is true.
#reading input from the user 
n1 = int(input())
n2 = int(input())
print(n1 %2 ==0 or n2%2==0)
#program 14:logicalnot on a condition
#logical not -->reverse the result 
#ture -->false
#false -->ture
#reading the input from the user 
num =int(input())
print(not(num>0))
#program 15:augmented assignment operations
#read a number from the user
a =int(input ())#20
a =a+5# a=20+5-->25
a =a*2# a=25*2-->50
a =a-3# a=50-3-->47
print(a)
#program 16:exchange values of two variables
#reading the input from user
a =int(input())
b =int(input())

#logicl 1 -using temp variable
temp = a
a = b
b = temp
print(a)
print(b)

#logic 2: without using temp(3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#logic 3:without using temp (3rd variable)
a = a^b  
b = a^b
a = a^b  
print(a)
print(b)

#logic 4: without using temp(3rd vaiable)
#promblem :it cannot handle 0
a = a*b 
b = a/b 
a = a/b
print(a)
print(b)

#logic 5: using python's special 
#simplest way
a,b = b,a
print(a)
print(b)

#program 17 : calculate simplest interest
#formula:(principle *rate*time)/100
#user inputs
principle = float (input ())#loan amount
rate =float(input())#rate of interest
time =float(input())#repayment time
#calculate interest
si=(principle*rate*time)/100
#print the result
print(si)

#program 18:Temperature conversion (celsius to fahrenheit)
#formula:F=(C*9/5)+32
#read the temperature in celsius
c =float(input())
#convert the celsius to fahrenheit
f=(c*9/5)+32
print(f)

#program 19:check divisibility by 3 and 5
n=int(input())
print(n%3==0 and n%5==0)

#program 20:sum of digits of a two-digit number
num=int(input())#num = 48
tens = num//10 #tens=48//10 = 4
units = num%10 #units = 48%10 = 8
total = tens+units #total = 4+8 = 12
print(total)


















