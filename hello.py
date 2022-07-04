import tkinter

class graphic():

    def __init__(self) -> None:
        self.picture = tkinter.Canvas(root, width=100,height=100)
        self.picture.create_rectangle(0,0,100,100,fill="green")
        self.picture.place(x=0,y=0)
        pass

root = tkinter.Tk()
root.geometry("200x200")
root.title("Test window")

testclass = graphic()


root.mainloop()