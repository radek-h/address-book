from django.urls import path
from . import views

app_name = "address_book"

urlpatterns = [
    path('', views.contact_list, name="contact_list"), # GET
    path('add/', views.contact_add, name="contact_add"), # POST
    path('search/', views.contact_search, name="contact_search"), # GET
    path('delete/<int:pk>/',  views.contact_detail, name="contact_delete"), # DELETE
    path('edit/<int:pk>/',  views.contact_detail, name="contact_edit"), # POST
    path('phone_add/<int:pk>/', views.phone_add, name="phone_add"), # POST
    path('email_add/<int:pk>/', views.email_add, name="email_add"), # POST

]

