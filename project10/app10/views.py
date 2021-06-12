from django.shortcuts import render

def show(request):
    if request.method == "POST":
        username = request.POST.get("t1")
        password = request.POST.get("t2")
        type = request.POST.get("ty")

        if username == "Ravi" and type =="Admin" and password == "ravi1234@":
            return render(request, "index.html", {"message": "Admin"})
        elif username == "Ravi" and type == "Employee" and password == "kumar@123":
            return render(request, "index.html", {"message": "Employee"})
        elif username == "Ravi" and type == "Customer" and password == "ravikumar@123":
            return render(request, "index.html", {"message": "Customer"})

        else:
            return render(request, "index.html", {"message": "error"})


    if request.method == "GET":
        return render(request, "index.html")
