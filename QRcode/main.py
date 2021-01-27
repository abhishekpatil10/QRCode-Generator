import tkinter
import pyqrcode
from tkinter import *
from PIL import ImageTk, Image
import png

from qrcode import QRCode
root=tkinter.Tk()
root.geometry("400x400")
root.resizable(width=0,height=0)
root.title('BarCode')
root.iconbitmap(r'icon.ico')

lb=Label(root,text="Enter Your text and get QRCode",bg='#900C3F',font=('bold'),height=2,width=100)
lb.pack()

def load():
    global lb1,lb2
    text = lb1.get()
    qr = pyqrcode.create(text)
    a = qr.svg('scn.svg',scale=8)
    b = qr.png('scn.png',scale=6)
    lb3['text']='QR Generated Successfully'
    
    
    
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(root) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("BarCode") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("600x600") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="This is a new window").pack()
    photo=r'scn.png'
    root.photo = ImageTk.PhotoImage(Image.open(photo))
    lb4 = Label(newWindow,image=root.photo,height=400,width=500)
    lb4.pack(padx=50)
  
    
    
    
  

lb1=Entry(root,text='',font=(24))
lb1.place(x=50,y=50,width=300,height=50)
btn = Button(root,text="GET QR code",command=load)
btn.pack(pady=70)
lb3 = Label(root,text='')
lb3.pack()
photo=r'C:\Users\abhis\OneDrive\Desktop\music\match-finder\icon1.ico'
root.photo = ImageTk.PhotoImage(Image.open(photo))
btn1 = Button(root,text='Check QR code',command=openNewWindow)
btn1.pack()
lb2 = Label(root,image=root.photo,height=250,width=250)
lb2.pack(padx=50)
root.mainloop()
