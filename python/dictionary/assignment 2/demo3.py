#Read Dept name dynamically, if it is available then display Dept id otherwise display msg “Dept is Not Availabl1e”
Engineering_batch = {468 : "CSE",  572 : "ECE", 621 : "EEE", 482 : "Civil"}
Engineering_batch[684] = "IT"
dept = input("Enter dept name:")
for i,j in Engineering_batch.items():
    if dept in j:
        print("idno for above dept is:",i)
        break
else:
    print("Given dept is not aval")  