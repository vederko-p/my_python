import tkinter
import time
import tkinter.messagebox

class clocks():


    def __init__(self):


        # frames
        
        self.main_window = tkinter.Tk()
        self.main_window.title("Будильник")
        self.main_window.geometry('400x180')
          
        self.time_frame = tkinter.Frame(
            self.main_window,
            width=300, height=130,
            background="#4A036F"
            )
         self.time_frame.place(x=50, y=30)
        
        self.buttons_frame = tkinter.Frame(
            self.main_window,
            width=300, height=30,
            background="#4A036F"
            )
        self.buttons_frame.place(x=50, y=120)
  

        # variables

        self.global_time = tkinter.IntVar()
        self.global_time.set(
            int(time.strftime('%H')) * 3600 +
            int(time.strftime('%M')) * 60 +
            int(time.strftime('%S'))
            )

        self.label_time = tkinter.StringVar()
        self.label_time.set('00:00')

        self.alarm_time = tkinter.IntVar()
        self.alarm_time.set(51300)

        self.alarm_switch = tkinter.IntVar()
        self.alarm_switch.set(0)
        

        # time_frame elelemnts

        self.showing_time_label = tkinter.Label(
            self.time_frame,
            textvariable=self.label_time,
            font=('Pixel Cyr', 40),
            bg='#4A036F',
            fg='white'
            )
        self.showing_time_label.place(x=75, y=20)


        # buttons_frame elements

        self.h_button = tkinter.Button(
            self.buttons_frame,
            command=self.h_plus,
            text="H",
            width=5,
            bg='#4512AE',
            fg='white'
            )
        self.h_button.place(x=40, y=2)

        self.m_button = tkinter.Button(
            self.buttons_frame, 
            command=self.m_plus,
            text="M",
            width=5,
            bg='#4512AE',
            fg='white'
            )
        self.m_button.place(x=140, y=1)
        
        self.a_button = tkinter.Button(
            self.buttons_frame,
            command=self.alarm,
            text="A",
            width=5,
            bg='#4512AE',
            fg='white'
            )
        self.a_button.place(x=240, y=1)
       

        self.showing_time_label.after_idle(self.ttime)
        
        tkinter.mainloop()


    # methods

    def ttime(self):

        if self.alarm_switch.get() == 0 and self.global_time.get() == self.alarm_time.get():
            tkinter.messagebox.showinfo('Будильник!', 'Будильник!')
        
        self.showing_time_label.after(1000,self.ttime)
        self.global_time.set((self.global_time.get() + 1) % 86400)
        
        if self.alarm_switch.get() == 0:
            
            self.label_time.set(
                '{0:0=2d}:{1:0=2d}'.format(
                    self.global_time.get() // 3600%24,
                    self.global_time.get() // 60%60
                    )
                )
        else:
            self.label_time.set(
                '{0:0=2d}:{1:0=2d}'.format(
                    self.alarm_time.get() // 3600%24,
                    self.alarm_time.get() // 60%60
                    )
                )


    def h_plus(self):
        
        if self.alarm_switch.get() == 0:
            self.global_time.set(self.global_time.get() + 3600)
        else:
            self.alarm_time.set((self.alarm_time.get() + 3600) % 86400)


    def m_plus(self):
        
        if self.alarm_switch.get() == 0:
            self.global_time.set(self.global_time.get() + 60)
        else:
            self.alarm_time.set((self.alarm_time.get() + 60) % 86400)


    def alarm(self):
        
        if self.alarm_switch.get() == 0:
            self.alarm_switch.set(1)
        else:
            self.alarm_switch.set(0)


t = clocks()
