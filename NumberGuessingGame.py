import random
pool=[]
for i in range(1,101):
  pool.append(i)
print("Welcome to the number guessing game!")
guessed_number=random.choice(pool)

print("I'm thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty, 'easy' or 'hard': ")

if difficulty=="easy":
  attempts=10
  while attempts>0:
    user_guess=int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
    attempts-=1
    if user_guess==guessed_number:
      print(f"You guessed it! The number was {guessed_number}")
      attempts=0
    elif user_guess<guessed_number:
      print("Too low!\nGuess again.")
    else:
      print("Too high.\nGuess again.")
  else:
    print(f"You are out of guesses. The answer was {guessed_number}")
else:
  attempts=5
  while attempts>0:
    user_guess=int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
    attempts-=1
    if user_guess==guessed_number:
      print(f"You guessed it! The number was {guessed_number}")
      attempts=0
    elif user_guess<guessed_number:
      print("Too low!\nGuess again.")
    else:
      print("Too high.\nGuess again.")
  else:
    print(f"You are out of guesses. The answer was {guessed_number}")
