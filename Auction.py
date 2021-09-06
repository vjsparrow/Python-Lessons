from replit import clear

bid_dict={}

def bid():
  names=input("What is your name?\n")
  bid_amount=int(input("what's your bid?\n"))

  bid_dict[names]=bid_amount

  recur=input("Would you like to bid again? Yes or No: \n").lower()

  if recur=="yes":
    clear()
    bid()
  else:
    clear()
    max_bid=0
    for i in bid_dict:
      if bid_dict[i]>max_bid:
        max_bid=bid_dict[i]
        winner=i
    print(f"The winner is {winner}")

bid()
