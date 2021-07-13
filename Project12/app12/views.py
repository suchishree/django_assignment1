from django.shortcuts import render
from app12.models import Registration

def showhomepage(request):
    return render(request, 'main.html')


def showregistrationpage(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Registration(name=name, contact=contact, location=location, email=email, password=password).save()

        return render(request, "register.html", {"message": "registration is done"})



def showloginpage(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        em = request.POST.get("email")
        pw = request.POST.get("password")
        try:
            stu_obj = Registration.objects.get(email=em, password=pw)
            return render(request, "welcome.html")
        except Registration.DoesNotExist:
            return render(request, "login.html", {"error_message": "invalid user"})



