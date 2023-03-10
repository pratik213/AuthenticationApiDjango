from django.urls import path,include
from . import views

urlpatterns = [
    path('details',views.Product.as_view(),name='product_details'),
    path('update',views.Product.as_view(),name='product_update'),
    path('create',views.Product.as_view(),name='product_create'),
   

]
