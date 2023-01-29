from Buttons import Buttons
from Window import Window


class Game:
    """Кла для основного игрового процесса и обработки нажатий"""
    colors = {'1': 'blue', '2': 'green', '3': 'red', '4': 'orange', '5': 'magenta', '6': 'purple', '7': 'brown', '8': 'black'}

    def __init__(self):
        self.window = Window(self)
        self._game_starts = False
        self.list_alarms = []
        self.bind_commands()
        self.window.mainloop()

    def bind_commands(self):
        """Присвоение кнопкам команд при нажатии"""
        for row in self.window.list_button:
            for btn in row:
                btn.bind('<Button-1>', lambda temp=btn: self.click_validation(temp))
                btn.bind('<Button-3>', lambda temp=btn: self.alarm(temp))

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

    def click_validation(self, event):
        """Валидация нажатия левой кнопки перед обработкой"""
        button: Buttons = event.widget
        if button['image'] or button.is_open:
            return
        if not self._game_starts and button.is_bomb:
            self.first_is_bomb(button)
        self._game_starts = True
        self.click(button)

    def click(self, button):
        """Обработка нажатия левой кнопкой на поле"""
        if button.is_bomb:
            button['image'] = button.first_boom
            button.is_open = True
            for row in self.window.list_button:
                for btn in row:
                    if btn.is_bomb and btn.number != button.number:
                        btn.configure(image=btn.boom)
                    while btn._tclCommands:
                        btn.deletecommand(btn._tclCommands[0])
            self.window.end_game(game=self, win=False)
        elif button.count_near_bombs:
            button.configure(text=button.count_near_bombs, relief='sunken', state='disabled')
            button['disabledforeground'] = self.colors[str(button.count_near_bombs)]
            button.is_open = True
        else:
            button.configure(text='', relief='sunken', state='disabled')
            self.breadth_first_search(button)

    def first_is_bomb(self, button: Buttons):
        """Выполнятся если первый клик попал по бомбе"""
        while button.is_bomb:
            self.window.create_bombs(button=button)
        self.window.count_bombs()
        for row in self.window.list_button:
            for btn in row:
                if btn.number in self.list_alarms:
                    btn['image'] = button.alarm

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
                        next_button = self.window.list_button[x + dx][y + dy]
                        if not next_button.is_open and next_button.number is not None and current_button not in temp_list:
                            temp_list.append(next_button)


if __name__ == '__main__':
    Minesweeper = Game()
