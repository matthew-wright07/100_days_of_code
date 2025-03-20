import tkinter

window = tkinter.Tk()
window.title("Idk man")
window.minsize(500,300)

def handle_calculate():
    miles = miles_input.get()
    km = float(miles) * 1.60934
    km_output.config(text=str(km))


label = tkinter.Label(text="Is Qqual To")
label.grid(row=1,column=0)

miles_input = tkinter.Entry()
miles_input.grid(row=0,column=1)

miles_text = tkinter.Label(text="Miles")
miles_text.grid(row=0,column=2)

km_output = tkinter.Label()
km_output.grid(row=1,column=1)

km_text = tkinter.Label(text="Km")
km_text.grid(row=1,column=2)

calculate = tkinter.Button(text="Calculate",command=handle_calculate)
calculate.grid(row=2,column=1)

window.mainloop()
