from distutils.cmd import Command
from itertools import tee
from logging.handlers import RotatingFileHandler
from math import fabs
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

def showcount(number):
    labeltest = tkinter.Label(text=number)
    labeltest.place(x=300,y=300)
    root.after(1000)
    pass

def loop():
    number = 0
    for i in range(10):
        # root.after(1000,showcount(number))
        number = 1 + number
        showcount(number)



def wait():
    # global check_picture_existeance
    global sydw
    # if(check_picture_existeance == False):
    #     sydw = 0
    # else:
    #     pass
    
    # check_picture_existeance = True
    sydw = sydw + 1
    lafdslk = tkinter.Label(text=sydw)
    # lafdslk.after(10000)
    lafdslk.place(x=500,y=500)
    root.after(100,wait)







root = tkinter.Tk()
root.geometry("1000x1000")
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

buttonla = tkinter.Button(root,text="carry out loop function",command=lambda:loop())
buttonla.bind("<ButtonPress>")
buttonla.place(x=400,y=400)


sydw = 0
root.after(10000,wait)


# loop(root)

root.mainloop()


# Tips to move as spending time.
# https://www.school.ctc-g.co.jp/columns/hishinuma/hishinuma28.html
