from tkinter import messagebox

from Buttons import Buttons
from Window import Window


class Game:
    window = Window()
    colors = {'1': 'blue', '2': 'green', '3': 'red', '4': 'orange', '5': 'magenta', '6': 'purple', '7': 'brown', '8': 'black'}

    def __init__(self):
        self._game_starts = False
        self.window.bind('<FocusOut>', self.exit)
        self.list_alarms = []
        self.bind_commands()
        self.window.mainloop()

    def bind_commands(self):
        """Присвоение кнопкам команды при нажатии"""
        for i in self.window.list_button:
            for j in i:
                j.bind('<Button-1>', lambda temp=j: self.click(temp))
                j.bind('<Button-3>', lambda temp=j: self.alarm(temp))

    def alarm(self, event):
        """Обработка нажатия правой кнопкой на поле"""
        button: Buttons = event.widget
        if button.is_open:
            return
        if button['image']:
            button['image'] = ''
            self.list_alarms.pop(self.list_alarms.index(button.number))
        else:
            button['image'] = button.alarm
            self.list_alarms.append(button.number)

    def click(self, event):
        """Обработка нажатия левой кнопкой на поле"""
        button: Buttons = event.widget
        if button['image']:
            return
        if button.is_bomb and not self._game_starts:
            while button.is_bomb:
                self.window.create_bombs(button)
            self.window.count_bombs()

            for i in self.window.list_button:
                for j in i:
                    if j.number in self.list_alarms:
                        j['image'] = button.alarm
        self._game_starts = True
        if button.is_bomb:
            button['image'] = button.first_boom
            button.is_open = True
            # messagebox.showinfo('Game over', message='BOOM!!!')
            for i in range(self.window.column):
                for j in range(self.window.row):
                    btn: Buttons = self.window.list_button[i][j]
                    if btn.is_bomb and btn.number != button.number:
                        btn.configure(image=btn.boom)
                    while btn._tclCommands:
                        btn.deletecommand(btn._tclCommands[0])
        elif button.count_near_bombs:
            button.configure(text=button.count_near_bombs, relief='sunken', state='disabled')
            button['disabledforeground'] = self.colors[str(button.count_near_bombs)]
            button.is_open = True
        else:
            button.configure(text='', relief='sunken', state='disabled')
            self.breadth_first_search(button)

    def breadth_first_search(self, button: Buttons):
        """Алгоритм обхода в ширину для поиска соседних клеток без мин"""
        temp_list = [button]
        while temp_list:
            current_button = temp_list.pop()
            current_button.configure(image='', relief='sunken', state='disabled')
            current_button.is_open = True
            if current_button.count_near_bombs:
                current_button['text'] = current_button.count_near_bombs
                current_button['disabledforeground'] = self.colors[str(current_button.count_near_bombs)]
            else:
                x, y = current_button.x, current_button.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # if dx or dy:
                        next_button = self.window.list_button[x + dx][y + dy]
                        if not next_button.is_open and next_button.number is not None and current_button not in temp_list:

                            temp_list.append(next_button)

    def exit(self, event):
        """Закрытие без фокуса"""
        self.window.quit()


if __name__ == '__main__':
    Minesweeper = Game()
