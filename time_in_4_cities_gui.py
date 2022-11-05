import arrow
import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [
    [sg.Button('New York', size = (10,1)),
    sg.Button('Dublin', size = (10,1)),
    sg.Button('Belgrade', size = (10,1)),
    sg.Button('Tokyo', size = (10,1))],
    [sg.Text('')],
    [sg.Text('', key = '_TIME_', size = (40,1), justification='c')]
]

window = sg.Window(title = 'Current time', layout = layout, font = ('Arial', 16))

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'New York':
        time = arrow.now('America/New_York').ctime()
        window['_TIME_'].Update(f"{time}")
    if event == 'Dublin':
        time = arrow.now('Europe/Dublin').ctime()
        window['_TIME_'].Update(f"{time}")
    if event == 'Belgrade':
        time = arrow.now('Europe/Belgrade').ctime()
        window['_TIME_'].Update(f"{time}")
    if event == 'Tokyo':
        time = arrow.now('Asia/Tokyo').ctime()
        window['_TIME_'].Update(f"{time}")

window.close()