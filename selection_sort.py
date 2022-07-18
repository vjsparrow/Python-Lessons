def selectionsort(l):
# Run through the list comparing minimum value to the current value
  for start in range(len(l)):
# Assign minimum value to the iterated value
    minpos = start
    for i in range(start,len(l)):
      if l[i]<l[minpos]:
        minpos=i

# Replace initial minimum value by the current minimum value
    (l[start],l[minpos])=(l[minpos],l[start])

  return(l)
"""
Alt code
"""
def select (array):

  for i in range (len(array)):
    for j in range(i+1, len(array)):
      if array[i] > array[j]:

        array[i], array[j] = array [j], array [i]
  print (array)

select([78, 34, 4, 45, 16, 1]
