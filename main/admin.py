from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('nama', 'gambar', 'keterangan')  # Kolom yang tampil di admin