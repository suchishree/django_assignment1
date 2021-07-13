from django.shortcuts import render, redirect

def showmainpage(request):
    return render(request, 'slide.html')
def showregister(request):
    return render(request, 'register.html')

def showhome(request):
    return render(request,'slide.html')
