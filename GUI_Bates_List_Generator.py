from tkinter import *
from collections import Counter

class App:
    def __init__(self, master):

        self.frame = Frame(master)
    #    self.frame.pack()
        self.frame.grid(row=10,column =10)

    def createTextInput(self):
        # create a Text widget
        self.txt = Text(self.frame, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word', width=25)
        self.txt.grid(row=0, column=0, padx=2, pady=2, rowspan=1, ipadx=0, ipady=0 ) 

        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(self.frame, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        self.button = Button(self.frame, text='Retrieve input', command=self.retrieve_input)
        self.button.grid(row=0, column=2)

    def createInterface(self , lines):
        self.entry = []
        self.entryLength = []
        self.message = []

        for count,line in enumerate(lines):
            #Creating and setting text output ,message and length variables
            lineVar = StringVar()
            lineVar.set(line)

            lengthVar = IntVar()
            lengthVar.set(len(line))

            messageVar = StringVar()
            messageVar.set(line)

            #Adds
            self.entry.append(Entry(self.frame, textvariable = lineVar))
            self.entry[count].grid(column=0, row=count+1, padx=2, pady=2)

            self.entryLength.append(Entry(self.frame, textvariable = lengthVar))
            self.entryLength[count].grid(column=1, row=count+1, padx=2, pady=2)

            self.message.append(Message(self.frame, textvariable = messageVar))
            self.message[count].grid(column=2, row=count+1, padx=2, pady=2 , sticky='nsew')

    def retrieve_input(self):
        lines = self.txt.get("1.0", END).splitlines()
        print(lines)
        self.createInterface(lines)

    def createEntry(self):
        self.entry = Entry(self.frame)
        self.entry.grid(row=0,column =0)

root = Tk()
app = App(root)

app.createTextInput()

root.mainloop()
root.destroy() # optional; see description below
