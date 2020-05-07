#This is my final project for Python Basics: Masterticket
ticket_price = 10
tickets_remaining = 100
print("Welcome to Masterticket. Your one-stop-shop for getting hot tickets.")
name = input("Please enter your full name: ")
print("{}, there are {} tickets left.".format(name, tickets_remaining))
user_tickets = int(input("How many tickets would you like to purchase? "))

while user_tickets > tickets_remaining:
    user_tickets = int(input("Sorry, we do not have enough tickets for your purchase. Try again with a smaller amount: "))
order_confirmation = input("Order Confirmation: You are purchasing {} tickte[s].\n(Select OK or Cancel)  ".format(user_tickets))
ticket_price = user_tickets * 10
if order_confirmation == "OK":
    print("Please enter {} dollars".format(ticket_price))
print("Congratulations {}! You purchased {} tickets for the show. Enjoy!".format(name, user_tickets))