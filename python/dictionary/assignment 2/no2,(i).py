d1 =  {1101 : "BJA", 1421 : "AJ", 7712 : "NIM"}
idno = int(input("Enter id no: "))
clg_name = input("Enter clg name: ")
for i,j in d1.items():
    if idno in d1 and clg_name in j:
        d1[idno]=clg_name
        print(d1)
        break
else:
    print("n")   