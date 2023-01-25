from random import sample
from tkinter import messagebox
from Buttons import Buttons
from Window import Window


class Game:
    window = Window()

    def __init__(self):
        self.window.bind('<FocusOut>', self.exit)
        self.create_mines()

        self.bind_commands()
        self.window.mainloop()

    def create_mines(self):
        mines_numbers = sample(range(1, self.window.total + 1), self.window.total // 3)
        for i in self.window.list_button:
            if i.number in mines_numbers:
                i.is_mine = True

    def bind_commands(self):
        for i in self.window.list_button:
            i['command'] = lambda temp=i: self.click(temp)

    @staticmethod
    def click(button: Buttons):
        if button.is_mine:
            button['image'] = button.boom
        else:
            button.configure(text=button.number, state='disabled', disabledforeground='black')
        # messagebox.showinfo(message='BOOM!!!')

    def exit(self, event):
        """Закрытие без фокуса"""
        self.window.destroy()


if __name__ == '__main__':
    Minesweeper = Game()
