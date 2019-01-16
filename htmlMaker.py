##Nathan Hinton.
##this will create HTML files.  First it will start my creating a template and a new file.
##I realized that I cant do enters when using this as they will end the edditing of the file.

import os

def ls():
    print(os.listdir())
def cd():
    i = input('Dir: ')
    try:
        os.chdir(i)
        ls()
    except FileNotFoundError:
        print("Path not found!")
        print("restarting command")
        cd()

def openFile():
    f = open(filedialog.askopenfilename, 'r')
    data = f.read()
    #print(data)
    return data

def addData(data):
    print()
    #print("Text to add to a file:")
    print("Here is the current contents of the file:")
    print(data)
    print()
    i = input()
    if i == '':
        i = data
    return i

def changeFile(file, data):
    f = open(file, 'w')
    f.write(data)

#def editFile(name):
#    data = openFile(name)
#    newData = addData(data)
#    changeFile(name, newData)
    
def createFile():
    name = input("File name: ")
    template = input("Template Name: ")
    if template != '':
        try:
            tem = open(template, 'r')
            changeFile(name, tem.read())
        except FileNotFoundError:
            print("Template file not found!")

#Main Loop:
def main():
    run = True
    while run == True:
        print("-1:setup file")
        print("0:exit")
        print("1:veiw file")
        print("2:create file")
        print("3:edit file")
        print("4:list files")
        print("5:change dirrectory")
        i = input()
        if i == '-1':
            print("Press h")
            editFile('setup-tutorial')
        elif i == '0':
            run = False
            print("Thank you for using this program!")
        elif i == '1':
            print(openFile(input("Filename: ")))
        elif i == '2':
            createFile()
        elif i == '3':
            editFile()
        elif i == '4':
            ls()
        elif i == '5':
            cd()
        else:
            print("Invalid input!")

#main()


#Below is code that I found on github for a python text edditor.  I have stripped ot of some functionality.  THis will allow the files to be eddited more dynamicaly.

#enrixpad is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
# -*- coding: cp1252 -*-
from tkinter import *
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
    def table(self):
        self.text.insert(INSERT, """
<table>
  <thead><!--Table Header-->
    <th></th>
    <th></th>
    <th></th>
  </thead>
  <tbody><!--Table row 1-->
    <td></td>
    <td></td>
    <td></td>
  </tbody>
  <tbody><!--Table row 2-->
    <td></td>
    <td></td>
    <td></td>
  </tbody>
  <tbody><!--Table row 33-->
    <td></td>
    <td></td>
    <td></td>
  </tbody>
</table>
""")
    def line(self):
        self.text.insert(INSERT, "<hr>")
    def em(self):
        self.text.insert(INSERT, "<em></em>")
    def address(self):
        self.text.insert(INSERT, "<address></address>")
    def bold(self):
        self.text.insert(INSERT, "<b></b>")
    def picture(self):
        self.text.insert(INSERT, "<img></img>")
    def comment(self):
        self.text.insert(INSERT, "<!--  -->")
    def list(self):
        self.text.insert(INSERT, """
<ul><caption></caption>
  <li></li>
  <li></li>
  <li></li>
</ul>
""")
    def a(self):
        self.text.insert(INSERT, "<a href=\"\"><a/>")
    def p(self):
        self.text.insert(INSERT, "<p></p>")
    def heading(self):
        self.text.insert(INSERT,"<h3></h3>")
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
        menu.add_cascade(label="HTML",menu=html)
        menu.add_cascade(label="files", menu=files)
        html.add_command(label="Heading",command=self.heading)
        html.add_command(label="p", command = self.p)
        html.add_command(label="Link", command = self.a)
        html.add_command(label="List", command = self.list)
        html.add_command(label="Comment", command = self.comment)
        html.add_command(label="Picture", command = self.picture)
        html.add_command(label="Table", command = self.table)
        html.add_command(label="hr", command = self.line)
        html.add_command(label="Emphasis", command = self.em)
        html.add_command(label="Address", command = self.address)
        html.add_command(label="Bold", command = self.bold)
        #self.text = Text(self.root, height=30, width=60, font = ("Arial", 10))
        scroll = Scrollbar(self.root, command=self.text.yview)
        scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        self.text.pack()
        #self.root.resizable(0,0)
        self.root.mainloop()
        print("run Finished")
def editFile():
    obj = Edit(filedialog.askopenfilename())

main()
