import tkinter

class My_GUI:


    def __init__(self):


        # frames
        
        self.window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.window)
        self.top_frame.pack()

        self.middle_frame = tkinter.Frame(self.window)
        self.middle_frame.pack()

        self.bottom_frame = tkinter.Frame(self.window)
        self.bottom_frame.pack()

        self.button_frame = tkinter.Frame(self.window)
        self.button_frame.pack()


        # top_frame elements

        self.text_label1 = tkinter.Label(
            self.top_frame,
            text='Введите количество галлонов:'
            )
        self.text_label1.pack(side='left')

        self.entry_gal = tkinter.Entry(
            self.top_frame,
            width=10
            )
        self.entry_gal.pack(side='left')


        # middle_frame elements

        self.text_label2 = tkinter.Label(
            self.middle_frame,
            text='Введите количество миль:'
            )
        self.text_label2.pack(side='left')

        self.entry_miles = tkinter.Entry(
            self.middle_frame,
            width=10
            )
        self.entry_miles.pack(side='left')
        

        # bottom_frame elements

        self.text_label3 = tkinter.Label(
            self.bottom_frame,
            text='Мили на галлон (MPG) = '
            )
        self.text_label3.pack(side='left')

        self.mg = tkinter.StringVar()

        self.mg_label = tkinter.Label(
            self.bottom_frame,
            textvariable=self.mg
            )
        self.mg_label.pack()


        # button_frame elements

        self.calculate_button = tkinter.Button(
            self.button_frame,
            text='Вычислить MPG',
            command=self.calc
            )
        self.calculate_button.pack(side='left')

        self.quit_button = tkinter.Button(
            self.button_frame,
            text='Выйти',
            command=self.window.destroy
            )
        self.quit_button.pack(side='left')

        
    def calc(self):

        self.mg.set(
            str(float(self.entry_miles.get())/float(self.entry_gal.get()))
            )

        
        tkinter.mainloop()

t = My_GUI()
