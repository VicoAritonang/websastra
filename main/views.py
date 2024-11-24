from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Card
from django.http import JsonResponse

def show_json(request):
    cards = Card.objects.values()
    return JsonResponse(list(cards), safe=False)
