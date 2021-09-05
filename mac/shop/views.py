from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    # params = {'no_of_slides' : noSlides, 'range' : range(1, noSlides), 'products' : products}

    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]

    allProds = []

    catprods = Product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    #Fetch the product using ID
    
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/productView.html', {'product':product[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')
