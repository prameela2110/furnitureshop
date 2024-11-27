from django.urls import path
from  WebApp import views

urlpatterns =[
     path('home/',views.home_page,name="home"),
     path('products_page/',views.products_page,name="products_page"),
     path('about_page/',views.about_page,name="about_page"),
     path('contact_page/',views.contact_page,name="contact_page"),
     path('save_contact/',views.save_contact,name="save_contact"),
     path('filtered_product/<cat_name>/',views.filtered_product,name="filtered_product"),
     path('single_product/<int:prod_id>/',views.single_product,name="single_product"),
     path('sign_up/',views.sign_up,name="sign_up"),
     path('',views.sign_in,name="sign_in"),
     path('save_signup/',views.save_signup,name="save_signup"),
     path('user_login/',views.user_login,name="user_login"),
     path('save_cart/',views.save_cart,name="save_cart"),
     path('cart_page/',views.cart_page,name="cart_page"),
     path('delete_cart/<int:cart_id>/',views.delete_cart,name="delete_cart"),
     path('check_out/',views.check_out,name="check_out"),
     path('save_checkout/',views.save_checkout,name="save_checkout"),
     path('payment_page/',views.payment_page,name="payment_page"),
     path('service_page/',views.service_page,name="service_page"),
     path('blog_page/',views.blog_page,name="blog_page"),




]