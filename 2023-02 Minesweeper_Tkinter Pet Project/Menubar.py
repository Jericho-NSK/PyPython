from tkinter import Menu, StringVar, IntVar, Toplevel, Label, Button
from webbrowser import open_new_tab


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
        self.add_command(label='About', command=About)
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


class About(Toplevel):
    """Class for creating 'About' window"""
    _font = 'Comic Sans MS', 12, 'bold'
    _font_url = 'Comic Sans MS', 12, 'bold', 'underline', 'italic'

    def __init__(self):
        super().__init__()
        self.geometry('500x340+498+100')
        self.resizable(False, False)
        self.create_about()
        self.grab_set()

    def create_about(self):
        """Creating 'About' window"""
        text_name = 'Minesweeper v1.0'
        text_rules = 'Left-click checks the cell\nRight-click marks the cell as "ALARM"\nFirst click will never find the bomb'
        text = 'Created by Jericho for Pet-project'
        pady = 4

        Label(master=self, font=self._font, text=text_name, fg='brown').pack(pady=pady)
        Label(master=self, font=self._font, text=text_rules, fg='green').pack(pady=pady)
        Label(master=self, font=self._font, text=text, fg='magenta').pack(pady=pady)

        link = Label(master=self, font=self._font_url, text='Link to GitHub', fg='blue', cursor='hand2')
        link.pack(pady=pady)
        link.bind('<Button-1>', lambda temp=link: self.open_url(link))

        Label(master=self, font=self._font, text='2023', fg='red').pack(pady=pady)

        ok_button = Button(master=self, text='OK', bd=8, font=self._font, width=12, cursor='hand2')
        ok_button.pack(pady=pady)
        ok_button.bind('<Button-1>', lambda temp=ok_button: self.destroy())

    @staticmethod
    def open_url(link):
        """Opening URL to GitHub"""
        open_new_tab('https://github.com/Jericho-NSK/PyPython/tree/main/2023-02%20Minesweeper_Tkinter%20Pet%20Project')
        link['fg'] = 'purple'
