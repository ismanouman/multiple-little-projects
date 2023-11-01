from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

def create_table():
    con = sqlite3.connect("S_M_S.db")  # Connect to the SQLite database file
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                    ID INTEGER PRIMARY KEY,
                    Name TEXT,
                    Contact INTEGERS,
                    Email TEXT,
                    Gender TEXT,
                    Course TEXT,
                    DOB INTEGERS,
                    Address TEXT,
                    Tutor TEXT)""")
    
    con.commit()
    con.close()
create_table()

def add_students():
    # ... existing code ...
    con = sqlite3.connect("S_M_S.db")  # Connect to an SQLite database file
    cur = con.cursor()

    cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (id_entry.get(),
                 name_strvar.get(),
                 contact_entry.get(),
                 email_strvar.get(),
                 gender_strvar.get(),
                 course_strvar.get(),
                 dob_entry.get(),
                 address_strvar.get(),
                 tutor_strvar.get()))

    con.commit()
    con.close()
    fetch_data()

def fetch_data():
    con = sqlite3.connect("S_M_S.db")  # Connect to the same SQLite database file
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert('', END, values=row)

    con.close() 

def get_cursor(event):
    cursor_row = tree.focus()
    contents = tree.item(cursor_row)
    row = contents['values']
    
    id_entry.set(row[0])
    name_strvar.set(row[1])
    contact_entry.set(row[2])
    email_strvar.set(row[3])
    gender_strvar.set(row[4])
    dob_entry.set(row[5])
    address_strvar.set( row[6])
    tutor_strvar.set(END,row[7])

def clear_all_data():
    tree.delete(*tree.get_children())

def clear():
    id_entry.delete(0, END)
    name_strvar.set("")
    contact_entry.delete(0, END)
    email_strvar.set("")
    gender_strvar.set("")
    course_strvar.set("")
    dob_entry.delete(0, END)
    address_strvar.set("")
    tutor_strvar.set("")

def update_data():
    con = sqlite3.connect("S_M_S.db")  # Connect to the same SQLite database file
    cur = con.cursor()
    cur.execute("UPDATE students SET name=?, email=?, gender=?, contact=?, dob=?, address=?, tutor=? WHERE ID=?", (
        name_strvar.get(),
        email_strvar.get(),
        gender_strvar.get(),
        contact_entry.get(),
        dob_entry.get(),
        address_strvar.get(),
        tutor_strvar.get(),
        id_entry.get()
    ))

    con.commit()
    con.close()
    fetch_data()
    clear()
    
def delete_data():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
        
        # Also delete the record from the database
        con = sqlite3.connect("S_M_S.db")
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE ID=?", (id_entry.get(),))
        con.commit()
        con.close()
    else:
        messagebox.showwarning("Warning", "Please select a record to delete.")





main = Tk()
main.title('School Management System')
main.geometry("1000x600")

color1 = 'lightpink' 
color2 = 'purple' 

name_strvar = StringVar()
email_strvar = StringVar()
gender_strvar = StringVar()
course_strvar = StringVar()
address_strvar= StringVar()
tutor_strvar = StringVar()


Label(main, text="SCHOOL MANAGEMENT SYSTEM",fg="white", font="cambria", bg='purple').grid(row=1, column=2,pady=8)
#label frame
left_frame = LabelFrame(main, bg=color1)
left_frame.place(x=0.2, y=40, relheight=1, relwidth=0.35)

Label(left_frame, text="Student_ID", font="cambria", bg=color1).grid(row=1, column=0,sticky=W,pady=2)
Label(left_frame, text="Name", font="cambria", bg=color1).grid(row=2, column=0,sticky=W,pady=2)
Label(left_frame, text="Contact Number", font="cambria", bg=color1).grid(row=3, column=0,sticky=W,pady=2)
Label(left_frame, text="Email Address", font="cambria", bg=color1).grid(row=4, column=0,sticky=W,pady=2)
Label(left_frame, text="Course", font="cambria", bg=color1).grid(row=5, column=0,sticky=W,pady=2)
Label(left_frame, text="Date-of-Birth", font="cambria", bg=color1).grid(row=6, column=0,sticky=W,pady=2)
Label(left_frame, text="Gender", font="cambria", bg=color1).grid(row=7, column=0,sticky=W,pady=2)
Label(left_frame, text="Adress", font="cambria", bg=color1).grid(row=8, column=0,sticky=W,pady=2)
Label(left_frame, text="Tutor", font="cambria", bg=color1).grid(row=9, column=0,sticky=W,pady=2)

id_entry = Entry(left_frame, font=("cambria", 12), width=15)
id_entry.grid(row=1, column=1, sticky=W, pady=2)
Entry(left_frame, width=19, textvariable=name_strvar, font="cambria").grid(row=2, column=1,sticky=W,pady=2)
Entry(left_frame, width=19, textvariable=email_strvar, font="cambria").grid(row=4, column=1,sticky=W,pady=2)
Entry(left_frame, width=19, textvariable=course_strvar, font="cambria").grid(row=5, column=1,sticky=W,pady=2)
contact_entry=Entry(left_frame, width=19, font="cambria")
contact_entry.grid(row=3, column=1,sticky=W,pady=2)


dob_entry = Entry(left_frame, font=("cambria", 12), width=15)
dob_entry.grid(row=6, column=1, sticky=W, pady=2)
OptionMenu(left_frame, gender_strvar, 'Male', "Female").grid(row=7, column=1,sticky=W,pady=2)
Entry(left_frame, width=19, textvariable=address_strvar, font="cambria").grid(row=8, column=1,sticky=W,pady=2)
Entry(left_frame, width=19, textvariable=tutor_strvar, font="cambria").grid(row=9, column=1,sticky=W,pady=2)

# Button(left_frame, text='Submit',bg="purple",fg="white" ,font="cambria", width=8).grid(row=10, column=1,sticky=W,pady=2)

#button frame
btn_Frame = Frame(main, bd=3, relief=RIDGE, bg="white")
btn_Frame.place(x=15, y=500, width=300)
Addbtn = Button(btn_Frame,text="Add",font=("cambria","10","bold"),command=add_students ,width=12,bg="purple",fg="white").grid(row=0,column=1,padx=23,pady=10)
updatebtn = Button(btn_Frame, text="Update",font=("cambria","10","bold"),command=update_data , width=12,bg="purple",fg="white").grid(row=0, column=2, padx=10, pady=10)
deletebtn = Button(btn_Frame, text="Delete",font=("cambria","10","bold"),command=delete_data, width=12,bg="purple",fg="white").grid(row=1, column=1, padx=10, pady=10)
Clearbtn = Button(btn_Frame, text="Clear",font=("cambria","10","bold"),command=clear_all_data, width=12,bg="purple",fg="white").grid(row=1, column=2, padx=10, pady=10)

# database frame
right_frame = Frame(main, bg="white")
right_frame.place(relx=0.36, y=10, relheight=1, relwidth=0.63)

Label(right_frame, text='Students Records', font="cambria", bg='purple', fg='white').grid(row=1, column=12, sticky='ew')

tree = ttk.Treeview(right_frame, height=100, selectmode="browse",
                    columns=('Student ID', "Name", "Contact Number","Email Address", "Gender","Course", "Date-of-Birth", "Adress", "Tutor"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Contact Number', text='Contact', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Course', text='Course', anchor=CENTER)
tree.heading('Date-of-Birth', text='D-O-B', anchor=CENTER)
tree.heading('Tutor', text='Tutor', anchor=CENTER)
tree.heading('Adress', text='Adress', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=70, stretch=NO)
tree.column('#2', width=90, stretch=NO)
tree.column('#3', width=100, stretch=NO)
tree.column('#4', width=130, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.column('#6', width=80, stretch=NO)
tree.column('#7', width=100, stretch=NO)
tree.column('#8', width=120, stretch=NO)
tree.column('#9', width=120, stretch=NO)

tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
fetch_data()
main.mainloop()








# figd_Q3dqmG4dcE5b4kAip7YYGPjsMvFTOLNm6I1lW4AZ