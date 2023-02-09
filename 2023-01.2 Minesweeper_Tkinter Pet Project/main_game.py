from time import perf_counter

from buttons import Buttons
from final_window import Final
from window import Window


class Game:
    """Class for main game and click processing"""
    colors = {'1': 'blue', '2': 'green', '3': 'red', '4': 'orange', '5': 'magenta', '6': 'purple', '7': 'brown', '8': 'black'}

    def __init__(self):
        self.list_bombs_numbers = []
        self.list_opened = []
        self.list_alarms = []
        self.window = Window(self)
        self._game_starts = False
        self.list_alarms = []
        self.bind_commands()
        self.window.mainloop()

    def bind_commands(self):
        """Binding commands to buttons when pressed"""
        for row in self.window.list_button:
            for btn in row:
                btn.bind('<Button-1>', lambda temp=btn: self.click_validation(temp))
                btn.bind('<Button-3>', lambda temp=btn: self.alarm(temp))

    def alarm(self, event):
        """Handling a right click on a field"""
        button: Buttons = event.widget
        if button.is_open:
            return
        if button['image']:
            button['image'] = ''
            self.list_alarms.pop(self.list_alarms.index(button.number))
        else:
            button['image'] = button.alarm
            self.list_alarms.append(button.number)
        self.window.bottom_panel.counter(self)

    def click_validation(self, event):
        """Left-click validation before handling"""
        button: Buttons = event.widget
        if button['image'] or button.is_open:
            return
        if not self._game_starts and button.is_bomb:
            self.first_is_bomb(button)
        if not self._game_starts:
            self.window.bottom_panel.base_time = perf_counter() + self.window.mods[self.window.mode][str(self.window.side)][1] * 60 + 1
            self.window.bottom_panel.tick(self, self.window)
            self._game_starts = True
        self.click(button)

    def click(self, button):
        """Handling left-click on the field"""
        if button.is_bomb:
            button['image'] = button.first_boom
            button.is_open = True
            for row in self.window.list_button:
                for btn in row:
                    if btn.is_bomb and btn.number != button.number:
                        btn.configure(image=btn.boom)
            self.win_or_not(button, win=False)

        elif button.count_near_bombs:
            button.configure(text=button.count_near_bombs, relief='sunken', state='disabled')
            button['disabledforeground'] = self.colors[str(button.count_near_bombs)]
            button.is_open = True
            self.list_opened.append(button.number)
            self.win_or_not(button, win=True)

        else:
            button.configure(text='', relief='sunken', state='disabled')
            self.breadth_first_search(button)
            self.win_or_not(button, win=True)

    def first_is_bomb(self, button: Buttons):
        """Executed if the first click hits a bomb"""
        while button.is_bomb:
            self.window.create_bombs(game=self, button=button)
        self.window.count_bombs()
        for row in self.window.list_button:
            for btn in row:
                if btn.number in self.list_alarms:
                    btn['image'] = button.alarm

    def breadth_first_search(self, button: Buttons):
        """Breadth-first search algorithm for finding neighboring cells without mines"""
        temp_list = [button]
        while temp_list:
            current_button = temp_list.pop()
            current_button.configure(relief='sunken', state='disabled')
            current_button.is_open = True
            if current_button['image']:
                current_button['image'] = ''
                self.list_alarms.pop(self.list_alarms.index(current_button.number))
                self.window.bottom_panel.counter(self)
            self.list_opened.append(current_button.number)
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

    def win_or_not(self, button=None, win=None):
        """Win or lose check"""
        if not win:
            self.window.after_cancel(self.window.bottom_panel.after_id)
            self.window.bottom_panel.counter_bombs.configure(fg='red')
            Final(window=self.window, game=self, win=False)
        elif len(set(self.list_opened)) == self.window.side ** 2 - len(self.list_bombs_numbers):
            self.window.after_cancel(self.window.bottom_panel.after_id)
            for row in self.window.list_button:
                for btn in row:
                    if btn.is_bomb and btn.number != button.number:
                        btn.configure(image=btn.boom)
            self.window.bottom_panel.counter_bombs.configure(text='0', fg='green')
            Final(window=self.window, game=self, win=True)


if __name__ == '__main__':
    Minesweeper = Game()
