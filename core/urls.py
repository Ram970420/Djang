
from django.urls import path
from . import views

urlpatterns=[
    path('app/sample/', views.sample_get_view, name='sample_view'),
    path('app1/sample/', views.sample1, name='sample_view'),
]