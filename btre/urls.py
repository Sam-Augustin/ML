
from Appointments.models import Appoint
from django.contrib import admin
from django.urls import path,include
from Appointments.views import appoint,adetails

urlpatterns = [
    path('',include('pages.urls')),
    path('listings/',include('listings.urls')),
    path('Appoint', appoint,name='Appoint'),
    path('admin/', admin.site.urls),
    path('adetails',adetails,name='adetials'),
]
