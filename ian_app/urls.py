from django.urls import path
from ian_app import views

urlpatterns=[

    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('contact/',views.contact,name='my_contact'),

    path('blog/',views.blog,name='my_blog'),

    path('services/',views.services,name='my_services'),

    path('ian',views.ian,name='my_ian'),

]