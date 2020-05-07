#make a contact book for people to add in. 
#TODO allow user to input contacts. first ask their name, and phone number. 
#TODO add new contact to contact book.
#TODO allow user to access it whenever
#TODO provide a delete function
#TODO allow them to select a contact to call. 

contact_book = []
 
def instructions():
    print ("""
||Contact Book||
'Add' : adds new contact
'Show' : shows current contact book
'Edit' : edits a current contact
'Done' : completes your contact book
'Delete' : deletes an entry
""")

def add_contact(contact_name, contact_number):
    contact_book.append([contact_name, contact_number])
    print("New contact added:")

def show_contacts():
    print("All contacts: ")
    contact_position = 1
    for contact in contact_book:
        print(contact_position, ". ", contact[0], "-", contact[1])
        contact_position += 1
    
instructions()
while True:
    navigation_choice = input("> ")
    if navigation_choice == "Add":
        new_name = input("Enter First and Last Name: ")
        new_number = input("Enter Phone Number:")
        add_contact(new_name, new_number)
        print(new_name, "(", new_number,")")
    elif navigation_choice == "Show":
        show_contacts()
    elif navigation_choice == "Delete":
        show_contacts()
        contact_position = int(input("Select contact to delete: "))
        del contact_book[contact_position - 1]
    elif navigation_choice == "Edit":
        show_contacts()
        contact_position = int(input("Select contact to edit: "))
        contact_change = input("Enter new phone number: ")
        contact_book[contact_position - 1 ][1]= contact_change
    elif navigation_choice == "Done":
        break