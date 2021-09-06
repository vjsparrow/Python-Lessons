import random
from game_data import data
from art import logo,vs

print(logo)

# Create list
search_list=[]
for i in range(2):
  search_list.append(random.choice(data))
score=0
# Print list
def print_list(list1,score):
  print(f"Compare A: {list1[0]['name']}, a {list1[0]['description']}, from {list1[0]['country']}\n{vs}\nCompare B: {list1[1]['name']}, a {list1[1]['description']}, from {list1[1]['country']}")

  if list1[0]['follower_count']>list1[1]['follower_count']:
    answer='a'
  else:
    answer='b'

  user_guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  if user_guess==answer:
    score+=1
    print(f"You're right! Your current score is: {score}")
    search_list[0]=search_list[1]
    search_list[1]=random.choice(data)
    while search_list[0]==search_list[1]:
      search_list[1]=random.choice(data)
    print_list(search_list,score)
  else:
    print(f"You lost! Your score is {score}")

print_list(search_list,0)
