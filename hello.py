from distutils.cmd import Command
from itertools import tee
import tkinter


count = 0
check_picture_existeance = False
# id_id

def move():
    pass

class graphic():

    def __init__(self) -> None:
        self.picture = tkinter.Canvas(root, width=100,height=100)
        self.picture.create_rectangle(0,0,100,100,fill="green")
        self.picture.place(x=0,y=0)
        pass

    def checkupdate(self,event):
        global count
        count = count + 100
        self.label = tkinter.Label(text=count)
        self.label.place(x=100,y=100)
        pass

    def checkupdate_revace(self,event):
        global count
        count = count - 100
        self.label1 = tkinter.Label(text=count)
        self.label1.place(x=100,y=100)
        pass


    def movepicture(self):
        global id_id
        # global check_picture_existeance
        
        # if(check_picture_existeance == False):
        #     pass
        # else:
        #     # self.hello.delete(id_id)
        #     pass
        global count
        id_id = self.hello = tkinter.Canvas(root, width=100,height=100)
        self.hello.create_rectangle(0,0,100,100,fill="red")
        self.hello.place(x=count,y=0) 
        # check_picture_existeance = True
        pass

    def delete(self):
        self.hello.delete(id_id)
        pass

root = tkinter.Tk()
root.geometry("500x500")
root.title("Test window")

testclass = graphic()

# root.after(1,testclass.movepicture,)
# testclass.movepicture()
# testclass.checkupdate()

bottun = tkinter.Button(root,text="Increase")
bottun.bind("<ButtonPress>",testclass.checkupdate)
# bottun.bind("<ButtonPress>",testclass.movepicture)
bottun.place(x=200,y=200)

bottun2 = tkinter.Button(root,text="Decrease")
bottun2.bind("<ButtonPress>",testclass.checkupdate_revace)
# bottun2.bind("<ButtonPress>",testclass.movepicture)
bottun2.place(x=200,y=250)

button1 = tkinter.Button(root,text="force update move function",command=lambda:[testclass.movepicture(),testclass.delete()])
button1.bind("<ButtonPress>")
button1.place(x=300,y=200)



root.mainloop()