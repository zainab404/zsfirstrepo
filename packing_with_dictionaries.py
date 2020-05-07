#packing is when you can pass multiple arguments. 
#here, we used **kwargs to signify the use of multiple arguments.
#the for loop will iterate over the arguments given and print each one

def print_student(**kwargs):
    for key,value in kwargs.items():
        print("{} {}".format(key,value))

print_student(name = "Zainab", job = "Programmer", major = "ISOM", boyfriend = "Guillermo")

