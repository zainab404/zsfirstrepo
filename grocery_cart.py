grocery_list = []

def show_help():
    print("Virtual Grocery List Application")
    print("""
Enter 'DONE' to finish list.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


def addToList(item):
    grocery_list.append(item)
    print("New item added. List has {} item[s]".format(len(grocery_list)))


def show_list():
    print("Grocery List: ")
    for item in grocery_list:
        print(item)


show_help()
while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    addToList(new_item)
    #^^^i don't understand the calling of this function
show_list()
    
    




#TODO continually prompt the user to add a grocery item or view my list
#TODO provide a (HELP) option for the user if they need to understand how to use this
#TODO allow the user to add the item
#TODO upon the user adding an itme, present their grocery list to them
#TODO allow them to see their list at any time
#TODO allow them to finish making their list and show them final list