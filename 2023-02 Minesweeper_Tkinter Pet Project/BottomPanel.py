from tkinter import Label
from time import asctime, localtime, time, strptime, strftime, monotonic, perf_counter
from datetime import datetime, timedelta

class BottomPanel:
    _font = 'Calibre', 12, 'bold'

    def __init__(self, window, game):
        self.base_time = 0
        self.base_time = None
        self.start = window.mods[window.mode][str(window.side)][1]
        self.temp = 0
        self.after_id = ''
        self.time_text = 0
        self.time = 0
        self.counter_text = 0
        self.counter_bombs = 0
        self.create_timer(window, game)
        self.create_counter(window, game)

    def create_timer(self, window, game):
        self.time_text = Label(master=window, text='Timer:', font=self._font)
        self.time_text.grid(row=window.side, columnspan=2, sticky='e')
        self.time = Label(master=window, text=f'{window.mods[window.mode][str(window.side)][1]}:00', font=self._font)
        self.time.grid(row=window.side, column=2, columnspan=3)

    def create_counter(self, window, game):
        self.counter_text = Label(master=window, text='Bombs:', font=self._font)
        self.counter_text.grid(row=window.side+1, columnspan=2, sticky='e')
        self.counter_bombs = Label(master=window, text=len(game.list_alarms), font=self._font)
        self.counter_bombs.grid(row=window.side + 1, column=2, columnspan=3)

    def tick(self, game, window):
        self.after_id = window.after(1000, lambda: self.tick(game, window))
        minutes = f'{int((self.base_time - perf_counter())//60)}'
        seconds = f'{int((self.base_time - perf_counter()) % 60)}'.rjust(2, '0')
        timer = f'{minutes}:{seconds}'
        self.time['text'] = timer
        if int(minutes) <= 0 and int(seconds) <= 0:
            game.win_or_not(win=False)
            self.time['fg'] = 'red'



