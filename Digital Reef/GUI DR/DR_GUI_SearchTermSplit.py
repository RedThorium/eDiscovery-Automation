from tkinter import *
from collections import Counter

def num_of_open_paren(word):
    word = str(word)
    counter = Counter(word)
    return counter['('] - counter[')']

def split_OR_Terms(terms):
    #value is -1 and not zero because there is usually a pair of "()" arround
    #the whole set of terms so it causes the function not to work

    openCount = -1
    elementCount = 0
    termList = []

    for word in terms.split():
        openCount+=num_of_open_paren(word)
        if (word != "OR"):
            try: termList[elementCount]  = termList[elementCount] + " " + word
            except: termList.append(word)
        elif (word == "OR" and openCount == 0):
            elementCount+=1
        elif (word == "OR" and openCount >= 1):
            try: termList[elementCount]  = termList[elementCount] + " " + word
            except: termList.append(word)
    termList[0] = termList[0][1:]
    termList[-1] = termList[-1][:-1]
    return termList

class App:
    def __init__(self, master):

        self.frame = Frame(master)
    #    self.frame.pack()
        self.frame.grid(row=10,column =10)

    def createTextInput(self):
        # create a Text widget
        self.txt = Text(self.frame, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 10), undo=True, wrap='word', width=40, height=35)
        self.txt.grid(row=0, column=0, padx=2, pady=2, rowspan=1, ipadx=0, ipady=0 )

        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(self.frame, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        self.button = Button(self.frame, text='Retrieve input', command=self.retrieve_input)
        self.button.grid(row=1, column=0)

    def displaySplitTerms(self , lines):

        splitTerms = split_OR_Terms(lines)

        self.txt = Text(self.frame, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 10), undo=True, wrap='word', width=40, height=35)
        self.txt.grid(row=0, column=2, padx=2, pady=2, rowspan=1, ipadx=0, ipady=0 )

        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(self.frame, command=self.txt.yview)
        scrollb.grid(row=0, column=3, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

        """
        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(self.frame, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
        """

        for term in splitTerms:
            self.txt.insert(INSERT,term)
            self.txt.insert(INSERT,"\n")


    def retrieve_input(self):
        lines = self.txt.get("1.0", END)
        #print(lines)
        self.displaySplitTerms(lines)

    def createEntry(self):
        self.entry = Entry(self.frame)
        self.entry.grid(row=0,column =0)

root = Tk()
app = App(root)

app.createTextInput()

root.mainloop()
root.destroy() # optional; see description below
