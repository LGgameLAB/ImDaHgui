import PySimpleGUI as sg
import os
import lib

sg.theme('Light Green 2')

commands = {
    "decode": lib.decode,
    "encode": lib.encode 
}
inputs = {
    "encodeTxt": sg.InputText(),
    'fileName' :sg.InputText()
}
layout = [  [sg.Text('Encoding message:'), inputs["encodeTxt"]],
            [sg.Text('Enter a filename'), inputs["fileName"], sg.FileBrowse(initial_folder=os.getcwd())],
            [sg.Button(k,) for k, v in commands.items()],
            [sg.Text('Output:', key='txt1',size=(60, 1))],
            [sg.Cancel()]]

# resource/image1.jpeg
window = sg.Window('ImDaH', layout, finalize = True,element_padding=(2, 2), auto_size_text=True)
# window['txt1'].update(f"WTF")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    for k, v in commands.items():
        if event == k:
            newtext = f"Output: {str(commands[k](values))}"
            print(newtext)
            window['txt1'].update(newtext)
    

window.close()