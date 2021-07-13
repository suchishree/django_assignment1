student = {"name":"rosy","idno":101,"marks":435}
d = student.items()
print(d)
a = student.keys()
print(a)
print(len(student))
for x in student:
    print(x)
student.clear()
print(student)    
student = {"name":"rosy","idno":101,"marks":435}
print(student.get("name"))
