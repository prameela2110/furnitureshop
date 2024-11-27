from django.urls import path
from ShopApp import views

urlpatterns = [
    path('furniture_page/',views.furniture_page,name="furniture_page"),
    path('add_categories/',views.add_categories,name="add_categories"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:cat_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:cat_id>/',views.update_category,name="update_category"),
    path('delete_student/<int:cat_id>/',views.delete_student,name="delete_student"),
    path('add_product/',views.add_product,name="add_product"),
    path('save_product/',views.save_product,name="save_product"),
    path('display_products/',views.display_products,name="display_products"),
    path('edit_products/<int:prod_id>/',views.edit_products,name="edit_products"),
    path('update_products/<int:prod_id>/',views.update_products,name="update_products"),
    path('delete_products/<int:prod_id>/',views.delete_products,name="delete_products"),
    path('login_page/',views.login_page,name="login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_details/',views.contact_details,name="contact_details"),
    path('delete_contact/<int:d_id>/',views.delete_contact,name="delete_contact"),

]