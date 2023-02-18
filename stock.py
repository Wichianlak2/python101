from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI=Tk()#นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมตรวจสต๊อกสินค้า')#นี่คือชื่อของบโปรแกรม
GUI.geometry('750x400')#นี่คือขนาดของโปรแกรม

L1 = Label(GUI,text='โปรแกรมตรวจสต๊อกสินค้า',font=('Angsana New',30),fg='green')
L1.place(x=50,y=20)
L1.pack(ipadx=20,ipady=20)


#####################
def Button2():
    text = 'ตอนนี้มีปูนอย่ในสต๊อก 5 ตัน'
    messagebox.showinfo('ปูนซีเมนต์ในสต๊อก',text)

FB1 = LabelFrame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='ปูนซีเมนต์ในสต๊อก',command=Button2)#B2.pack(ipadx=20,ipady=20)
B2.pack(ipadx=20,ipady=20,padx=10,pady=10)
###################
def Button3():
    text = 'ตอนนี้มีหินอยู่ในสต๊อก 2 ตัน'
    messagebox.showinfo('หินในสต๊อก',text)

FB2 = LabelFrame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=100)
B3 = ttk.Button(FB1,text='หินในสต๊อก',command=Button3)#B2.pack(ipadx=20,ipady=20)
B3.pack(ipadx=20,ipady=20,padx=10,pady=10)
###################
def Button4():
    text = 'เหล็ก,หิน,ปูน,ทราย'
    messagebox.showinfo('สินค้าที่มี',text)

FB3 = LabelFrame(GUI) #คล้ายกระดาน
FB3.place(x=100,y=200)
B4 = ttk.Button(FB1,text='สินค้าที่มีอยู่ในสต๊อก',command=Button4)#B2.pack(ipadx=50,ipady=50)
B4.pack(ipadx=20,ipady=20,padx=10,pady=10)
###############





GUI.mainloop()
