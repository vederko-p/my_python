import tkinter
import tkinter.messagebox

class My_GUI():


    def __init__(self):


        # frames

        self.window = tkinter.Tk()

        self.check_button_frame = tkinter.Frame(self.window)
        self.check_button_frame.pack()

        self.button_frame = tkinter.Frame(self.window)
        self.button_frame.pack()


        # variables for check buttons

        self.v1 = tkinter.IntVar()
        self.v1.set(0)
        self.v2 = tkinter.IntVar()
        self.v2.set(0)
        self.v3 = tkinter.IntVar()
        self.v3.set(0)
        self.v4 = tkinter.IntVar()
        self.v4.set(0)
        self.v5 = tkinter.IntVar()
        self.v5.set(0)
        self.v6 = tkinter.IntVar()
        self.v6.set(0)
        self.v7 = tkinter.IntVar()
        self.v7.set(0)


        # check button frame elements

        self.cb1 = tkinter.Checkbutton(
            self.check_button_frame,
            text='Замена масла = $30.00',
            variable=self.v1
            )
        self.cb1.pack()

        self.cb2 = tkinter.Checkbutton(
            self.check_button_frame,
            text='Смазочные работы - $20.00',
            variable=self.v2
            )
        self.cb2.pack()

        self.cb3 = tkinter.Checkbutton(
            self.check_button_frame,
            text='Промывка радиатора - $40.00',
            variable=self.v3
            )
        self.cb3.pack()

        self.cb4 = tkinter.Checkbutton(
            self.check_button_frame,
            text='Замена жидкости в трансмиссии - $100.00',
            variable=self.v4
            )
        self.cb4.pack()

        self.cb5 = tkinter.Checkbutton(
            self.check_button_frame,
            text='Осмотр - $35.00',
            variable=self.v5
            )
        self.cb5.pack()

        self.cb6 = tkinter.Checkbutton(
            self.check_button_frame,
            text='Замена глушителя выхлопа - $200.00',
            variable=self.v6
            )
        self.cb6.pack()

        self.cb7 = tkinter.Checkbutton(
            self.check_button_frame,
            text='Перестановка шин - $20.00',
            variable=self.v7
            )
        self.cb7.pack()


        # button frame elements

        self.view_cost_button = tkinter.Button(
            self.button_frame,
            text='Показать стоимость',
            command=self.eval
            )
        self.view_cost_button.pack(side='left')
        
        self.quit_button = tkinter.Button(
            self.button_frame,
            text='Выйти',
            command=self.window.destroy
            )
        self.quit_button.pack(side='left')


        tkinter.mainloop()
        

    def eval(self):

        self.message = 'Ваши затраты = $'
        self.message = self.message + str(30*self.v1.get() + 20*self.v2.get() + 40*self.v3.get() + 100*self.v4.get() + 35*self.v5.get() + 200*self.v6.get() + 20*self.v7.get())

        tkinter.messagebox.showinfo('Общая стоимость', self.message)


t = My_GUI()
