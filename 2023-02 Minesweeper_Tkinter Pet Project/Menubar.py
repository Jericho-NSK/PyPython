from tkinter import Menu, StringVar, IntVar, Toplevel


class Menubar(Menu):
    """Class for creating a menu bar with settings"""

    def __init__(self, window, game):
        super().__init__(master=window)
        self.size_var = IntVar(value=window.side)
        self.mode_var = StringVar(value=window.mode)
        self.create_menu(window, game)
        window.config(menu=self)

    def create_menu(self, window, game):
        """Creating menubar"""
        size = Menu(self, tearoff=0)
        size.add_radiobutton(label='5x5', variable=self.size_var, value=5, command=lambda: self.new_size(window, 5))
        size.add_radiobutton(label='10x10', variable=self.size_var, value=10, command=lambda: self.new_size(window, 10))
        size.add_radiobutton(label='15x15', variable=self.size_var, value=15, command=lambda: self.new_size(window, 15))

        mode = Menu(self, tearoff=0)
        mode.add_radiobutton(label='Easy', variable=self.mode_var, value='easy', command=lambda: self.new_mode(window, 'easy'))
        mode.add_radiobutton(label='Normal', variable=self.mode_var, value='normal', command=lambda: self.new_mode(window, 'normal'))
        mode.add_radiobutton(label='Hard', variable=self.mode_var, value='hard', command=lambda: self.new_mode(window, 'hard'))

        self.add_command(label='New', command=lambda: self.new_game(window, game))
        self.add_cascade(label='Size', menu=size)
        self.add_cascade(label='Mode', menu=mode)
        self.add_command(label='Exit', command=self.quit)

    @staticmethod
    def new_game(window, game, final: Toplevel = False):
        """Operations when starting a new game"""
        if final:
            final.destroy()
        [child.destroy() for child in window.winfo_children() if '!buttons' in child._name]
        if window.bottom_panel.after_id:
            window.after_cancel(window.bottom_panel.after_id)
        window.new_window(game=game)
        game.bind_commands()
        game._game_starts = False
        game.list_alarms.clear()
        game.list_opened.clear()

    @staticmethod
    def new_size(window, size):
        """Setting new size when changing using the menu"""
        window.side = size

    @staticmethod
    def new_mode(window, mode):
        """Setting a new mode when changing using the menu"""
        window.mode = mode
