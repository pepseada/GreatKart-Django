from .models import Category

# To brings category and put it in menu 
def menu_links(request):
    links = Category.objects.all()
    return dict(links= links)