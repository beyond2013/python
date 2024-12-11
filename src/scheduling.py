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
  among 46 sets so that few sets have more than 70% students in common, indicating that these subjects
  are often opted together e.g. pure mathematics and applied mathematics, mathematics and statistics, botany and chemistry. 
  where as few sets should have no students in common e.g. biology and mathematics usually not opted together.
'''

import random

def generate_random_sets(n, min_val, max_val):
  """
  Generates n random sets of numbers from min_val to max_val, ensuring each number appears in exactly 3 sets.

  Args:
    n: Number of sets to generate.
    min_val: Minimum value for the numbers in the sets.
    max_val: Maximum value for the numbers in the sets.

  Returns:
    A list of n sets, each containing numbers from min_val to max_val.
  """

  # Create a list of numbers from min_val to max_val
  all_numbers = list(range(min_val, max_val + 1))

  # Shuffle the list randomly
  random.shuffle(all_numbers)

  # Create n empty sets
  sets = [set() for _ in range(n)]

  # Assign each number to 3 sets, ensuring even distribution
  for i, num in enumerate(all_numbers):
    for j in range(3):
      set_index = (i * 3 + j) % n
      sets[set_index].add(num)
  return sets

def find_disjoint_pairs(sets):
    """
    Finds disjoint pairs of sets.

    Args:
        sets: A list of sets.

    Returns:
        A list of tuples, where each tuple contains the indices of two disjoint sets.
    """

    all_numbers = set()
    set_dict = {}
    disjoint_pairs = []

    for i, s in enumerate(sets):
        all_numbers.update(s)
        frozen_set_s = frozenset(s)
        if frozen_set_s not in set_dict:
            set_dict[frozen_set_s] = []
        set_dict[frozen_set_s].append(i)

    for s1, indices1 in set_dict.items():
        for s2, indices2 in set_dict.items():
            if s1.isdisjoint(s2):
                for i1 in indices1:
                    for i2 in indices2:
                        disjoint_pairs.append((i1, i2))

    return disjoint_pairs

# Generate 46 random sets with numbers from 1 to 10000
random_sets = generate_random_sets(46, 1, 10000)

# Print the generated sets (for debugging or verification)
for i, s in enumerate(random_sets):
  print(f"Set {i+1}: Length:{len(s)} {type(s)}")
print(f"Total elements in all sets = ", sum(len(s) for s in random_sets))
disjoint_pairs = find_disjoint_pairs(random_sets)
print(disjoint_pairs)
