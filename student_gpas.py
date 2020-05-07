student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]

#this created a new variable that only includes a slice of the original. 
sliced_gpas = student_gpas[2:5]
print(sliced_gpas)

#both of these statements are true
2.3 in student_gpas
1.1 not in student_gpas

#this will check if 3.7 appears in the list student_gpas 
if 3.7 in student_gpas:
    print("I love guillermo")

#this will determine how many times the int '4.0' appears in the list student_gpas
print(student_gpas.count(4.0))

print(student_gpas.index(4.0))