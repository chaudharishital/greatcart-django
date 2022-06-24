from django.shortcuts import render
from store.models import Product


def home(request):
    products=Product.objects.all()
    print("products are ",products)
    context={
    'products':products,
    }
    return render(request,'home.html',context)
