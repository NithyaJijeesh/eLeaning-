from django.urls import path,include
from.import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('placement',views.placement,name="placement"),
    path('subscribe',views.subscribe,name="subscribe"),
    path('contactuss',views.contactuss,name="contactuss"),
]