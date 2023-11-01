from tkinter import *
root = Tk()
root.title("Pakistan Flag")

# Create a canvas widget
canvas = Canvas(root, width=700, height=450)
canvas.pack()

# Draw the green rectangle
can=canvas.create_rectangle(15, 12, 400, 240,fill="green")

# Draw the white rectangle
canvas.create_rectangle(100,240, 15, 12, fill="white")

# Draw the white crescent
canvas.create_arc(150, 50, 290, 190, start=50, extent=260,outline="white",style=ARC )
canvas.create_arc(180, 60, 290, 180, start=50, extent=260,outline="white",style=ARC )

# Draw the white star
id=canvas.create_polygon(195, 60, 203, 85, 230, 85, 207, 100, 215, 125, 195, 110, 175, 125, 183, 100, 160, 85, 187, 85, fill="white", outline="green")
canvas.moveto(id, 200, 80)  #to fix position 
#create line 
canvas.create_line(19, 240, 19, 500,fill="#231709",width=8)
canvas.create_line(18, 430, 18, 800,fill="#231709",width=20)

#text 
text=Label(canvas,text="Happy-Independence-Day",fg="green",font=("ROMAN","22","bold")).place(x=85,y=350)
#image attechement
bg= PhotoImage(file="img.png")
text = Label(canvas,image=bg).place(x=400, y=320)

# emo= PhotoImage(file="emo.png")
# text = Label(canvas,image=emo).place(x=525, y=320)
#label creation
root.mainloop()