from tkinter import *
from tkinter.ttk import Combobox         #USED FOR COMBOBOX 
from tkinter import messagebox
window = Tk()
window.geometry("450x300")

#image attached
bg= PhotoImage(file="image.png")
text = Label(window,image=bg).place(x=0, y=0)

#label creation
text = Label(window,text = "Choose any 2 favourite colors!",foreground="black",font=("cambria",12)).place(x = 60,y = 10)
fav_clr_1 = Label(window,text = "1st color ",foreground="green",font=("cambria",10,"bold")).place(x = 40,y = 70)
fav_cle_2 = Label(window,text = "2nd color ",foreground="red",font=("cambria",10,"bold")).place(x = 40,y = 100)

#values for combobox
fav_colors = ["black", "Green", "Blue", "Yellow", "Orange", "Purple"]  # List of available colors

#combobox creation
fav_clr_1 = Combobox(window,values=fav_colors,font=("cambria",10,"bold")).place(x = 120,y = 70)
fav_clr_1 = Combobox(window,values=fav_colors,font=("cambria",10,"bold")).place(x = 120,y = 100)
  
#function for messsagebox using showinfo ()
def display():
#messsagebox
    messagebox.showinfo("message", "Thanks :) ")

#submit button
submit_button = Button(window,text = "Submit",background="orange",font=("cambria",10,"bold"),command=display).place(x = 180,y = 190)

window.mainloop()
