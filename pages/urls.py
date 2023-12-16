from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('Diseases',views.Diseases, name='Diseases'),
    path('Fdisease',views.Fdisease, name='Fdisease'),
    path('healthylife',views.healthylife, name='healthylife'),
    #path('Appoint',views.Appoint, name='Appoint'),
    path('Contacts',views.Contacts, name='Contacts'),
    path('hindiDiseases',views.hindiDiseases, name='hindiDiseases'),
    path('hindiFdisease',views.hindiFdisease, name='hindiFdisease'),
    path('hindihealthylife',views.hindihealthylife, name='hindihealthylife'),

]