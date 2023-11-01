from tkinter import *
window = Tk()
window.geometry("450x300")
window.configure(bg="black")
# the label for ID
student_ID = Label(window,text = "Student_ID ",foreground="blue",font=("cambria",10,"bold")).place(x = 40,y = 60)
# the label for password
password = Label(window,text = "Password ",foreground="blue",font=("cambria",10,"bold")).place(x = 40,y = 100)

submit_button = Button(window,text = "Submit",background="pink",font=("cambria",10,"bold")).place(x = 150,y = 130)

entry_field_1 = Entry(window,width = 20,background="gray").place(x =120,y = 60)

entry_field_2 = Entry(window,width = 20,background="gray").place(x = 120,y = 100)

#scrollbar
scrollbar=Scrollbar(window).pack(side=LEFT,fill=Y)
window.mainloop()
