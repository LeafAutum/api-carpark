from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from rest_framework import routers
from .views import Carparkset,Slotsallset

# router = routers.DefaultRouter()
# router.register('Carpark', Carparkset)
# router.register('Slotsall',Slotsallset)
# #router.register(r'^(?P<pk>\d+)/$', Carparkset)

urlpatterns = [
    #path('' ,include(router.urls)),

    path(r'^(?P<pk>\d+)/$', Carparkset, name='sloturl'),

    ]
