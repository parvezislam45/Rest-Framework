from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('api/',include('api.urls')),
    path('category/',include('category.urls')),
    path('product/',include('product.urls')),
    path('account/',include('account.urls')),
   
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
