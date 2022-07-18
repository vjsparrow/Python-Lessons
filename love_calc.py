print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1=name1.lower()
name2=name2.lower()

# Initialize a variable to keep a count of how many times True appears in both names
t=0
# Initialize a variable to keep a count of how many times Love appears in both names
l=0
# Concatenate both names into one string
nameb=name1+name2
# Check how many times True appears in both names
t=nameb.count("t")
t=t+nameb.count("r")
t=t+nameb.count("u")
t=t+nameb.count("e")
# Check how many times Love appears in both names
l=nameb.count("l")
l=l+nameb.count("o")
l=l+nameb.count("v")
l=l+nameb.count("e")
# Concatenate both variables.
j=int(str(t)+str(l))
# Print the right message using If
if j<10 or j>90:
  print(f"Your score is {j}, you go together like coke and mentos.")
elif j>40 and j<50:
  print(f"Your score is {j}, you are alright together.")
else:
  print(f"Your score is {j}.")
