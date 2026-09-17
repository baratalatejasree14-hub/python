#dictionaries in python
#dictionary is a collection of key value pairs that is unordered and mutable 
student ={
"name":"bhargavi",
"age":00,
"course":"python"
}

print(student)

#access elements in dic
print(student["name"])
print(student["age"])
print(student["course"])

#change values in dictionary
student["age"]=11
print(student["age"])

#add a new data to a dictionary
student["city"] ="vijayawada"
print(student)

#remove data
student.pop("city")
print(student)

#get ()returns the values of the specified key
print(student.get("name"))

#update ()updates the values of the specified key
student.update({"age":22})
print(student)

#popitem() removes the last inserted keyvalue pair
student={
"name":"bhargavi",
"age":21,
"course":"python"
}

student.popitem()

print(student)
student={
"name":"Bhargavi"
}

student.setdefault("age",21)
print(student)

student.clear()
print(student)

student ={
"name":"Bhargavi",
"age":21
}
new_student=student.copy()
print(new_student)

