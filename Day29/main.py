import tkinter

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

image = tkinter.PhotoImage(file="./logo.png")
label = tkinter.Label(window, image=image)
label.pack()

window.mainloop()
