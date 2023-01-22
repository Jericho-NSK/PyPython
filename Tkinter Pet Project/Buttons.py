from tkinter import Button


class Buttons(Button):
    """Buttons creator"""
    _bg = '#9D9DF2'
    _font = 'Arial', 16, 'bold'
    _pad = 3

    def __init__(self, text: str = '',
                 bg: str = _bg,
                 activebackground=_bg,
                 font: tuple = _font,
                 bd=7,
                 command=None):
        super().__init__(text=text, bg=bg, activebackground=activebackground, font=font, bd=bd, command=command)
        self.grid(stick='wens', padx=self._pad, pady=self._pad)
