#RockPaperScissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

i=[rock,paper,scissors]
j=random.choice(i)
k=input("Rock, Paper, or Scissors?\n")
k=k.lower()
while k!="rock" and k!="paper" and k!="scissors":
  k=input("Invalid entry! Please try again:")
  k=k.lower()
if k=="rock":
  if j==paper:
    print(rock)
    print(j)
    print("You lose!")
  elif j==scissors:
    print(rock)
    print(j)
    print("You win!")
  else:
    print(rock)
    print(j)
    print("It's a tie :-|")
elif k=="paper":
  if j==rock:
    print(paper)
    print(j)
    print("You win!")
  elif j==scissors:
    print(paper)
    print(j)
    print("You lose!")
  else:
    print(paper)
    print(j)
    print("It's a tie :-|")
elif k=="scissors":
  if j==paper:
    print(scissors)
    print(j)
    print("You win!")
  elif j==rock:
    print(scissors)
    print(j)
    print("You lose!")
  else:
    print(scissors)
    print(j)
    print("It's a tie :-|")
