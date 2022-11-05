import arrow
import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [
    [sg.Button('New York', size = (10,1)),
    sg.Button('Dublin', size = (10,1)),
    sg.Button('Belgrade', size = (10,1)),
    sg.Button('Tokyo', size = (10,1))],
    [sg.Text('', size = (40,1))]
]

window = sg.Window(title = 'Current time', layout = layout, font = ('Arial', 16))

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'New York':
        pass
    if event == 'Dublin':
        pass
    if event == 'Belgrade':
        pass
    if event == 'Tokyo':
        pass

window.close()