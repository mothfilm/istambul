#!/usr/bin/env python3
"""Скачивает все фото для Istanbul Guide в папку images/"""
import urllib.request
import ssl
import os
import time

os.makedirs('images', exist_ok=True)

# Обход SSL-ошибок на macOS
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

images = {
    'galataport.jpg':   'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Istanbul%2C_Turkey_%28November_2023%29_-_611.jpg/800px-Istanbul%2C_Turkey_%28November_2023%29_-_611.jpg',
    'baklava.jpg':      'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Baklava_-_Turkish_special%2C_80-ply.JPEG/800px-Baklava_-_Turkish_special%2C_80-ply.JPEG',
    'cistern.jpg':      'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Cisterna_Bas%C3%ADlica%2C_Estambul%2C_Turqu%C3%ADa%2C_2024-09-28%2C_DD_73-75_HDR.jpg/800px-Cisterna_Bas%C3%ADlica%2C_Estambul%2C_Turqu%C3%ADa%2C_2024-09-28%2C_DD_73-75_HDR.jpg',
    'hagia_sophia.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Hagia_Sophia_%28228968325%29.jpeg/800px-Hagia_Sophia_%28228968325%29.jpeg',
    'blue_mosque.jpg':  'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Blue_Mosque_2.jpg/800px-Blue_Mosque_2.jpg',
    'gulhane.jpg':      'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/G%C3%BClhane_Park%2C_Istanbul.jpg/800px-G%C3%BClhane_Park%2C_Istanbul.jpg',
    'grand_bazaar.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Grand_Bazaar_Istanbul_-_panoramio.jpg/800px-Grand_Bazaar_Istanbul_-_panoramio.jpg',
    'galata_tower.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Galata_tower_01_23.jpg/800px-Galata_tower_01_23.jpg',
    'taksim.jpg':       'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Taksim_Square_2020.jpg/800px-Taksim_Square_2020.jpg',
    'galata_bridge.jpg':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Fishermen_on_Galata_Bridge.JPG/800px-Fishermen_on_Galata_Bridge.JPG',
    'turkish_food.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Some_Turkish_food_and_desserts.jpg/800px-Some_Turkish_food_and_desserts.jpg',
}

headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://en.wikipedia.org/'}

for filename, url in images.items():
    path = os.path.join('images', filename)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15, context=ssl_ctx) as r:
            data = r.read()
        with open(path, 'wb') as f:
            f.write(data)
        print(f'✓ {filename} ({len(data)//1024} KB)')
    except Exception as e:
        print(f'✗ {filename}: {e}')
    time.sleep(2)

print('\nГотово! Все фото в папке images/')
