# --------------
# Code starts here
class_1 = ['Geoffrey Hinton' , 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)




# Code ends here


# --------------
# Code starts here
courses = {'Math' : 65 , 'English' : 70 , 'History' : 80 ,'French' : 70 , 'Science' : 60 }
marks = [65, 70, 80 , 70, 60]
total = sum(marks)
print(total)
percentage = total/500*100
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffrey Hinton': 78 , 'Andrew Ng': 95 , 'Sebastian Rashka': 65 , 'Yoshua Benjio': 50 , 'Hilary Mason': 70 , 'Corinna Cortes': 66 , 'Peter Warden': 75}
marks = [78, 95, 65, 50, 70, 66, 75]
max_marks_scored = max(marks)
print(max_marks_scored)
topper = max(mathematics,key = mathematics.get)
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here
first_name = (topper.split()[0])
last_name = (topper.split()[1])
full_name = last_name + " " + first_name
certificate_name = full_name.upper()
print(first_name)
print(last_name)
print(full_name)
print(certificate_name)
# Code ends here


