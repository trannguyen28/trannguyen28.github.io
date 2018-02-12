from tkinter import *
import tkinter.messagebox

root = Tk()

# **************Popup**************
'''
tkinter.messagebox.showinfo('Welcome!', 'Answer this question to enter the system.')

answer = tkinter.messagebox.askquestion('Question', '1 + 1 = 2?')

if answer == 'yes':
    tkinter.messagebox.showinfo('Congratulations!', 'You have succeeded entering the system.')

elif answer == 'no':
    tkinter.messagebox.showinfo('...', 'Really?')
'''

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red", command = create_window)
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


class BerryButtons:
    
    def __init__(self, master):
        self.button1 = Button(topFrame, text="Button 1", fg="red", command = self.create_window)
        self.button1.pack(side=LEFT)
        photo = PhotoImage(file="ml.png")
        label = Label(root, image=photo)
        label.pack()
        
def create_window(seft, master):
        window = Toplevel (root)
        
b = create_window(root)
'''    
class BerryButtons:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Smiley", command=self.smiley)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def smiley(master):
        photo = PhotoImage(file="ml.png")
        label = Label(frame, image=photo)
        label.pack()
        
    def printMessage(self):
        print("Wow~")

b = BerryButtons(root)

def create_window():
    window = Toplevel (root)
'''
'''
photo = PhotoImage(file="ml.png")
label = Label(root, image=photo)
label.pack()
'''
root.mainloop()

