from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    
    # To show this list in admin page
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'date_joined', 'last_login', 'is_active')

    list_display_links = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  # To make password read only can not change it

admin.site.register(Account, AccountAdmin)

