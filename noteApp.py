from customtkinter import *
import sys

class App():
    def __init__(self):
        self.root = CTk()
        self.root.geometry('800x600')
        self.root.title('noteApp')
        
        self.fileOpen = CTkButton(self.root, text='File open', command=self.OpenFile)
        self.fileSave = CTkButton(self.root, text='File save', command=self.SaveFile)
        self.fileSaveAs = CTkButton(self.root, text='File save as', command=self.SaveFileAs)

        self.fileOpen.grid(row=0, column=0, padx=5, pady=5)
        self.fileSave.grid(row=0, column=1, padx=5, pady=5)
        self.fileSaveAs.grid(row=0, column=2, padx=5, pady=5)

        self.textBox = CTkTextbox(self.root, height=562, width=790)
        self.textBox.grid(row=1, column=0, columnspan=3)

        self.SaveFileName = ''

    def OpenFile(self):
        def load_file():
            file_name = self.fileEntry.get()

            try:
                with open(file_name, 'r') as f:
                    content = f.read()
                    self.textBox.delete('0.0', 'end')
                    self.textBox.insert('0.0', content)
                    self.SaveFileName = file_name
            except FileNotFoundError:
                self.textBox.delete('0.0', 'end')
                self.textBox.insert('0.0', 'Invalid file')

            self.fileEntry.grid_forget()
            self.enter.grid_forget()

        self.fileEntry = CTkEntry(self.root, width=645)
        self.fileEntry.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.textBox.grid_forget()
        self.textBox.grid(row=2, column=0, columnspan=4)

        self.enter = CTkButton(self.root, text='Enter File Name', command=load_file)
        self.enter.grid(row=1, column=3)

    def SaveFile(self):
        if self.SaveFileName == '':
            self.SaveFileAs()
        else:
            content = self.textBox.get("0.0", "end")
            try:
                with open(self.SaveFileName, 'w') as f:
                    f.write(content)
            except Exception as e:
                if hasattr(self, 'saveButton'):
                    self.saveButton.configure(text='Error')
                else:
                    print("Save failed:", e)

    def SaveFileAs(self):
        def save_file():
            file_name = self.fileEntry.get()
            self.SaveFileName = file_name
            content = self.textBox.get("0.0", "end")

            try:
                with open(file_name, 'w') as f:
                    f.write(content)
            except Exception as e:
                self.saveButton.configure(text='Error')

            self.fileEntry.grid_forget()
            self.saveButton.grid_forget()

        self.fileEntry = CTkEntry(self.root, width=645)
        self.fileEntry.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.textBox.grid_forget()
        self.textBox.grid(row=2, column=0, columnspan=4)

        self.saveButton = CTkButton(self.root, text='Enter File Name', command=save_file)
        self.saveButton.grid(row=1, column=3)

if __name__ == '__main__':
    app = App()
    app.root.mainloop()