from time import perf_counter
from tkinter import Label


class BottomPanel:
    """Class for creating a bottom field with a timer and bomb counter"""
    _font = 'Calibre', 12, 'bold'

    def __init__(self, window, game):
        self.base_time = None
        self.after_id = None
        self.time_text = None
        self.time = None
        self.counter_text = None
        self.counter_bombs = None
        self.create_text(window, game)

    def create_text(self, window, game):
        """Creating Labels"""
        if window.side == 5:
            text_column = 0
            count_column = 3
        elif window.side == 10:
            text_column = 1
            count_column = 6
        else:
            text_column = 3
            count_column = 9

        Label(master=window, text='Timer:', font=self._font).grid(row=window.side, column=text_column, columnspan=3, sticky='e', padx=15)
        self.time = Label(master=window, text=f'{window.mods[window.mode][str(window.side)][1]}:00', font=self._font)
        self.time.grid(row=window.side, column=count_column, columnspan=2, sticky='we')

        Label(master=window, text='Bombs:', font=self._font).grid(row=window.side + 1, column=text_column, columnspan=3, sticky='e', padx=15)
        self.counter_bombs = Label(master=window, text=len(game.list_bombs_numbers), font=self._font)
        self.counter_bombs.grid(row=window.side + 1, column=count_column, columnspan=2, sticky='we')

    def tick(self, game, window):
        """Timer that starts on the first click in the Game class"""
        self.after_id = window.after(1000, lambda: self.tick(game, window))
        minutes = f'{int((self.base_time - perf_counter()) // 60)}'
        seconds = f'{int((self.base_time - perf_counter()) % 60)}'.rjust(2, '0')
        timer = f'{minutes}:{seconds}'
        self.time['text'] = timer
        if int(minutes) <= 0 and int(seconds) == 0:
            game.win_or_not(win=False)
            self.time['fg'] = 'red'

    def counter(self, game):
        """Undiscovered bombs counter"""
        unfounded_bombs = len(game.list_bombs_numbers) - len(game.list_alarms)
        self.counter_bombs['text'] = unfounded_bombs
        if unfounded_bombs < 0:
            self.counter_bombs['fg'] = 'red'
        else:
            self.counter_bombs['fg'] = 'black'
