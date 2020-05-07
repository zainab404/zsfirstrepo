groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']
#this shows how to create a numbered list

index = 1
for index, item in groceries()


for index, item in enumerate(groceries, 1):
    print(index,"-", item)
