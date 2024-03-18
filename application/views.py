from django.shortcuts import render
from store.models import Product
# Create your views here.

def index(request):

    # To bring all available products (items,objects...) in model of Product
    products = Product.objects.all().filter(is_available= True)
    # dictionary to pass the data in template
    context = {
        'products':products,
    }

    return render(request , 'home.html' , context)