course = {"name":"Zainab Ali", "major":"ISOM", "grade": "Senior", "career":"coder"}

print(course['name'])
#changes the value of the 'name' key
course['name'] = "Hadia Ali"
#adds a new key:value pair in the dictionary
course['age'] = 21

print(course)
#deletes the key 'age'
del(course['age'])

#iterates over a dictionary
for key,value in course.items():
    print(key,value)