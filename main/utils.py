import csv
from .models import Card

def read_csv_to_card(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Card.objects.create(
                nama=row['nama'],
                gambar=row['gambar'],
                # mp3file=row['mp3file'],
                keterangan=row['keterangan']
            )
