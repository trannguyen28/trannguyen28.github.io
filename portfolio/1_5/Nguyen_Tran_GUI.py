from tkinter import *
import tkinter.messagebox

root = Tk()



# **************Window**************

class Buttons:
    
    def __init__(self, master):

        label = Label(master, text="Pick one to see how your day will be.")
        label.pack()
        
        frame = Frame(master)      # Frame for buttons
        frame.pack()

        self.button1 = Button(frame, text="Option 1", fg="green", command=self.Button1)   # When pressed, Button1 will be called
        self.button1.pack(side=LEFT)

        self.button2 = Button(frame, text="Option 2", fg="red", command=self.Button2)   # When pressed, Button2 will be called
        self.button2.pack(side=LEFT)

        self.button3 = Button(frame, text="Option 3", fg="blue", command=self.Button3)   # When pressed, Button3 will be called
        self.button3.pack(side=LEFT)

        self.button4 = Button(frame, text="Option 4", fg="orange", command=self.Button4)   # When pressed, Button4 will be called
        self.button4.pack(side=LEFT)

    def Button1(self):
        print("Your day will be great. (ﾉ◕ヮ◕)ﾉ*")

    def Button2(self):
        print("Your day will be awesome. ✧◝(⁰▿⁰)◜✧")

    def Button3(self):
        print("Your day will be fantastic. ♥(ˆ⌣ˆԅ)") 

    def Button4(self):
        print("Your day will be wonderful. (❁´▽`❁)")



# **************Window**************

tkinter.messagebox.showinfo('Welcome!', 'Answer this question to enter the system.')   # Pop up when GUI runs

answer = tkinter.messagebox.askquestion('Question', '1 + 1 = 2?')

if answer == 'yes':
    tkinter.messagebox.showinfo('Suceeded', 'You have successfully entered the system.')   # Answer correct -> Enter
    b = Buttons(root)

elif answer == 'no':
    tkinter.messagebox.showinfo('Failed', 'You have not succeeded entering the system.')   # Answer incorrect -> Exit


    
root.mainloop()

