from tkinter import Toplevel, Label, Radiobutton, Button, IntVar, StringVar

from Menubar import Menubar


class Final(Toplevel):
    """Класс для создания финального окна, вызываемого в случае выигрыша или проигрыша"""
    _font = 'Calibre', 12, 'normal'
    _font_buttons = 'Calibre', 14, 'bold'

    def __init__(self, window, game, win: bool):
        super().__init__(takefocus=True)

        self._title = 'YOU ARE WINNER!!!' if win else 'YOU ARE LOOSE :('
        self.title(self._title)
        self.geometry('500x300+600+200')
        self.resizable(False, False)
        self.create_menu(window, game)
        self.final_alignment()
        self.grab_set()

    def final_alignment(self):
        """Выравнивание кнопок по ширине и высоте поля с равным весом"""
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, weight=1)
        for column in range(self.grid_size()[0]):
            self.grid_columnconfigure(column, weight=1)

    def create_menu(self, window, game):
        """Создание финального окна"""
        self.side_label = Label(master=self, font=self._font, text='Size').grid(row=0, column=1)
        self.size_var = IntVar(value=window.side)

        Radiobutton(master=self, text='5x5', font=self._font, variable=self.size_var, value=5, relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_size(window, 5)).grid(row=1, column=1)
        Radiobutton(master=self, text='10x10', font=self._font, variable=self.size_var, value=10, relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_size(window, 10)).grid(row=2, column=1)
        Radiobutton(master=self, text='15x15', font=self._font, variable=self.size_var, value=15, relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_size(window, 15)).grid(row=3, column=1)

        self.mode_label = Label(master=self, font=self._font, text='Mode').grid(row=0, column=3)
        self.mode_var = StringVar(value=window.mode)

        Radiobutton(master=self, text='Easy', font=self._font, variable=self.mode_var, value='easy', relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_mode(window, 'easy')).grid(row=1, column=3)
        Radiobutton(master=self, text='Normal', font=self._font, variable=self.mode_var, value='normal', relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_mode(window, 'normal')).grid(row=2, column=3)
        Radiobutton(master=self, text='Hard', font=self._font, variable=self.mode_var, value='hard',  relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_mode(window, 'hard')).grid(row=3, column=3)

        Button(master=self, text='New game', font=self._font_buttons, bd=6, fg='green',
                    command=lambda: Menubar.new_game(window, game, final=self)).grid(row=4, column=1, ipadx=40, ipady=5)
        Button(master=self, text='Exit', font=self._font_buttons, bd=6, fg='red',
                    command=self.quit).grid(row=4, column=3, ipadx=60, padx=30, ipady=5)
