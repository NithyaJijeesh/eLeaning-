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

    path('python_dev',views.python_dev,name="python_dev"),
    # path('react_dev',views.react_dev,name="react_dev"),
    # path('rest_api',views.rest_api,name="rest_api"),
    # path('digital_marketing',views.digital_marketing,name="digital_marketing"),
    # path('frontend_dev',views.frontend_dev,name="frontend_dev"),
    path('course_select/<pk>',views.course_select,name="course_select"),

]