
#comparsion operators
a = 10
b = 20


print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age eligibility checker
age = int(input("enter your age:"))

print("eligible: ",age>=18)


#pass or fail checker
marks = int(input("Enter marks"))
print("passed:",marks >= 40)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username")
password = input("Enter password")

print(username == correct_username)
print(password == correct_password)

#logical operators 
age=25
citizen=True
print(age >= 18 and citizen == True)
has_card = False
has_cash =  True
print(has_card or has_cash) 

#not
is_logged_in = True
print(not is_logged_in)


#atm eligibility checker
balance = 10000
withdraw = 5000
print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibility checker
marks = float(input("Enter marks:"))
attendence = float(input("Enter attendence:"))
eligible=marks >=85 and attendence >=75

print("scholarship Eligible")

#bitwise operators
a=5
b=3
print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)
a=8
b=2
print(a>>b)
print(a<<b)
a=12
b=6
print(a<<b)

#electricity bill calculator
units = int(input("Enter electricity units:"))
rate=6
bill=units*rate
print("Electricity bill:",bill)

#travel expense calculator
travel=float(input("Travel expense:"))
food=float(input("Food expense:"))
hotel=float(input("Hotel expense:"))

total=travel+food+hotel

print("Total Expense:",total)

#list in python
#list is an ordered and changeable collection that can store
marks=[80,90,75,85]
print(marks)

#accessing elements in a list
marks=[80,90,75,85]

print(marks[0])
print(marks[1])
print(marks[3])

#change elements in a list
marks=[80,90,75]

marks[1]=95

print(marks)

#add elements to a list
marks=[80,90,75]

marks.append(85)

print (marks)
#remove elements from a list
marks=[80,90,75]

marks.remove(90)
print(marks)

#insert

numbers=[10,20,30]
numbers.insert(1,15)

print(numbers)

#extend
a=[1,2,3]
b=[4,5,6]

a.extend(b)

print(a)
#clear
numbers=[10,20,30]
numbers.clear()
print(numbers)
#index
numbers=[10,20,30,40]
print(numbers.index(20))
#count
print(numbers.count(20))

#sort
numbers=[40,10,30,20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#reverse
numbers=[10,20,30,40]
numbers.reverse()
print(numbers)

#copy method
a=[1,2,3]
b=a.copy()
print(b)

numbers=[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#tuples in python
#tuple is a collection of multiple values that is cannot be changed after creation
student=("Bhargavi",98,"python")
print(student[0])

#access values in a tuple
student=("Bhargavi",21,85.5)
print(student[0])
print(student[1])
print(student[2])

#tuples are immutable,meaning they cannot be changed after creation
numbers=(10,20,20,30,20)
print(numbers.count(20))

numbers=(10,20,30,40)
print(numbers.index(30))

numbers=(10,20,30,40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))




