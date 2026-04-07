from tkinter import *

window=Tk()
window.title("My First GUI Program")
window.minsize(600,600)

my_label=Label(text="Hello",font=("Arial",20))
my_label.pack()

##Button
def button_clicked():
    text = input_field.get()
    my_label["text"]=text

my_button=Button(text="Click me",command=button_clicked)
my_button.pack()

##Input field
input_field=Entry(width=20)
input_field.pack()

##TextBox
textBox=Text(width=40,height=5)
textBox.pack()

##SpinBox
spinBox=Spinbox(width=5)
spinBox.pack()

##Scale
scale=Scale(from_=0,to=20,orient='horizontal')
scale.pack()

##CheckButton
checkBox=Checkbutton(text="Check")
checkBox.pack()

##RadioButton
radioButton=Radiobutton(text="Radio")
radioButton.pack()

##ListBox
listBox=Listbox()
listBox.pack()

window.mainloop()