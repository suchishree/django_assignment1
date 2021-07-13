from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    return render(request, "demo.html")


def registeruser(request):

    f_name = request.POST.get("t1")
    l_name = request.POST.get("t2")

    full_name = f_name+" "+l_name

    return HttpResponse(full_name)



