from django.shortcuts import render
from django.shortcuts import redirect
from student.models import RegistrationModel
from common.utils import sendTextMessage
from random import randint

def showCommonPage(request):
    return render(request, "common/index.html")

def studentPage(request):
    return render(request, "common/student.html")
def studentRegistration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact_number")
        email = request.POST.get("email")
        password = request.POST.get("password")

        otp = randint(100000, 999999)

        message = '''Thanks for registration with sathya,
        To finish the Registration use the given OTP
        Your OTP :'''+str(otp)

        if sendTextMessage(message, contact):
            RegistrationModel(Name=name, contact=contact,email=email,password=password,otp=otp).save()
        else:
            pass
        return redirect('student_otp')
    else:
        studentPage()


def openStudentOtp(request):
    return render(request, "common/otp.html")
