import tkinter
haupt_fenster = tkinter.Tk()
haupt_fenster.title("THI - WI3 - SWD")

leinwand = tkinter.Canvas(haupt_fenster, width=800, height=450, bg="lightblue")
leinwand.grid(row=0, column=0, rowspan=4, columnspan=2)

label = tkinter.Label(haupt_fenster, text="Meine erste GUI")
label.grid(row=0, column=0)

button = tkinter.Button(haupt_fenster, text="OK", fg="red", bg="yellow")
button.grid(row=1, column=1)
# button.pack() <- würde nicht funktionieren, da vorher schon grid()

haupt_fenster.mainloop()