import tkinter
import tkinter.messagebox

class My_GUI:
    

    def __init__(self):


        # frames

        self.window = tkinter.Tk()

        self.radio_button_frame = tkinter.Frame(self.window)
        self.radio_button_frame.pack()

        self.entry_frame = tkinter.Frame(self.window)
        self.entry_frame.pack()

        self.button_frame = tkinter.Frame(self.window)
        self.button_frame.pack()


        # variables for radio button

        self.v = tkinter.IntVar()
        self.v.set(1)


        # radio_button_frame elements

        self.rb1 = tkinter.Radiobutton(
            self.radio_button_frame,
            text='Дневное вемя (6:00 - 17:59)',
            variable=self.v,
            value=1
            )
        self.rb1.pack()

        self.rb2 = tkinter.Radiobutton(
            self.radio_button_frame,
            text='Вечернее время (18:00 - 23:59)',
            variable=self.v,
            value=2
            )
        self.rb2.pack()

        self.rb3 = tkinter.Radiobutton(
            self.radio_button_frame,
            text='Непиковый период (00:00 - 5:59)',
            variable=self.v,
            value=3
            )
        self.rb3.pack()


        # entry_frame elements

        self.label = tkinter.Label(
            self.entry_frame,
            text='Введите количество минут:'
            )
        self.label.pack(side='left')

        self.entry = tkinter.Entry(
            self.entry_frame
            )
        self.entry.pack(side='left')


        # button_frame elements

        self.show_cost_button = tkinter.Button(
            self.button_frame,
            text='Показать стоимость',
            command=self.show_cost
            )
        self.show_cost_button.pack(side='left')

        self. quit_button = tkinter.Button(
            self.button_frame,
            text='Выйти',
            command=self.window.destroy
            )
        self.quit_button.pack(side='left')


        tkinter.mainloop()


    def show_cost(self):

        self.message = 'Ваши затраты = $'
        
        if self.v.get() == 1:
            self.message = self.message + str(int(self.entry.get())*0.16)
        elif self.v.get() == 2:
            self.message = self.message + str(int(self.entry.get())*0.2)
        elif self.v.get() == 3:
            self.message = self.message + str(int(self.entry.get())*0.08)

        tkinter.messagebox.showinfo('Общая стоимость', self.message)



t = My_GUI()
