import tkinter

class My_GUI:


    def __init__(self):

        self.window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.window)
        self.top_frame.pack()

        self.middle_frame = tkinter.Frame(self.window)
        self.middle_frame.pack()

        self.bottom_frame = tkinter.Frame(self.window)
        self.bottom_frame.pack()

        self.text = tkinter.StringVar()
        self.text.set('средний')

        self.label = tkinter.Label(self.top_frame,textvariable=self.text)
        self.label.pack()

        self.button1 = tkinter.Button(
            self.middle_frame,
            text='sinister',
            command=self.set_sinister
            )
        self.button1.pack(side='left')

        self.button2 = tkinter.Button(
            self.middle_frame,
            text='dexter',
            command=self.set_dexter
            )
        self.button2.pack(side='left')

        self.button3 = tkinter.Button(
            self.middle_frame,
            text='medium',
            command=self.set_medium
            )
        self.button3.pack(side='left')

        self.quit_button = tkinter.Button(
            self.bottom_frame,
            text='Выйти',
            command=self.window.destroy
            )
        self.quit_button.pack()

        tkinter.mainloop()

    def set_sinister(self):

        self.text.set('зловещий')


    def set_dexter(self):

        self.text.set('правый')


    def set_medium(self):

        self.text.set('средний')


t = My_GUI()
