import config
import protocols.test_stream.client as ts_client
import PySimpleGUI as sg

def run():
    
    #Operating mode constant
    MODE = ""

    #Layout for choosing operating mode
    choose_layout = [  [sg.Text('Choose a protocol')],
                [sg.Button('Test stream'), sg.Button('Http')],
                ]

    #Create the Window
    window = sg.Window('Soundnet '+config.get("main","version"), choose_layout, size=(300,300), element_justification='c')

    #Client loop
    while True:

        event, values = window.read(timeout=100)

        if event == "Test stream":
            new_window = sg.Window('Soundnet '+config.get("main","version"), ts_client.get_layout(), size=(300,300), element_justification='c', finalize=True)
            window.close()
            window = new_window

            ts_client.init()
            MODE = event

        if MODE == "Test stream":
            ts_client.listen(event, values, window)
            
            
        if event == sg.WIN_CLOSED or event == 'Exit': 
            break

    window.close()
