from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('details/',views.details,name='details'),
    path('form/',views.form,name='form'),
    path('form/add/',views.addition,name='addition')
    

]