from tkinter import *

m = Tk()
w = Canvas(m, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()

m.mainloop()  # infinite loop that waits for events to happen
