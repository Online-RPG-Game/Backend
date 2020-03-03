from django.conf.urls import url
from . import api

urlpatterns = [
    url('welcome', api.welcome),
    url('init', api.initialize),
    url('get_rooms', api.get_rooms),
    url('move', api.move),
    url('say', api.say),
]
