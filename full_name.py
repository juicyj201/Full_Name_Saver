import re
from sys import argv
import csv
import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar

# CLASSES
class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last


    def __str__(self):
        return f"{self.first} {self.last}"


    @property
    def first(self):
        return self._first


    @first.setter
    def first(self, first):
        self._first = first if first != None else ValueError    


    @property
    def last(self):
        return self._last


    @last.setter
    def last(self, last):
        self._last = last if last != None else ValueError   

class RunWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)    
        self.first_label = tkinter.Label(self, text="Enter your first name: ", width=30, height=3)
        self.last_label = tkinter.Label(self, text="Enter you surname: ", width=30, height=3)
        self.first_name = tkinter.Entry(self)
        self.last_name = tkinter.Entry(self)
        self.confirm_btn = ttk.Button(self, text="Confirm", width=30, command=self.click)

        self.confirm_btn.grid(row=2, column=0, sticky="nsew", columnspan=2)
        self.first_label.grid(row=0, column=0, sticky="nsew")
        self.last_label.grid(row=1, column=0, sticky="nsew")
        self.first_name.grid(row=0, column=1, sticky="nsew")
        self.last_name.grid(row=1, column=1, sticky="nsew") 

    def click(self):
        if self.first_name.get != None:
            print(self.first_name.get())
            print(self.last_name.get())
            first_last(f"{self.first_name.get()} {self.last_name.get()}")
        else:
            print("theres something a foot")    
        #


# FUNCTIONS
def main():
    gui()


def first_last(s):
    if match := re.search(r'^(\w+)\s(\w+)$', s):
        first = match.group(1)
        last = match.group(2)
        return save_to_file(first, last)
    else:
        print("L + weak + bozo")            


def save_to_file(first, last):
    with open("full_name.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=['First Name', 'Last Name'])
        writer.writerow({'First Name': first, 'Last Name': last})

    messagebox.showinfo("Save success","Full name has been saved successfully.")    

def gui():
    window = RunWindow()
    window.rowconfigure(0, minsize=50)  
    window.columnconfigure([0, 1], minsize=50)

    # Run window
    window.eval('tk::PlaceWindow . center')
    window.mainloop()


if __name__ == "__main__":
    main()