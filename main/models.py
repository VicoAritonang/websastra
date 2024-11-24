import uuid
from django.db import models

class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    gambar = models.URLField()
    mp3file = models.URLField(blank=True, null=True)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama
