'''
Write a Python function histogram(l) that takes as input a list of integers with repetitions 
and returns a list of pairs as follows:.

for each number n that appears in l, there should be exactly one pair (n,r) in the list returned 
by the function, where r is the number of repetitions of n in l.

the final list should be sorted in ascending order by r, the number of repetitions. For numbers 
that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

>>> histogram([13,12,11,13,14,13,7,7,13,14,12])
[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

>>> histogram([7,12,11,13,7,11,13,14,12])
[(14, 1), (7, 2), (11, 2), (12, 2), (13, 2)]

>>> histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])
[(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]

'''


# State the problem: 
  # Count the number of repititions for each element of a list and return a pair (element, count of repitions of the element) sorted by:
    # 1. The count of repititions, and in case of a tie in the count of repititions:
    # 2. By the size of the element.

# Algorithm:
  # 1. Iterate through the list and find the count of repititions for each element.
  # 2. Store the result in pairs and append them to a list
  # 3. Next, we need to sort these pairs. Iterate through the list with pairs and perform insertion sort.
  # 4. Return the sorted list.

def histogram(l):
  final_list = []
# Generating the list of pairs
  helper_list = []
  for i in range(len(l)):
    if not l[i] in helper_list:
      helper_list.append(l[i])
      r = 0
      for j in range(i, len(l)):
        if l[j] == l[i]:
          r += 1
      final_list.append((l[i], r))
  
  # Sorting the list of pairs(employing Insertion Sort)
  for i in range(len(final_list)):
    pos = i
  
    while pos > 0 and (final_list[pos][1] < final_list[pos - 1][1] or final_list[pos][1] == final_list[pos - 1][1]):
      if final_list[pos][1] < final_list[pos - 1][1]:
        (final_list[pos], final_list[pos - 1]) = (final_list[pos - 1], final_list[pos])
      elif final_list[pos][1] == final_list[pos - 1][1]:
        if final_list[pos][0] < final_list[pos - 1][0]:
          (final_list[pos], final_list[pos - 1]) = (final_list[pos - 1], final_list[pos])
      pos -= 1
  return(final_list)

print(histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7]))
