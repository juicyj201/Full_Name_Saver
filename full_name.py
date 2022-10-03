import re
from sys import argv
import csv

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


def main():
    if argv[1] == "-n":
        first_last(str(input("What is your full name: ")))


def first_last(s):
    if match := re.search(r'^(\w+)\s(\w+)$', s):
        first = match.group(1)
        last = match.group(2)
        #print(match.group(1), match.group(2))
        return save_to_file(first, last)        


def save_to_file(first, last):
    with open("full_name.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=['First Name', 'Last Name'])
        writer.writerow({'First Name': first, 'Last Name': last})


if __name__ == "__main__":
    main()