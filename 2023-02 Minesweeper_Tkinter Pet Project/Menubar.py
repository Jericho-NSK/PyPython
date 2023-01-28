from tkinter import Menu


class Menubar(Menu):

    def __init__(self, window, game):
        super().__init__(master=window)
        self.create_menu(window, game)
        window.config(menu=self)

    def create_menu(self, window, game):
        """Создание меню"""
        self.add_command(label='New', command=lambda: self.new_game(window, game))

        size = Menu(self, tearoff=0)
        size.add_radiobutton(label='5x5', command=lambda: self.new_size(window, 5))
        size.add_radiobutton(label='10x10', command=lambda: self.new_size(window, 10))
        size.add_radiobutton(label='15x15', command=lambda: self.new_size(window, 15))
        self.add_cascade(label='Size', menu=size)

        mode = Menu(self, tearoff=0)
        mode.add_command(label='Easy', command=lambda: self.new_mode(window, 'easy'))
        mode.add_command(label='Normal', command=lambda: self.new_mode(window, 'normal'))
        mode.add_command(label='Hard', command=lambda: self.new_mode(window, 'hard'))
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

    @staticmethod
    def new_mode(window, mode):
        """Задание нового режима при изменении через меню"""
        window.mode = mode
