'''
 Suppose that candidates for a competitive exam can opt for 3 subjects out of 46.
 Compulsory papers for every candidates consist of 5 subjects.
 To schedule exams for all courses requires 5 + 46 = 51 days.
 There is a pattern in opting subjects. e.g. Candidates opting for Mathematics
 also opt for Statistics. Similarly some subjects are not opted together at all e.g. 
 candidates opting for Mathematics do not opt for Botany. 
 It is therefore possible to schedule exams for subjects that are not opted together on the same day,
 reducing the number of days required to conduct exams.

 Following code will be used to simulate the problem and its solution

  1. StudentID is a unique number identifying each Candidate appearing in exam.
  2. CourseID is a unique number between 1 and 46 (both inclusive) identifying one of the 46 option subjects.

  If we have 46 sets whose members are the StudentIDs, then each pair of disjoint sets can be scheduled on the same day.
  Suppose 10,000 candidates appear in the exam, we need to generate 46 sets.
  To model real world situation appropriately StudentIDs of 10,000 candidates should be distributed
  on 46 sets so that few sets have overlapping students. 
'''

# Set up a function to generate random numbers between 1 and 10,000
import random

min = 1
max = 10001
population = range(min,max)
sample = random.sample(population, 1000)
print(sample)
sample_set = set(sample)
print(len(sample_set))