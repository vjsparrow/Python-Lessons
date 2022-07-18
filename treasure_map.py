# TreasureMap
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Position is a string, need to convert it to a list
i=list(position)
# map[[11,21,31],[12,22,32],[13,23,33]]
# map[[00,01,02],[10,11,12][20,21,22]]
# map[0,1,2]
# i=[a,b]
j=int(i[1])
k=int(i[0])
map[j-1][k-1]="X"

# Alternate Code

# j=int(i[0])
# j=j-1
# if i[1]=="1":
#   row1[j]="X"
# elif i[1]=="2":
#   row2[j]="X"
# elif i[1]=="3":
#   row3[j]="X"
# else:
#   print("Please enter correct number! Map unchanged!")
# a=1, then y=0. a=2, then y=1. a=3, then y=2
# b=1, then x=0. b=2, then x=1. b=3, then x=2.

print(f"{row1}\n{row2}\n{row3}")
