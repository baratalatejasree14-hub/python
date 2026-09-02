a=10
b=3

print("Addition",a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Floor division",a//b)
print("Remainder",a%b)
print("power",a**b)



#simple calculator
a=int(input("enter first number"))
b=int(input("enter second number"))

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)

#student marks calculator 
name=input("Enter student name:")

m1=int(input("Enter python marks:"))
m2=int(input("Enter java marks:"))
m3=int(input("Enter SQL marks:"))

total=m1+m2+m3
average=total/3

print("\n----- student Report -----")
print("Name:",name)
print("Total:",total)
print("Average:",average)

#shopping bill calculator
price1=float(input("Enter product 1 price:"))
price2=float(input("Enter product 2 price:"))
price3=float(input("Enter product 3 price:"))

total=price1+price2+price3

discount=total*0.10
final_amount=total-discount
print("total",total)
print("discount",discount)
print("final amount:",final_amount)

#salary calculator
basic=float(input("Enter basic salary:"))

hra =basic*0.20
da=basic*0.10

gross_salary=basic+hra+da

print("Basic salary",basic)
print("Hra",hra)
print("Da",da)
print("gross salary",gross_salary)



