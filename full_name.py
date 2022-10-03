import re
from sys import argv
import csv
import os

def main():
    if argv[1] == "-n":
        first_last(str(input("What is your full name: ")))
        open_file()



def first_last(s: str):
    if match := re.search(r'^([a-zA-Z])([ ])([a-zA-z])$', s):
        name_dict = {
            "First Name":match.group(1), 
            "Last Name":match.group(3)
        }

        return save_to_file(name_dict)        


def save_to_file(**converted):
    with open("full_name.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name"])
        writer.writerow(converted)


def open_file():
    file = "./full_name.csv"
    fp = os.open(file)


if __name__ == "__main__":
    main()