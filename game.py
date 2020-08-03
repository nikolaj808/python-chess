from board import *
from tkinter import *

root = Tk()
root.configure(background='black')
root.title('Chess')

Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=1)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=2)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=3)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=4)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=5)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=6)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=7)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=1, column=8)

Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=1)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=2)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=3)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=4)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=5)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=6)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=7)
Button(root, bg='white', fg='white', bd=0, relief='ridge', highlightthickness=0).grid(row=2, column=8)

root.mainloop()