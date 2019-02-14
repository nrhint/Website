##Nathan Hinton
##When this is done it will contain the complete gui for the html edditor.

#Here is the code for the edditor. It will have none of the HTML and CSS menus at first.


from tkinter import *
try:
    from tkinter import filedialog
except ImportError:
    print("IMPORT ERROR")
import time

class Edit:
    def __init__(self, filename):
        self.filename = filename
        self.root = Tk()
        self.root.attributes('-topmost')
        self.text = Text(self.root, height=30, width=120, font = ("Arial", 10))
        self.run()
    def o(self):
        self.save()
        self.text.delete(1.0 , END)
        self.filename = filedialog.askopenfilename()
        self.file = open(self.filename , 'r')
        if self.file != '':
            txt = self.file.read()
            self.text.insert(INSERT,txt)
        else:
            pass
    def opn(self):
        obj = Edit(filedialog.askopenfilename())
    def save(self):
        if self.filename:
            alltext = self.text.get(1.0, END)
            open(self.filename, 'w').write(alltext)
    def kill(self):
        self.save()
        self.root.quit()
    def kill2(self):
        self.save()
        self.root.destroy()
    def line(self):
        lin = "_" * 60
        self.text.insert(INSERT,lin)
    def date(self):
        data = time.localtime()
        self.text.insert(INSERT,data[0:3])
    def run(self):
        start = True
        #self.root = Tk()
        self.root.title(str(self.filename)+"-Edit")
        menu = Menu(self.root)
        filemenu = Menu(self.root)
        self.root.config(menu = menu)
        if start == True:
            try:
                file = open(str(self.filename), 'r')
                txt = file.read()
                self.text.insert(INSERT,txt)
            except FileNotFoundError:
                print("!!!FILE NOT FOUND ERROR!!!")
                print("MAKING A NEW FILE!")
                open(str(filename), 'w')
            start = False
        menu.add_cascade(label="File", menu=filemenu)
        #filemenu.add_separator()
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Open", command=self.o)
        filemenu.add_command(label="OpenInNewWin", command=self.opn)
        filemenu.add_command(label="Exit", command=self.kill2)
        insmenu = Menu(self.root)
        menu.add_cascade(label="Insert",menu= insmenu)
        insmenu.add_command(label="Date",command=self.date)
        insmenu.add_command(label="Line",command=self.line)
        html = Menu(self.root)
        files = Menu(self.root)
        #self.text = Text(self.root, height=30, width=60, font = ("Arial", 10))
        scroll = Scrollbar(self.root, command=self.text.yview)
        scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        self.text.pack()
        #self.root.resizable(0,0)
        self.root.mainloop()
##        print("run Finished")
obj = Edit(filedialog.askopenfilename())
