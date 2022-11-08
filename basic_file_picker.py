from tkinter import *
from tkinter import filedialog as fd

def song_picker():
    filename = fd.askopenfilename()


root = Tk()

root.geometry('150x150')


btn = Button(root, text = 'Select file', bd = '5', command = song_picker)

btn.pack(side = 'top')



root.geometry = ('500x500')


root.mainloop
