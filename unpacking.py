full_name = input("Enter your full name: \n").split(" ")

print(full_name)
#here i will unpack my user input and assign it to two different variables, respectively
first, last = input("plz enter your full name: \n").split(" ")
print(first)
print(last)

def unpacker(*args):
    return args
    
#here i am assigned two variables to each parameter in my function
val1, val2 = unpacker('Python', 'rocks!')
print(val1)
print(val2)
