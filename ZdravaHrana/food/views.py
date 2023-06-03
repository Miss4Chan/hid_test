from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def outOfStock(request):
    if request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = Client.objects.get(user=request.user)
            product.save()
    
    context = Product.objects.filter(quantity=0,category__active=True)
    return render(request,"outOfStock.html",{"form":ProductForm, "products":context})