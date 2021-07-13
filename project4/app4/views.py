from django.shortcuts import render

def show(request):
    employee_info = {"idno":101,"name":"ravi","salary":185000.00}
    return render(request,"demo1.html",employee_info)
