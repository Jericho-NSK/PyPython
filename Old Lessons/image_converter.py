import os
from io import BytesIO

import pygame
from PIL import Image


# icon = Image.open(os.path.join(os.getcwd(), 'images', f'{filename}.png').reduce(5)  # Уменьшение в 5 раз

def pillow_only(filename, width=80, height=80) -> Image:
    """Convert to image with new size WITHOUT creating new file"""
    pil_icon = Image.open(os.path.join(os.getcwd(), 'images', f'{filename}.png'), mode='r')
    pil_icon = pil_icon.resize((width, height))

    pil_icon = pygame.image.frombuffer(pil_icon.tobytes(), (width, height), 'RGBA')
    pil_icon = pil_icon.convert_alpha()
    return pil_icon


def new_image(filename, width=80, height=80, new_file=False) -> None | bytes:
    """Convert to the image with new size to bytecode WITH OR WITHOUT creating a new file"""
    icon = Image.open(os.path.join(os.getcwd(), 'images', 'originals', f'original_{filename}.png'), mode='r')
    icon = icon.resize((width, height))

    icon_arr = BytesIO()
    icon.save(icon_arr, format='PNG')
    icon_arr = icon_arr.getvalue()
    if new_file:
        with open(os.path.join(os.getcwd(), 'images', f'{filename}.png'), 'wb') as file:
            file.write(icon_arr)
    else:
        return icon_arr


pillow_only()
new_image()
