from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    # use slug to enter in page in page (shoes,jacket,... from store)
    path('<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name= 'product_detail'),
]

