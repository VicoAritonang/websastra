from django.urls import path
from .views import show_json

app_name = 'main'


urlpatterns = [
    path('json/', show_json, name='show-json'),
]