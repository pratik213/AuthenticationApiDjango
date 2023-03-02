from django.urls import path,include
from . import views

urlpatterns = [
    path('api/register/customer',views.CustomerRegisterView.as_view(),name='register_customer'),
    path('api/register/seller',views.SellerRegisterView.as_view(),name='register_seller'),
    path('api/login/customer',views.CustomerLoginView.as_view(),name='LoginCustomer'),
    path('api/login/seller',views.SellerLoginView.as_view(),name='LoginSeller'),
    path('api/customer/profile',views.UserProfileView.as_view(),name='CustomerProfile'),

]
