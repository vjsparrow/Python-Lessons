# Ask if the user wants to play the game
import random
# Deal two cards for the player and one for the dealer
# Keep track of scores

cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_deck=[]
dealer_deck=[]
player_score=0
dealer_score=0
### Maybe wrap it in a function?
def initial(player_deck,player_score,dealer_deck,dealer_score):
  print("**********************************")
  play=input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
  if play=="y":

    for i in (0,1):
      player_deck.append(random.choice(cards_value))
      player_score+=int(player_deck[i])
    if player_score==21:
      print(f"Your cards: {player_deck}, current score is: {player_score}")
      print(f"Jackpot! You win!")
      initial([],0,[],0)

    dealer_deck.append(random.choice(cards_value))
    dealer_score=int(dealer_deck[0])

    print(f"Your cards: {player_deck}, your score is: {player_score}")
    print(f"Dealer cards: {dealer_deck}, dealer's score is: {dealer_score}")

    deal_stand=input("Would you like another card? Type 'y' for Yes and 'n' for pass: ").lower()
    if deal_stand=="y":
      deal(player_deck,player_score,dealer_deck,dealer_score)
    else:
      stand(player_deck,player_score,dealer_deck,dealer_score)

def deal(player_deck,player_score,dealer_deck,dealer_score):
  player_deck.append(random.choice(cards_value))
  player_score+=int(player_deck[-1])
  if player_deck[-1]==11 and player_score>21:
    player_deck[-1]=1
    player_score=0
    for i in player_deck:
      player_score+=int(i)
  if player_score>21:
    print("**********************************")
    print(f"Your cards: {player_deck}, your score is: {player_score}")
    print(f"Dealer cards: {dealer_deck}, dealer's score is: {dealer_score}")
    print("You went over, you lose!")
    initial([],0,[],0)
  elif player_score==21:
    print("**********************************")
    print(f"Your cards: {player_deck}, your score is: {player_score}")
    print(f"Dealer cards: {dealer_deck}, dealer's score is: {dealer_score}")
    print(f"Jackpot! You win!")
    initial([],0,[],0)
  else:
    print("**********************************")
    print(f"Your cards: {player_deck}, your score is: {player_score}")
    print(f"Dealer cards: {dealer_deck}, dealer's score is: {dealer_score}")

    deal_stand=input("Would you like another card? Type 'y' for Yes and 'n' for pass: ").lower()
    if deal_stand=="y":
      deal(player_deck,player_score,dealer_deck,dealer_score)
    else:
      stand(player_deck,player_score,dealer_deck,dealer_score)

def stand(player_deck,player_score,dealer_deck,dealer_score):
  if dealer_score>player_score:
    print("Dealer wins!")
    initial([],0,[],0)
  else:

    dealer_deck.append(random.choice(cards_value))
    dealer_score+=int(dealer_deck[-1])
    if dealer_score>21 and dealer_deck[-1]==11:
      dealer_deck[-1]=1
      dealer_score=0
      for i in dealer_deck:
        dealer_score+=int(i)
    if dealer_score>21:
      print("**********************************")
      print(f"Your cards: {player_deck}, your score is: {player_score}")
      print(f"Dealer cards: {dealer_deck}, dealer's score is: {dealer_score}")
      print("Dealer went over, you win!")
      initial([],0,[],0)
    elif dealer_score<=21 and dealer_score>player_score:
      print("**********************************")
      print(f"Your cards: {player_deck}, your score is: {player_score}")
      print(f"Dealer cards: {dealer_deck}, dealer's score is: {dealer_score}")
      print("Dealer wins")
      initial([],0,[],0)
    else:
      stand(player_deck,player_score,dealer_deck,dealer_score)

initial([],0,[],0)
