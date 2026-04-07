from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(400,400)

miles_inputField=Entry(window,width=10)
miles_inputField.grid(row=1,column=8)

miles_Label=Label(text="Miles")
miles_Label.grid(row=1,column=9)

miles_Label=Label(text="is Equal to")
miles_Label.grid(row=2,column=2)

km_inputField=Entry(window,width=10)
km_inputField.grid(row=2,column=8)

miles_Label=Label(text="Km")
miles_Label.grid(row=2,column=9)

def calculate():
    miles=float(miles_inputField.get())
    km=miles*1.6
    km_inputField.insert(END, string=f"{km}")

button=Button(text="Calculate",command=calculate)
button.grid(row=3,column=8)


window.mainloop()

