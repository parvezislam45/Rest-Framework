from .models import Item

def menu_links(request):
    links = Item.objects.all()
    return dict(links=links)