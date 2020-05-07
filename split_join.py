import time

opinion = "Zainab is the best sister ever!"
facts = opinion.split()
for words in facts:
    print(words)
    time.sleep(.5)

def grocery_list(list_of_groceries):
    list_of_groceries = input("")