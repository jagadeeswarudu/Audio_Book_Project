from tkinter import *
import PyPDF3
import pyttsx3
mw=Tk()
mw.title('Audiook')
photo=PhotoImage(file='AudioBook.png')
mw.wm_iconphoto(False, photo)
mw.configure(background='#78965f')
mw.geometry("400x430")
reader=pyttsx3.init()
rate = reader.getProperty('rate')
reader.setProperty('rate',110)
voices = reader.getProperty('voices')
p1=Label(mw,text='Select :\n            Male voice or Female voice           ',font="50",fg='black',bg='#34ebd8')
p1.pack()
p1.grid(row=0,column=0,pady=5,columnspan=2)
btn0=Button(mw,text=' Male voice ',bg='black',fg='yellow',command=lambda:m_or_f(0))
btn1=Button(mw,text=' Female voice ',bg='black',fg='yellow',command=lambda:m_or_f(1))
btn0.grid(row=1,column=0,padx=50,pady=20)
btn1.grid(row=1,column=1,pady=20,sticky=W)
p2=Label(mw,text='Enter book name : ',font=('Arial',10),fg='blue',bg='#78965f')
p2.grid(row=2,column=0,padx=8,sticky=W)
p3=Label(mw,text='Enter page number : ',font=('Arial',10),fg='blue',bg='#78965f')
p3.grid(row=4,column=0,padx=8,sticky=W)
input1=Entry(mw,width=18,font=('Arial',28),justify=LEFT,bg='#5d5e5c')
input1.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
input2=Entry(mw,width=18,font=('Arial',28),justify=LEFT,bg='#5d5e5c')
input2.grid(row=5,column=0,columnspan=2,padx=10,pady=10)
btn3=Button(mw,text=' OK ',bg='black',fg='yellow',command=lambda:f_name())
btn3.grid(row=6,column=0,columnspan=2)
btn4=Button(mw,text='            \nSTOP READING\n            ',bg='pink',fg='red',command=lambda:close)
btn4.grid(row=7,column=0,pady=20,columnspan=2)
def close():
    mw.quit()
reader=pyttsx3.init()
rate = reader.getProperty('rate')
reader.setProperty('rate',110)
voices = reader.getProperty('voices')
s=False
def m_or_f(v):
    reader.setProperty('voice', voices[v].id)
    read('Welcome to Audiook')
    read('Enter book name')
    read('Enter page number')
def read(txt):
    reader.say(txt)
    reader.runAndWait()
def f_name():
    file_name=input1.get()
    pdf_book=open(file_name+'.pdf','rb')
    pdfReader=PyPDF3.PdfFileReader(pdf_book)
    pages=pdfReader.numPages
    n=int(input2.get())
    n=n-1
    for i in range(n,pages+1):
        read('Now Reading page')
        p=i+1
        read(p)
        page=pdfReader.getPage(i)
        text=page.extractText()
        text=text.replace('\n','')
        read(text)
mw.mainloop()





