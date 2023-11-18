### LIBRARIES

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

#--------------------------------------------------------------------------------------------------------------------------------------------------------

### FUNCTIONS

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def clear_console():
    if os.name == 'posix':
        _ = os.system('clear')  # For Unix/Linux (including Mac)
    else:
        _ = os.system('cls')    # For Windows systems

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def validation(options, choice):
    words = ""
    for i in range(0, len(options)):
        words = words + " " + options[i]
    state = False
    for i in range(0, len(options)):
        if options[i] == choice:
            state = True
    while state == False:
        print(f"Incorrect option, you can only choose from: {words}")
        choice = input("Try again: ")
        for i in range(0, len(options)):
            if options[i] == choice:
                state = True
    return choice

#--------------------------------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------------------------

def menu1():
    clear_console()
    print()
    print("---------------- MENU ----------------")
    print()
    print("1 - Load a database")
    print("2 - Select a database")
    print("3 - Exit")
    print()
    option_menu1 = input("What would you like to do? (choose 1 or 2 or 3): ")
    option_menu1 = validation(["1", "2", "3"], option_menu1)
    return option_menu1

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def create():
    pass

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def choose_dataset():    
    selected_subfolder = select_subfolder()
    selected_file = select_file(selected_subfolder)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def list_subfolders():
    return [name for name in os.listdir('examples') if os.path.isdir(os.path.join('examples', name))]

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def list_files_in_folder(folder):
    folder_path = os.path.join('examples', folder)
    return [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def select_subfolder():
    print("Available subfolders:")
    subfolders = list_subfolders()
    for i, subfolder in enumerate(subfolders, start=1):
        print(f"{i}. {subfolder}")

    while True:
        try:
            option = int(input("Select a subfolder (enter the corresponding number): "))
            if 1 <= option <= len(subfolders):
                return subfolders[option - 1]
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def select_file(subfolder):
    print(f"Files available in '{subfolder}':")
    files = list_files_in_folder(subfolder)
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    while True:
        try:
            option = int(input("Select a file (enter the corresponding number): "))
            if 1 <= option <= len(files):
                return os.path.join('examples', subfolder, files[option - 1])
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------------------------

### PROGRAM START

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    start = 1

    while start == 1:
        option_menu1 = menu1()

        if option_menu1 == "1":
            choose_dataset()
        elif option_menu1 == "2":
            pass
        else:
            start = 0
            print()
            input("Goodbye")

#--------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
