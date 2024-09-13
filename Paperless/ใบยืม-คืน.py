from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry #ปฏิทิน
from datetime import datetime #จัดการวันเวลา
import csv

# สร้าง windows
GUI = Tk()
GUI.geometry('600x800')
GUI.title('แบบฟอร์มยืม-คืนอุปกรณ์')

# สร้างกรอบ และขยายให้เต็มกรอบทุกด้าน และใช้ grid แทน pack
main_frame = ttk.Frame(GUI, padding='10')
main_frame.grid(row=0, column=0, sticky=(N,W,E,S))

# กำหนดให้ row + column ยืดหดออโต้
GUI.columnconfigure(0, weight=1)
GUI.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# หัวข้อ
ttk.Label(main_frame, text='แบบฟอร์มยืม/คืน อุปกรณ์', font=('LilyUPC', 25, 'bold')).grid(column=0, row=0, columnspan=2, pady=10)

# ส่วนที่ 1: ข้อมูลทั่วไป
ttk.Label(main_frame, text='ส่วนที่ 1 : ข้อมูลทั่วไป', font=('LilyUPC', 20, 'bold')).grid(column=0, row=1, columnspan=2, sticky=W, pady=10)

# DateEntry ในการเลือกเวลา
v_date = StringVar()
ttk.Label(main_frame, text='วันที่:', font=('LilyUPC', 18)).grid(column=0, row=2, sticky=W, pady=5)
DateEntry(main_frame, textvariable=v_date, font=('LilyUPC', 16), date_pattern='dd/mm/yyyy').grid(column=1, row=2, sticky=W, pady=5)

v_name_th = StringVar()
ttk.Label(main_frame, text='ชื่อ - นามสกุล (ไทย):', font=('LilyUPC', 18)).grid(column=0, row=3, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_name_th, font=('LilyUPC', 16)).grid(column=1, row=3, sticky=(W,E), pady=5)

v_name_en = StringVar()
ttk.Label(main_frame, text='ชื่อ - นามสกุล (Eng):', font=('LilyUPC', 18)).grid(column=0, row=4, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_name_en, font=('LilyUPC', 16)).grid(column=1, row=4, sticky=(W,E), pady=5)

v_emp_id = StringVar()
ttk.Label(main_frame, text='รหัสพนักงาน:', font=('LilyUPC', 18)).grid(column=0, row=5, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_emp_id, font=('LilyUPC', 16)).grid(column=1, row=5, sticky=(W,E), pady=5)

v_department = StringVar()
ttk.Label(main_frame, text='ฝ่าย:', font=('LilyUPC', 18)).grid(column=0, row=6, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_department, font=('LilyUPC', 16)).grid(column=1, row=6, sticky=(W,E), pady=5)

v_section = StringVar()
ttk.Label(main_frame, text='แผนก:', font=('LilyUPC', 18)).grid(column=0, row=7, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_section, font=('LilyUPC', 16)).grid(column=1, row=7, sticky=(W,E), pady=5)

v_email = StringVar()
ttk.Label(main_frame, text='อีเมล์:', font=('LilyUPC', 18)).grid(column=0, row=8, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_email, font=('LilyUPC', 16)).grid(column=1, row=8, sticky=(W,E), pady=5)

v_tel = StringVar()
ttk.Label(main_frame, text='เบอร์โทร:', font=('LilyUPC', 18)).grid(column=0, row=9, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_tel, font=('LilyUPC', 16)).grid(column=1, row=9, sticky=(W,E), pady=5)

# ส่วนที่ 2: รายละเอียด
ttk.Label(main_frame, text='ส่วนที่ 2 : รายละเอียด', font=('LilyUPC', 20, 'bold')).grid(column=0, row=10, columnspan=2, sticky=W, pady=10)

v_asset = StringVar()
ttk.Label(main_frame, text='ชื่อวัสดุ/อุปกรณ์:', font=('LilyUPC', 18)).grid(column=0, row=11, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_asset, font=('LilyUPC', 16)).grid(column=1, row=11, sticky=(W,E), pady=5)

v_purpose = StringVar()
ttk.Label(main_frame, text='ต้องการจะขอยืมวัสดุ/อุปกรณ์เพื่อ:', font=('LilyUPC', 18)).grid(column=0, row=12, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_purpose, font=('LilyUPC', 16)).grid(column=1, row=12, sticky=(W,E), pady=5)

v_location = StringVar()
ttk.Label(main_frame, text='สถานที่ใช้งาน:', font=('LilyUPC', 18)).grid(column=0, row=13, sticky=W, pady=5)
ttk.Entry(main_frame, textvariable=v_location, font=('LilyUPC', 16)).grid(column=1, row=13, sticky=(W,E), pady=5)

v_start_date = StringVar()
ttk.Label(main_frame, text='ตั้งแต่วันที่:', font=('LilyUPC', 18)).grid(column=0, row=14, sticky=W, pady=5)
DateEntry(main_frame, textvariable=v_start_date, font=('LilyUPC', 16), date_pattern='dd/mm/yyyy').grid(column=1, row=14, sticky=W, pady=5)

v_end_date = StringVar()
ttk.Label(main_frame, text='ถึงวันที่:', font=('LilyUPC', 18)).grid(column=0, row=15, sticky=W, pady=5)
DateEntry(main_frame, textvariable=v_end_date, font=('LilyUPC', 16), date_pattern='dd/mm/yyyy').grid(column=1, row=15, sticky=W, pady=5)

# Combobox สำหรับเลือกประเภทเอกสาร หาวิธีแยกประเภทเอกสาร
v_doc_type = StringVar(value="ยืม")  # ค่าเริ่มต้นเป็น "ยืม"
ttk.Label(main_frame, text='ประเภทเอกสาร:', font=('LilyUPC', 18)).grid(column=0, row=16, sticky=W, pady=5)
doc_type_combo = ttk.Combobox(main_frame, textvariable=v_doc_type, values=["ยืม", "คืน"], font=('LilyUPC', 16), state="readonly")
doc_type_combo.grid(column=1, row=16, sticky=(W,E), pady=5)
doc_type_combo.current(0)  # เลือก "ยืม" เป็นค่าเริ่มต้น

def writetocsv(data):
    with open('24CSITF07_data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

def Save():
    data = [v_doc_type.get(),v_date.get(), v_name_th.get(), v_name_en.get(), v_emp_id.get(),v_department.get(), v_section.get(), v_email.get(), v_tel.get(),v_asset.get(),v_purpose.get(), v_location.get(), v_start_date.get(), v_end_date.get()]
    writetocsv(data)
    print("บันทึกข้อมูลเรียบร้อยแล้ว")
    # เคลียร์ข้อมูลในฟอร์ม
    for var in [v_name_th, v_name_en, v_emp_id, v_department, v_section, v_email, v_tel, v_asset, v_purpose, v_location]:
        var.set('')
    v_date.set(datetime.now().strftime('%d/%m/%Y'))
    v_start_date.set(datetime.now().strftime('%d/%m/%Y'))
    v_end_date.set(datetime.now().strftime('%d/%m/%Y'))
    v_doc_type.set('ยืม')

ttk.Button(main_frame, text='บันทึก', command=Save).grid(column=1, row=17, sticky=E, pady=20, padx=10)




GUI.mainloop()