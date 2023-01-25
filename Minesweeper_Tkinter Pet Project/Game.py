from tkinter import messagebox
from Buttons import Buttons
from Window import Window


class Game:
    window = Window()
    colors = {'1': 'blue', '2': 'green', '3': 'red', '4': 'orange', '5': 'magenta', '6': 'purple', '7': 'brown', '8': 'black'}

    def __init__(self):
        self.window.bind('<FocusOut>', self.exit)
        self.bind_commands()
        self.window.mainloop()

    def bind_commands(self):
        for i in self.window.list_button:
            for j in i:
                j['command'] = lambda temp=j: self.click(temp)

    def click(self, button: Buttons):
        if button.is_mine:
            button['image'] = button.boom
            # messagebox.showinfo(message='BOOM!!!')
        elif button.count_near_mines:
            button.configure(text=button.number, state='disabled')
            if str(button.count_near_mines) in self.colors:
                button['disabledforeground'] = self.colors[str(button.count_near_mines)]
            button['text'] = button.count_near_mines
        else:
            button.configure(relief='sunken', state='disabled')
            coords = (button.coordinates[0] - 1, button.coordinates[1],
                      button.coordinates[0] + 1, button.coordinates[1],
                      button.coordinates[0], button.coordinates[1] - 1,
                      button.coordinates[0], button.coordinates[1] + 1,)
            # for i, j in coords:
            #     if
            #     if self.window.list_button[i][j].number is not None:
            #         # self.click(self.window.list_button[i][j])
            #         print(i, j, button.x, button.y, self.window.list_button[i][j].number)


    def exit(self, event):
        """Закрытие без фокуса"""
        self.window.destroy()


if __name__ == '__main__':
    Minesweeper = Game()
