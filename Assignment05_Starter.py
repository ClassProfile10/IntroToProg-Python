# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RR,1.1.2030,Created started script
# C,11.13.22,Added code to complete assignment 5 for step 3-7
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
#strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """  # A menu of user options
strChoice = "" # A Capture the user option selection
lstRow =[]


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile =  open("ToDoList.txt", 'r')
for row in objFile:
    lstRow= row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip() }
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print('Task    |    Priority')
        for i in lstTable:
            print(i["Task"] + ' | ' + i['Priority'])

        continue # goes back to the top of while loop
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        while (True):
            str_task = input('Task: ')
            str_value = input('Priority: ')
            lstTable.append({"Task": str_task, "Priority": str_value})
            str_choice = input('Exit? ("y/n"): ')
            if str_choice.lower() == 'y':
                break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        while (True):
            tracker = 0
            str_task = input('Enter Task to remove: ')
            for row in lstTable:
                if row["Task"].lower() == str_task.lower():
                    print('This row was removed: ', row)
                    lstTable.remove(row)

                    print('new table is: ', lstTable)
                    tracker = + 1
            if tracker >= 1:
                pass
            else:
                print('row not found')
            str_choice = input('Exit? ("y/n"): ')
            if str_choice.lower() == 'y':
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile =  open("ToDoList.txt", 'w')
        for row in lstTable:
            objFile.write(row['Task'] + ',' + row['Priority'] + '\n')
        objFile.close()

        print('The following data was saved to the file: ')
        for row in lstTable:
            print(row["Task"],',',row['Priority'])

        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program, breaks the while loop
