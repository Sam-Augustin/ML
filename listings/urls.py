from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='listings'),
    path('listing',views.listing, name='listing'),
    path('register',views.register, name='register'),
    path('logout',views.register, name='logout'),
    path('search',views.search, name='search'),
    path('prediction',views.prediction, name='prediction'),
    
]