from tkinter import Tk, Button, PhotoImage


class MainWindow(Tk):
    _row = 10
    _column = 10
    _width = 500
    _height = 500

    def __init__(self):
        super().__init__()
        self.geometry(f'{self._width}x{self._height}+1300+200')
        self.resizable(False, False)
        self.iconphoto(True, PhotoImage(file='Icon.png'))
        [Button(bd=3).grid(stick='wens', row=i, column=j) for i in range(self._row) for j in range(self._column)]
        self.make_grid()

        self.bind('<FocusOut>', self.exit)

    def exit(self, event):
        self.quit()

    def make_grid(self):
        print(self.grid_size())
        for i in range(self.grid_size()[0]):
            self.grid_columnconfigure(i, minsize=int(self._width / self.grid_size()[0]))
        for i in range(self.grid_size()[1]):
            self.grid_rowconfigure(i, minsize=int(self._height / self.grid_size()[1]))


sapper = MainWindow()
sapper.mainloop()
