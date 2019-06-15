from tkinter import *

#gui를 통한 간단한 창 만들어봄

def printHello():
    print('hi')

root=Tk()

w=Label(root,text="Python Test")
b=Button(root,text="HEllo Python", command=printHello)
c=Button(root,text="Quit", command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()