#Grocery List
#Logan Walker
#period 7
#1/18/24

mylist= []
#functions
#this function lets users choose an option of what they want to do with their grocery list
#no parameters
def GroceryList():
    print("Welcome to your grocery list.")
    print("Please choose an option:")
    print("1. Add to list \n 2. View current list \n 3. Mark task as completed \n 4. Remove task from list \n 5. Clear list \n 6. Sort list \n 7. Display amount of items \n 8. Exit list")
    option= int(input ("Option: "))
    if option==1:
        add()
        GroceryList()
    if option ==2:
        view()
        GroceryList()
    if option==3:
        complete()
        GroceryList()
    if option ==4:
        remove()
        GroceryList()
    if option ==5:
        clear()
        GroceryList()
    if option ==6:
        sortlist()
        GroceryList()
    if option ==7:
        displaynotes()
        GroceryList()
    if option ==8:
        quit()
    else:
        print("invalid input. Please try again")
        GroceryList()
#Prints the number of items in the list
def displaynotes():
    print (len(mylist))
#Sorts the list alphabetically
def sortlist():
    mylist.sort()
    print(mylist)

#Clears the list of items
def clear():
    mylist.clear()
#this function asks users for input and adds it to the grocery list
def add():
    x = str(input("Items: "))
    mylist.append(x)
 #this function lets users view the list by printing the items on it  
def view():
    print(mylist)
#this function asks users for an input of what item they want to mark and then finds the position of the item. Then it replaces the item with a message that it is marked as bought
def complete():
    print("What item do you want to mark as bought? ")
    z=str(input("Item: "))
    if z in mylist:
        a=mylist.index(z)
        mylist.pop(a)
        mylist.insert(a, z+ " bought")
    else:
        print("Invalid input please try again")
        complete()
        
#this function asks users for input and removes that items from the list
def remove():
    y=str(input("Item you want to remove: "))
    if y in mylist:
        b=mylist.index(y)
        mylist.pop(b)
    else:
        print("Invalid input please try again")
        remove()
#this function ends the program
def end():
    quit()



#main
GroceryList()
