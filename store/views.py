from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request, category_slug= None):
    categories = None
    products =None

    if category_slug != None:
        # Category is the model in category app to import slug from models
        categories = get_object_or_404(Category, slug=category_slug)
        # To appear a product only filter by category
        products =Product.objects.filter(category=categories, is_available= True)
        product_count = products.count()
        # if do not category_slug appear all products
    else:
        products        = Product.objects.all().filter()
        product_count  = products.count()

    context = {
        'products': products ,
        'product_count':product_count ,
    }
    return render(request,'store/store.html',context)

def product_detail(request, category_slug, product_slug):

    # use double_ (__) between category__slug because this is ForeignKey field $$$ link between category and slug
    # single_product use to bring and appear data to html page
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug = product_slug)
    except Exception as e:
        e

    context ={
        'single_product':single_product
    }

    return render(request, 'store/product_detail.html', context)