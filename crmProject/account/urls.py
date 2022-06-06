from django.urls import path
from account import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('product/',views.product, name='product'),
    path('order/',views.order, name='order'),
    path('all_customers/',views.all_customers, name='all_customers'),
    path('customer/<pk>',views.customer, name='customer'),

    path('add_product/',views.add_product, name='add_product'),
    path('edit_product/<pk>',views.edit_product, name='edit_product'),
    path('delete_product/<pk>',views.delete_product, name='delete_product'),

    path('register',views.register_view, name='register'),
    path('login',views.login_view, name='login'),
    path('logout',views.logout_view, name='logout')
]
