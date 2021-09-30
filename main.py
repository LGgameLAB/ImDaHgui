import PySimpleGUI as sg
import lib

sg.theme('DarkAmber')

commands = {
    "decode": lib.decode,
    "encode": lib.encode 
}
inputs = {
    "encodeTxt": sg.InputText(),
    'fileName' :sg.InputText()
}
layout = [  [sg.Text('Encoding message:'), inputs["encodeTxt"]],
            [sg.Text('Enter a filename'), inputs["fileName"], sg.FileBrowse()],
            [sg.Button(k,) for k, v in commands.items()],
            [sg.Text('Output:', key='txt1')],
            [sg.Cancel()]]


window = sg.Window('ImDaH', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print(values)
    for k, v in commands.items():
        if event == k:
            window.Element('txt1').Update(f"Output: {commands[k](values)}")
    

window.close()