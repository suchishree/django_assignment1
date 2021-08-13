from django.shortcuts import render,redirect
from app1.models import productinfoModel

# Create your views here.
def showindex(request):


    return render(request, "main.html")

def addproduct(request):
    if request.method == "POST":
        name = request.POST.get("product_name")
        price = request.POST.get("product_price")
        description = request.POST.get("product_description")
        image = request.FILES["product_image"]

        productinfoModel(name=name, price=price, description=description, image=image).save()
        return redirect('add_product')
    else:
        return render(request, 'product.html')

def viewproduct(request):
    if request.COOKIES.get("csrftoken"):
        total_cookies = len(request.COOKIES) - 1
    else:
        total_cookies = len(request.COOKIES)

    return render(request, "view_product.html", {"product": productinfoModel.objects.all(),"cookie":total_cookies})

def savecookie(request):
    p_no = request.GET.get("pno")
    p_name = request.GET.get("pname")

    response =redirect('view_product')
    response.set_cookie(p_no,p_name)

    return response

