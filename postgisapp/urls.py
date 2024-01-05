from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('addLocation/',views.addLocation),
    path('viewLocation/<int:locationId>/',views.viewLocation),
    path('allLocation/',views.allLocation)
]