import random

#---this is a function to get the user choices,and randomly select the computer choices
def get_choices():
  player_choice = input("Enter a choice(rock,paper,scissors): ")
  options = ["Rock","paper","scissor"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice , "computer":computer_choice }
  return choices

def check_win(player,computer):
  print( f"you chose {player},computer chose {computer}")
  if player =="rock":
    if computer== "scissors":
      return "rock smashes scissors, you win!"
    elif computer == "paper":
      return "paper coves rock, you lose"
    else:
      return "it a tie."
  elif player =="paper":                                                                
    if computer== "scissors":
      return " scissors cuts paper, you lose!"
    elif computer == "rock":
      return "paper coves rock, you win!"
    else:
      return "it a tie."
  elif player =="scissors":
    if computer== "paper":
      return "scissors cuts paper, you win!"
    elif computer == "rock":
      return "rock smashes scissors you lose"
    else:
      return "it a tie."
  
choices= get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)

  
  