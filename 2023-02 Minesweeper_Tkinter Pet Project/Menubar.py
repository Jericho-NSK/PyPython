from tkinter import Menu, IntVar


class Menubar(Menu):

    def __init__(self, window, game):
        super().__init__(master=window)
        self.create_menu(window, game)
        window.config(menu=self)

    def create_menu(self, window, game):
        """Создание меню"""
        self.add_command(label='New', command=lambda: self.new_game(window, game))

        self.size = IntVar()
        self.size.set(10)
        self.size2 = Menu(self, tearoff=0)
        self.size2.add_radiobutton(value=5 if self.size == 5 else None, label='5x5', command=lambda: self.new_size(window, 5))
        self.size2.add_radiobutton(variable=True if self.size == 10 else None, label='10x10', command=lambda: self.new_size(window, 10))
        self.size2.add_radiobutton(value=15 if self.size == 15 else None, label='15x15', command=lambda: self.new_size(window, 15))
        self.add_cascade(label='Size', menu=self.size2)

        mode = Menu(self, tearoff=0)
        mode.add_command(label='Easy')
        mode.add_command(label='Normal')
        mode.add_command(label='Hard')
        self.add_cascade(label='Mode', menu=mode)

        self.add_command(label='Exit', command=self.quit)

    @staticmethod
    def new_game(window, game):
        """Операции при начале новой игры"""
        [child.destroy() for child in window.winfo_children() if '!buttons' in child._name]
        window.new_window()
        game.bind_commands()
        game._game_starts = False
        game.list_alarms.clear()

    @staticmethod
    def new_size(window, size):
        """Задание новых размеров при изменении через меню"""
        window.side = size

