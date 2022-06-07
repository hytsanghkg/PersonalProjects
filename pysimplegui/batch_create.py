# batch_create.py

import PySimpleGUI as sg
import os.path

# First create the window layout in 2 columns

# Column 1
file_list_column = [
    [
        sg.Text("Source Directory"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Multiline(
            enable_events=True, size=(50, 20), key="-MULTILINE-", enter_submits=True
        )
    ],
]

# Column 2
status_column = [
    [sg.Text("Separate folder names with ','")],
    [sg.Text("Process Status")],
    [sg.Text(key="-STATUS-")],
    #[sg.CB('Completed')],
    [sg.OK()]
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(status_column),
    ]
]

# Header of the app
window = sg.Window("Batch Create Folders", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # If OK is clicked, create folders in batch
    if event == "OK":
        folder = values["-MULTILINE-"].split(',')
        # If path is not specified
        if values["-FOLDER-"] == "":
            window["-STATUS-"].update("No path specified")
        # If no names are specified
        elif folder == ['']:
            window["-STATUS-"].update("No names specified")
        else:      
            try:
                # Create folder one by one
                for value in folder:
                    filename = os.path.join(
                    values["-FOLDER-"], value)
                    os.mkdir(filename)
                window["-STATUS-"].update("Folders created")
                # file_list = os.listdir(folder)
            except:
                # Except when folder already exists
                os.path.isdir(value)
                window["-STATUS-"].update(value + " Folder already exists")
                

    #     fnames = [
    #         f
    #         for f in file_list
    #         if os.path.isfile(os.path.join(folder, f))
    #         and f.lower().endswith((".png", ".gif"))
    #     ]
    #     window["-FILE LIST-"].update(fnames)
    # elif event == "-FILE LIST-":  # A file was chosen from the listbox
    #     try:
    #         filename = os.path.join(
    #             values["-FOLDER-"], values["-FILE LIST-"][0]
    #         )
    #         window["-TOUT-"].update(filename)
    #         window["-IMAGE-"].update(filename=filename)

    #     except:
    #         pass

window.close()