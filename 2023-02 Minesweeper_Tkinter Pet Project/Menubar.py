from tkinter import Menu, IntVar


class Menubar(Menu):

    def __init__(self, window, game):
        super().__init__(master=window)
        self.create_menu(window, game)
        window.config(menu=self)

    def create_menu(self, window, game):
        """Создание меню"""
        self.add_command(label='New', command=lambda: self.new(window, game))

        size = Menu(self, tearoff=0)
        size.add_radiobutton(label='5x5', command=lambda: self.size(window, 5))
        size.add_radiobutton(label='10x10', command=lambda: self.size(window, 10))
        size.add_radiobutton(label='15x15', command=lambda: self.size(window, 15))
        self.add_cascade(label='Size', menu=size)

        mode = Menu(self, tearoff=0)
        mode.add_command(label='Easy')
        mode.add_command(label='Normal')
        mode.add_command(label='Hard')
        self.add_cascade(label='Mode', menu=mode)

        self.add_command(label='Exit', command=self.quit)

    @staticmethod
    def new(window, game):
        """Операции при начале новой игры"""
        [child.destroy() for child in window.winfo_children() if '!buttons' in child._name]
        window.geometry(f'{window.width}x{window.height}+1000+100')
        window.create_default_buttons()
        window.create_buttons()
        window.create_bombs()
        window.alignment()
        window.count_bombs()
        game.bind_commands()
        game._game_starts = False

    @staticmethod
    def size(window, size):
        window.new_size(size)

