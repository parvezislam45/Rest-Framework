from django.urls import path
from .import views

urlpatterns = [
    path('',views.items,name='item'),
    path('category/<slug:category_slug>/',views.items,name ='products_by_category'),
     path('api/add_product/', views.add_product_api, name='add_product_api'),
     path('api/products/update/<int:product_id>/', views.update_product_api, name='update_product_api'),
     path('api/products/delete/<int:product_id>/', views.delete_product_api, name='delete_product_api'),
]

