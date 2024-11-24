
from django.urls import path
from .views import show_card

app_name = 'showCard'

urlpatterns = [
    path('<uuid:card_id>/', show_card, name='show_card'),
]