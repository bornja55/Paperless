from tkinter import *
from tkinter import ttk
import csv

GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมสมัครงาน')

L = Label(GUI,text='กรอกใบสมัครที่นี่',font=('LilyUPC',25))
L.pack()

L = Label(GUI,text='คุณสมบัติ\n\nอายุไม่เกิน 35 ปี\n-วุฒิ ป.ตรี',font=('LilyUPC',20))
L.pack()

v_fullname = StringVar()
L = Label(GUI,text='\nชื่อ-นามสกุล',font=('LilyUPC',20))
L.pack()
E1 = ttk.Entry(GUI,textvariable=v_fullname,font=('LilyUPC',18))
E1.pack()

v_tel = StringVar()
L = Label(GUI,text='เบอร์โทร',font=('LilyUPC',20))
L.pack()
E2 = ttk.Entry(GUI,textvariable=v_tel,font=('LilyUPC',18))
E2.pack()

v_position = StringVar()
L = Label(GUI,text='ตำแหน่ง',font=('LilyUPC',20))
L.pack()
E3 = ttk.Entry(GUI,textvariable=v_position,font=('LilyUPC',18))
E3.pack()

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


def Save():
    fullname = v_fullname.get()
    tel = v_tel.get()
    position = v_position.get()
    print(fullname,tel,position)
    data = [fullname,tel,position]
    writetocsv(data)
    v_fullname.set('')
    v_tel.set('')
    v_position.set('')


B1 = ttk.Button(GUI,text='ส่ง',command=Save)
B1.pack(pady=20,ipadx=20,ipady=10)

GUI.mainloop()