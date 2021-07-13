from django.shortcuts import render, redirect
from app14.models import ProductModel

def openmainpage(request):
    if request.method == "POST":
        name = request.POST.get("product_name")
        price = request.POST.get("product_price")
        photo = request.FILES["product_photo"]

        ProductModel(name=name, price=price, photo=photo).save()
        return redirect('main')
    else:
        return render(request, 'main.html')

