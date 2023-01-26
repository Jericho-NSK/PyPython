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
        """Присвоение кнопкам команды при нажатии"""
        for i in self.window.list_button:
            for j in i:
                j['command'] = lambda temp=j: self.click(temp)

    def click(self, button: Buttons):
        """Обработка нажатия на поле"""
        if button.is_mine:
            button['image'] = button.boom
            button.is_open = True
            # messagebox.showinfo(message='BOOM!!!')
        elif button.count_near_mines:
            button.configure(text=button.count_near_mines, relief='sunken', state='disabled')
            button['disabledforeground'] = self.colors[str(button.count_near_mines)]
            button.is_open = True
        else:
            button.configure(text='', relief='sunken', state='disabled')
            self.breadth_first_search(button)

    def breadth_first_search(self, button: Buttons):
        """Алгоритм обхода в ширину для поиска соседних клеток без мин"""
        temp_list = [button]
        while temp_list:
            current_button = temp_list.pop()
            current_button.configure(relief='sunken', state='disabled')
            current_button.is_open = True
            if current_button.count_near_mines:
                current_button['text'] = current_button.count_near_mines
                current_button['disabledforeground'] = self.colors[str(current_button.count_near_mines)]
            else:
                x, y = current_button.x, current_button.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if abs(dx-dy) == 1:
                            next_button = self.window.list_button[x+dx][y+dy]
                            if not next_button.is_open and next_button.number is not None and current_button not in temp_list:
                                temp_list.append(next_button)

    def exit(self, event):
        """Закрытие без фокуса"""
        self.window.quit()


if __name__ == '__main__':
    Minesweeper = Game()
