from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('',views.index, name='index'),
    path('events/', views.event_listing, name='events'),
    path('events/detail/<int:pk>', views.eventrun_listing, name='detail'),
    path('events/neweventrun/', views.eventrun_add, name='new_eventrun')
]
