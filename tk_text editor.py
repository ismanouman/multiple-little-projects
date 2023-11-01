from tkinter import *
from tkinter import Menu
root=Tk()
root.title("Text_editor")

#scroolbar
scrollbar=Scrollbar(root).pack(side=RIGHT,fill=Y)
#added text
text=Text(root,font=("cambria",10)).pack(fill=BOTH)
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

         # creating file_menu
file_menu = Menu(menubar,tearoff=0)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(label="Preferences",menu=sub_menu)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)

menubar.add_cascade(label="File",menu=file_menu,underline=0)

           #creating edit menu
edit_menu = Menu(menubar,tearoff=0)

#adding items
edit_menu.add_command(label='copy')
edit_menu.add_command(label='cut')
edit_menu.add_command(label='paste')

menubar.add_cascade(label='Edit',menu=edit_menu,underline=0)
root.mainloop()