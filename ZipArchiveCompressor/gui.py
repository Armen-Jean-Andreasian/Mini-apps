import PySimpleGUI
from script import make_archive


class ZipCompressor:
    def __init__(self):

        self.label1 = PySimpleGUI.Text("Select files to compress")
        self.input1 = PySimpleGUI.Input()
        self.choose_button = PySimpleGUI.FilesBrowse(button_text="Choose", key="files")

        self.label2 = PySimpleGUI.Text("Select destination folder")
        self.input2 = PySimpleGUI.Input()
        self.choose_button2 = PySimpleGUI.FolderBrowse(button_text="Choose", key="folder")

        self.compress_button = PySimpleGUI.Button("Compress")
        self.output_label = PySimpleGUI.Text(key="output", text_color='green')

        self.window = PySimpleGUI.Window(title="File Compressor",
                                         layout=[[self.label1, self.input1, self.choose_button],
                                                 [self.label2, self.input2, self.choose_button2],
                                                 [self.compress_button, self.output_label]])

    def run(self):
        while True:
            event, values = self.window.read()
            try:
                filepaths = values['files'].split(";")
                folder = values['folder']
                make_archive(filepaths, folder)
                self.window['output'].update(value='Compression completed')
            except AttributeError:
                break

            if PySimpleGUI.WIN_CLOSED:
                break

        self.window.close()
