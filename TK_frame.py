from tkinter import *  
root = Tk()  
colors=['blue','red','yellow','green','white','black','gray','pink']
for i in colors:  
    Frame(height = 20,width = 440,bg = i) .pack()


label = Label(root,text = "Date-of-birth ",foreground="green",font=("cambria",10,"bold")).place(x =640,y = 20)
label2 = Label(root,text = "Date-Month-Year",foreground="red",font=("cambria",10,"bold")).place(x = 635,y = 50)


def display():
    Label(root,text=f'{date.get()}-{month.get()}-{year.get()}',foreground="purple",font=('cambria', 10,"bold")).place(x=660,y=120)
#spinbox creation
date=IntVar()
month=IntVar()
year=IntVar()
#pack() used if we dont use x and y (.place())
sbox=Spinbox(root,textvariable=date,from_="1",to="30",border=3,width='5',command=display).place(x=610,y=80)
sbox=Spinbox(root,textvariable=month,from_="1",to="12",border=3,width='5',command=display).place(x=665,y=80)
sbox=Spinbox(root,textvariable=year,from_="1995",to="2005",border=3,width='5',command=display).place(x=720,y=80)



root.mainloop() 
