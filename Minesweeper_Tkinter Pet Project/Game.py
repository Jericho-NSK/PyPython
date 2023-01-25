from random import sample

from Window import Window


class Game:
    window = Window()

    def __init__(self):
        self.window.bind('<FocusOut>', self.exit)
        self.create_mines()
        self.window.mainloop()

    def create_mines(self):
        total = self.window._row * self.window._column
        mines_numbers = sample(range(1, total + 1), total // 3)
        for i in self.window.list_button:
            if i.number in mines_numbers:
                i.is_mine = True
            print(i.number, i.is_mine)

    def exit(self, event):
        """Закрытие без фокуса"""
        self.window.quit()


if __name__ == '__main__':
    Minesweeper = Game()
