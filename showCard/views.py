from django.shortcuts import render, get_object_or_404
from main.models import Card

# Create your views here.
def show_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, 'show_card.html', {'card': card})
