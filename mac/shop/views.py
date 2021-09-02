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
    return HttpResponse("We are contact")


def tracker(request):
    return HttpResponse("We are tracker")


def search(request):
    return HttpResponse("We are search")


def productView(request):
    return HttpResponse("We are product view")


def checkout(request):
    return HttpResponse("We are checkoutt")
