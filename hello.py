import tkinter

root = tkinter.Tk()
root.geometry("200x200")
root.title("Test window")

picture = tkinter.Canvas(root, width=100,height=100)
picture.create_rectangle(0,0,100,100,fill="green")
picture.place(x=0,y=0)


root.mainloop()