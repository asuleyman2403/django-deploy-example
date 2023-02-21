from django.urls import path
from online_shop import views

urlpatterns = [
    path('', views.home_page),
    path('categories/<int:pk>', views.category_page),
    path('about', views.about_page),
    path('online-shop/categories', views.categories_handler),
    path('online-shop/categories/<int:pk>', views.category_handler),
    path('online-shop/categories/<int:pk>/products', views.category_products_handler),
    path('online-shop/products', views.products_handler),
    path('online-shop/products/<int:pk>', views.product_handler)
]
