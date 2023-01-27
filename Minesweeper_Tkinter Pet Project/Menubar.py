from tkinter import Menu


class Menubar(Menu):

    def __init__(self, window, game):
        super().__init__(master=window)
        self.create_menu(window, game)

    def create_menu(self, window, game):
        """Создание меню"""
        self.add_command(label='New', command=lambda: self.new(window, game))

        difficulty = Menu(self, tearoff=0)
        difficulty.add_command(label='Easy')
        difficulty.add_command(label='Normal')
        difficulty.add_command(label='Hard')
        self.add_cascade(label='Difficulty', menu=difficulty)

        self.add_command(label='Exit', command=self.quit)

    @staticmethod
    def new(window, game):
        [child.destroy() for child in window.winfo_children() if '!buttons' in child._name]
        window.create_default_buttons()
        window.create_buttons()
        window.create_bombs()
        window.alignment()
        window.count_bombs()
        game.bind_commands()
