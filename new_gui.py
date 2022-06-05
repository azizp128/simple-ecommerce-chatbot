import PySimpleGUI as sg

layout = [
    [sg.Text('My one-shot window.')],
    [sg.Output(size=(50,25), key='-OUTPUT-')],
    [sg.Button('Product'), sg.Button('Price'), sg.Button('Shipping'), 
        sg.Button('Payment')],
    [sg.In(key='-QUERY-'), sg.Submit('Send')]
]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(values['-QUERY-'])

window.close()