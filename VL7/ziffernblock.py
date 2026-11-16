import tkinter
haupt_fenster = tkinter.Tk()
haupt_fenster.title("THI-SWD Ziffernblock")
zaehler = 1

# erzeuge die Buttons von 1-9 
for zeile in range(3):
    for spalte in range(3):
        button = tkinter.Button(haupt_fenster, text=str(zaehler), width=10, height=5)
        button.grid(row=zeile, column=spalte)
        zaehler = zaehler + 1

haupt_fenster.mainloop()