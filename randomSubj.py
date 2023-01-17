import random

subjects = list(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'))

def randomSubject(subj):
    result = random.sample(
            range(0, len(subj)), 3
            ) # returns 3 random int from 0 to len(subj)
    random_subj = list()
    for x in result:
        random_subj.append(subjects[x])

    return random_subj

#print(randomSubject(subjects))

var = "student"
list_of_str = list()

for i in range(10):
    newvar= var + str(i+1)
    list_of_str.append(newvar) 

list_of_students = list()

for st in list_of_str:
    st = randomSubject(subjects) 
    list_of_students.append(st)


print("First Student:", list_of_students[0])
