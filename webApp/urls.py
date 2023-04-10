from django.urls import path,include
from.import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
]