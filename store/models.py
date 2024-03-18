from django.urls import reverse
from django.db import models 
from category.models import Category
from django.contrib import admin
# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.CharField(max_length=250, blank=True)
    price           = models.IntegerField()
    stock           = models.IntegerField()
    old_price       = models.IntegerField()
    images          = models.ImageField(upload_to='products/img/%y/%m/%d')
    created_date    = models.DateTimeField(auto_now_add=True)
    modefied_date   = models.DateTimeField(auto_now=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available    = models.BooleanField(default= True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modefied_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

