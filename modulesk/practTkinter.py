from tkinter import Tk, Label, Message

# for i in dir(Tk):
#     if( i.startswith('_') == True ):
#         continue
#     print(i, end=", ")

root = Tk()
root.title("Hello Py Gui")


# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# print(width, height)

# root.attributes('-fullscreen', True)

# root.geometry('400x400+150+0')

# # text on screen
# txt = "First GUi"
# lb = Label(root, text=txt)
# lb.pack()

# | font change of txt
txt = "This is a sample txt from py."
lb = Label(root, text=txt)
lb.config(font=('arial', 32, 'bold italic underline'))

lb.pack()


root.mainloop()