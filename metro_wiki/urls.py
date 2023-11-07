from django.urls import path
from .views import *

urlpatterns = [
    path('city/', Cities.as_view(), name='cities'),
    path('line/', Lines.as_view(), name='lines'),
    path('station/', Stations.as_view(), name='stations'),

    path('city/<slug:city_slug>/', ShowCity.as_view(), name='city'),
    path('line/<slug:line_slug>/', ShowLine.as_view(), name='line'),
    path('station/<slug:station_slug>/', ShowStation.as_view(), name='station'),

    path('city/special/add/', AddCity.as_view(), name='add_city'),
    path('line/special/add/', AddLine.as_view(), name='add_line'),
    path('station/special/add/', AddStation.as_view(), name='add_station'),
    path('train/special/add/', AddLine.as_view(), name='add_train'),
    path('depot/special/add/', AddStation.as_view(), name='add_depot'),

    path('city/<slug:city_slug>/update/', UpdateCity.as_view(), name='update_city'),
    path('line/<slug:line_slug>/update/', UpdateLine.as_view(), name='update_line'),
    path('station/<slug:station_slug>/update/', UpdateStation.as_view(), name='update_station'),
    path('train/<slug:line_slug>/update/', UpdateLine.as_view(), name='update_train'),
    path('depot/<slug:station_slug>/update/', UpdateStation.as_view(), name='update_depot'),
]
