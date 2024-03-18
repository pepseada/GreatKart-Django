from django.db import models
from django.contrib import admin
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    cate_name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length = 250 , blank = True )
    cate_img = models.ImageField(upload_to='category/img/%y/%m/%d')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category' , args=[self.slug])

    def __str__(self):
        return self.cate_name
    
# TO write slug field automatic by cate_name
class CategoryAdmin(admin.ModelAdmin):                  
    prepopulated_fields = {'slug': ('cate_name',)}
    list_display = ('cate_name', 'slug')

    

