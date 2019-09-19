import tkinter

class MyGUI:

    def __init__(self):
        
        self.window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.window)
        self.top_frame.pack()

        self.bottom_frame = tkinter.Frame(self.window)
        self.bottom_frame.pack()

        self.text1 = tkinter.StringVar()    
        self.text2 = tkinter.StringVar()
        self.text3 = tkinter.StringVar()
            
        self.label1 = tkinter.Label(self.top_frame,textvariable=self.text1)
        self.label1.pack()

        self.label2 = tkinter.Label(self.top_frame,textvariable=self.text2)
        self.label2.pack()

        self.label3 = tkinter.Label(self.top_frame,textvariable=self.text3)
        self.label3.pack()


        self.button = tkinter.Button(
            self.bottom_frame,
            text='Показать инфо',
            command=self.info)
        self.button.pack(side='left'
                         )

        self.quit_button = tkinter.Button(
            self.bottom_frame,
            text='Выйти',
            command=self.window.destroy
            )
        self.quit_button.pack(side='left')
        
        tkinter.mainloop()

    def info(self):

        self.text1.set('Стивен Маркус')
        self.text2.set('274 Бейли')
        self.text3.set('Уэйнзвиль, Северная Каролина 27999')

t = MyGUI()
