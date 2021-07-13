Engineering_batch = {468 : "CSE",  572 : "ECE", 621 : "EEE", 482 : "Civil"}
Engineering_batch[684] = "IT"
print(Engineering_batch)
for i,j in Engineering_batch.items():
           
    print(i,end="\t")
    for k in j:
        print(k,end="")
    print()    
