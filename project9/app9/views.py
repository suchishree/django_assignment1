from django.shortcuts import render

def show(request):
    if request.method == "POST":
        username = request.POST.get("t1")
        password = request.POST.get("t2")
        if username == "suchishree" and password == "badjena":
            return render(request,"demo.html",{"message":"valid"})
        else:
            return render(request,"demo.html",{"message":"invalid"})

    if request.method == "GET":
        return render(request, "demo.html")

