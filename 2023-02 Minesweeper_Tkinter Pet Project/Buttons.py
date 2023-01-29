from tkinter import Button

from PIL import Image, ImageTk


class Buttons(Button):
    """Класс для создания кнопок, по которым будет кликать игрок"""
    button_size = 40
    _font = 'Arial', 11, 'bold'
    _bd = 3
    _icon_size = int(button_size * 0.82)
    _boom_icon = Image.open('Boom.png').resize((_icon_size, _icon_size))
    _first_boom_icon = Image.open('FirstBoom.png').resize((_icon_size, _icon_size))
    _alarm_icon = Image.open('Alarm.png').resize((_icon_size, _icon_size))

    def __init__(self, x=0, y=0, number=None):
        super().__init__(bd=self._bd,
                         font=self._font)
        self.first_boom = None
        self.boom = None
        self.alarm = None
        self['image'] = None
        self.x = x
        self.y = y
        self.number = number
        self.is_bomb = False
        self.count_near_bombs = False
        self.is_open = False
        self.create_icons()

    def create_icons(self):
        self.first_boom = ImageTk.PhotoImage(self._first_boom_icon)
        self.boom = ImageTk.PhotoImage(self._boom_icon)
        self.alarm = ImageTk.PhotoImage(self._alarm_icon)
