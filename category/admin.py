from django.contrib import admin
from .models import Category ,CategoryAdmin

# Register your models here.

# TO write slug field automatic by cate_name
# this instead of use in models.py page                    This is the same 

# class CategoryAdmin(admin.ModelAdmin):                  
    # prepopulated_fields = {'slug': ('cate_name',)}
    # list_display = ('cate_name', 'slug')


admin.site.register(Category, CategoryAdmin)