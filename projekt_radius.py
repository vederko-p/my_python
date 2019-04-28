import tkinter
from math import pi

def volume():
  
    try:
        if radius.get() >= 0:
            result.set(round(4/3*pi*(radius.get()**3), 3))
        else:
            result.set('Радиус меньше нуля')
    except:
        result.set("Введите число")

def writer_txt():
    try:
        with open('results.txt','a') as file:
            file.write('Радиус: '+str(radius.get())+' Объем: '+str(result.get())+'\n')
        status.set('Файл перезаписан')
            
    except:
       status.set('Файл не перезаписан')
       
def writer_html():
    try:
        with open('results.html','a') as file:
            file.write('Радиус: '+str(radius.get())+' Объем: '+str(result.get())+'\n')
        status.set('Файл перезаписан')
            
    except:
       status.set('Файл не перезаписан')
       
def writer():
    try:
        if where.get()!='HTML':
            writer_txt()
        else:
            writer_html()
    except:
        status.set('Файл не перезаписан')


                                            
window = tkinter.Tk()
frame=tkinter.Frame(window)
frame.grid(column=0, row=0)

window.title("Программа для вычесления объёма сферы")  
window.geometry('400x400')

lbl = tkinter.Label(frame, text="Введите радиус")  
lbl.grid(column=0, row=0)

radius = tkinter.DoubleVar()

status = tkinter.StringVar()

lbl_entry = tkinter.Entry(frame,textvariable=radius)  
lbl_entry.grid(column=1, row=0)

result_name = tkinter.Label(frame, text='Результат\nвычислений:')
result_name.grid(row=1, column=0)

result = tkinter.DoubleVar()
result_number = tkinter.Label(frame, textvariable=result)
result_number.grid(row=1, column=1)

button_frame = tkinter.Frame(frame)
button_frame.grid(row=1, column=0)

button1=tkinter.Button(frame,text="Вычислить",command=volume)
button1.grid(column=0, row=2)

button_save = tkinter.Button(frame,text='Сохранить',command=writer)
button_save.grid(row=2, column=1)

status_n = tkinter.Label(frame, textvariable=status)
status_n.grid(row=3, column=1)

where = tkinter.StringVar()
where.set('Teкст')
save_option = tkinter.OptionMenu(frame, where, 'Текст', 'HTML')
save_option.grid(row=2, column=2)


window.mainloop()  
