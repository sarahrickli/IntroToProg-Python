# Sarah Rickli
# 02.08.19 created original version
# script manages a to do list.

#-- Data --#

# dictionary to save task:priority
d = {}
# a list that acts as 'table' of rows.
l = []

filename = "/Users/sarahrickli/Documents/_PythonClass/Assignment05/ToDo.txt"

ToDotxt = open(filename, "r")

# Create a dictionary with elements in Todotxt
for line in ToDotxt:
    # replacing new line character for empty space
    line = line.replace("\n", " ")
    # splitting the line using ',' as delimiter
    line = line.split(",")
    # first element of line will be dictionary key
    dictK = line[0]
    # second element of line will be dictionary value
    dictV = line[1]
    # populating the dictionary
    d[dictK] = dictV

# Create a list with dictionary content
# Every item in list l is a tuple in the format (dict_key, dict_value)
# Ex: l = [ ('clean', 'low'), ('pay bill', 'high') ]
for k,v in d.items():
    item = (k, v)
    l.append(item)


# Display a menu of choices to the user
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print() # adding a new line

    # Show the current tasks in the list
    if (strChoice.strip() == '1'):
        for each in l:
            print(each[0] + ", " + each[1])

    # Add a new task to the list
    elif(strChoice.strip() == '2'):
        task = input("Task: ")
        prior = input("Priority: ")
        newData = (task, prior)
        l.append(newData)

    # Remove a task of the list
    elif(strChoice == '3'):
        removeData = input("Which tasks would you like to remove?" "\n" "Task: ")
        for each in l:
            # using lower() to ignore Case
            if each[0].lower() == removeData.lower():
                l.remove(each)
        print(each[0] + " was deleted.")

    # Save tasks to the ToDo.txt file
    elif(strChoice =='4'):
        newToDo = open(filename, "w")
        for each in l:
            newItem = (each[0] + ", " + each[1] + "\n")
            newToDo.write(newItem)
        newToDo.close()
        print("Data saved to file " + filename)

    # Exit the program
    elif (strChoice == '5'):
        # Before exiting, saving data to file
        newToDo = open(filename, "w")
        for each in l:
            newItem = (each[0] + ", " + each[1] + "\n")
            newToDo.write(newItem)
        newToDo.close()
        print("Exiting the program. Data saved to file " + filename)
        break
