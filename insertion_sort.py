# Insertion Sort

def insertionsort(list1):

    for i in range(1, len(list1)):

        while i > 0 and list1[i] < list1[i-1]:
            list1[i], list1[i-1] = list1[i-1],list1[i]
            i -= 1
    print(list1)

insertionsort([34, 21, 45, 12])
"""
alt code
"""
def insertionsort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq [pos - 1]:
            seq[pos], seq [pos - 1] = seq [pos - 1], seq[pos]
            pos -= 1
