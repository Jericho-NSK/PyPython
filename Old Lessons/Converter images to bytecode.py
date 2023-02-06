from io import BytesIO
from tkinter import PhotoImage

from PIL import Image

icon = Image.open(r'G:\Python\PyPython\2023-03 Pygame\Bomb_3.png', mode='r').resize((80, 80)).crop()  # требуемый размер
icon_arr = BytesIO()
icon.save(icon_arr, format='PNG')
icon_arr = icon_arr.getvalue()
print(icon_arr)  # <- скопировал результат из консоли в новую переменную byte_icon

byte_icon = b'...'  # <- тут длинная строка в байтовом виде. Весь код выше можно удалять.
# Кроме "from tkinter import PhotoImage", так как он еще нужен ниже

# final_img = PhotoImage(data=byte_icon, format='png')

with open('new_file3.png', 'wb') as file:  # Сохранение в новый файл
    file.write(icon_arr)
