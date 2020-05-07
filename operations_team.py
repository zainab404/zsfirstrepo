# TODO Create an empty list to maintain the player names
member_names = []

# TODO Ask the user if they'd like to add players to the list.
entry_choice = input("Would you like to add a new player? (Y/N)  ")
# If the user answers "Yes", let them type in a name and add it to the list.
if entry_choice.lower() == "y":
    first_member = input("Enter member name:  ")
    member_names.append(first_member)
# If the user answers "No", print out the team 'roster'
else:
    print("There are no members on the team.")

extra_entry = input("Would you like to add another member to the team? (Y/N)  ")
while extra_entry.lower() == "y":
    second_member = input("Enter member name:  ")
    member_names.append(second_member)
    extra_entry = input("Would you like to add another member to the team? (Y/N)  ")
# TODO print the number of players on the team
# TODO Print the player number and the player name
roster = len(member_names) 
if roster == 1:
    print("There is 1 member on the operations team")
    print(member_names[0])
else:
    print("There are {} members on the operations team".format(roster))
    member_number = 1
    for name in member_names:
        print("Member", member_number,":", name)
        member_number = member_number + 1
    vip = int(input("Please select the V.I.P. member by selecting their corresponding number. (1 - {}): ".format(roster)))
    print(member_names[vip - 1], "is the V.I.P. member. ")
    #for vip_choice in member_names:
        #if vip_choice == member_names[vip-1]:
            #print(vip_choice, "is the V.I.P. member.)