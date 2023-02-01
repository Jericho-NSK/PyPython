from tkinter import Toplevel, Label, Radiobutton, Button, IntVar, StringVar

from Menubar import Menubar


class Final(Toplevel):
    """Class for creating the final window to be called in case of a win or loss"""
    _font = 'Malgun Gothic', 14, 'bold'
    _font_buttons = 'Comic Sans MS', 16, 'bold'

    def __init__(self, window, game, win: bool):
        super().__init__(takefocus=True)
        self.size_var = IntVar(value=window.new_side)
        self.mode_var = StringVar(value=window.new_mode)
        self.geometry('500x350+498+100')
        self.resizable(False, False)
        self.create_menu(window, game, win)
        self.final_alignment()
        self.grab_set()

    def create_menu(self, window, game, win):
        """Creating the final window"""
        Label(master=self, font=self._font_buttons, text='YOU ARE WINNER!!!' if win else 'YOU LOSE :(',
              fg='green' if win else 'red').grid(row=0, column=1, columnspan=3, pady=5)

        Label(master=self, font=self._font, text='Size').grid(row=1, column=1, ipadx=50, padx=50)

        Radiobutton(master=self, text='5x5', font=self._font, variable=self.size_var, value=5, relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_size(window, 5), cursor='hand2').grid(row=2, column=1, pady=5)
        Radiobutton(master=self, text='10x10', font=self._font, variable=self.size_var, value=10, relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_size(window, 10), cursor='hand2').grid(row=3, column=1, pady=5)
        Radiobutton(master=self, text='15x15', font=self._font, variable=self.size_var, value=15, relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_size(window, 15), cursor='hand2').grid(row=4, column=1, pady=5)

        Label(master=self, font=self._font, text='Mode').grid(row=1, column=3, ipadx=60, padx=40)

        Radiobutton(master=self, text='Easy', font=self._font, variable=self.mode_var, value='easy', relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_mode(window, 'easy'), cursor='hand2').grid(row=2, column=3, pady=5)
        Radiobutton(master=self, text='Normal', font=self._font, variable=self.mode_var, value='normal', relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_mode(window, 'normal'), cursor='hand2').grid(row=3, column=3, pady=5)
        Radiobutton(master=self, text='Hard', font=self._font, variable=self.mode_var, value='hard', relief='groove', bd=5, width=7,
                    command=lambda: Menubar.new_mode(window, 'hard'), cursor='hand2').grid(row=4, column=3, pady=5)

        Button(master=self, text='New game', font=self._font_buttons, bd=6, fg='green', cursor='hand2',
               command=lambda: Menubar.new_game(window, game, final=self)).grid(row=5, column=1, ipadx=20, pady=15)
        Button(master=self, text='Exit', font=self._font_buttons, bd=6, fg='red', padx=40, cursor='hand2',
               command=self.quit).grid(row=5, column=3, ipadx=25, pady=15)

    def final_alignment(self):
        """Align buttons by width and height of field with equal weight"""
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, weight=1)
        for column in range(self.grid_size()[0]):
            self.grid_columnconfigure(column, weight=1)
