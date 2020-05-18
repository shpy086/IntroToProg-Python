# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# 5.17.2020, Worked through steps 1-6 of the document
# 5.18.2020, Step 1 worked in pycharm but failed in command shell, changed objfile path from relative to absolute
# RRoot,1.1.2030,Created started script
# <Steve Huang, 5.17.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "C:\\_PythonClass\\Assignment05\\ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

loadFile = open(objFile,'r')
for row in loadFile:
    lstRow = row.split(',')
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
loadFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["Task"] + "," + dicRow["Priority"]) #
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("Enter To-Do item: ")
        priority = input("Enter priority level: ")
        dicRow ={"Task": task, "Priority": priority}#
        lstTable.append(dicRow)
        print("\n" + "This task has been added: ")
        print(dicRow["Task"] + "," + dicRow["Priority"])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        itemRemoved = None
        removeTask = input("Which task would you like to remove? ")
        removeTask = removeTask.lower()
        for dicRow in lstTable:
            if dicRow["Task"] == removeTask:
                itemRemoved = dicRow
                break #
        if itemRemoved is None:
            print("This item does not exist.")
            continue
        lstTable.remove(itemRemoved)
        print("This item has been removed: " + itemRemoved["Task"] + "\n")
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        loadFile = open(objFile,'w')
        for dicRow in lstTable:
            loadFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        print("All items have been saved.")
        loadFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Please hit 'Enter' to exit")
        break  # and Exit the program
