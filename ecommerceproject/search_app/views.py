from django.shortcuts import render
from ecommerceapp.models import Product
from  django.db.models import Q

# Create your views here.
def SearchResult(request):
    products:None
    query:None
    if 'q'in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(q(name__contains=query)| q(descrptn__contains=query))
    return render(request,'search.html',{'query':query,'products':products})