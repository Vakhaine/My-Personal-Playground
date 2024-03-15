import PySimpleGUI as sg

label_1 = sg.Text("Select files to compress:")
input_1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label_2 = sg.Text("Select destination folder:")
input_2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

windows = sg.Window("Files Compressor",
                    layout=[[label_1, input_1, choose_button1],
                            [label_2, input_2, choose_button2],
                            [compress_button]])
windows.read()
windows.close()
