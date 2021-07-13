Engineering_batch = {468 : "CSE",  572 : "ECE", 621 : "EEE", 482 : "Civil"}
Engineering_batch[684] = "IT"
idno = int(input("Enter idno:"))
for i,j in Engineering_batch.items():
    if idno ==i :
        print("Dept for above idno is:",j)
        break
else:
    print("Given idno is not aval")    
