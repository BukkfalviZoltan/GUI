#A GUI-hoz PySimpleGui-t használtam. Ennek telepítéséhez az alábbit kell a Terminal ablakban beírni és futtatni: python -m pip install pysimplegui

import PySimpleGUI as sg

layout = [[sg.Text("Üdvözlünk a comb adagolóban!")], [sg.Button("Libacomb adagoló"), sg.Button("Kacsacomb adagoló"), sg.Button("Csirkecomb adagoló")], [sg.Button("Jóllaktam")]]

# Ablak létrehozása
window = sg.Window("COMBADAGOLÓ", layout)

# Event loop\eseménykezelő ciklus létrehozása
while True:
    event, values = window.read()
    #Program vége, ha a felhasználó a "Jóllaktam" gombra kattint, illetve, ha az ablakbezáró gombot használja
    if event == "Jóllaktam" or event == sg.WIN_CLOSED:
        sg.popup('Viszontlátásra!')
        break
    elif event == "Kacsacomb adagoló":
        sg.popup('Kapsz egy kacsacombot!')
    elif event == "Libacomb adagoló":
        sg.popup('Kapsz egy libacombot!')
    elif event == "Csirkecomb adagoló":
        sg.popup('Kapsz egy csirkecombot!')    
window.close()
#kommentet hagyunk ittend.