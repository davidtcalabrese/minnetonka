
# function to ask play again or not
def play_again():
  print("Do you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

# big room
def big_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nYou are in a very large room. There are two teenagers here.")
  print("They are playing Minecraft on a larget TV. You see a hallway and some stairs.")
  print("What would you do? (1, 2 or 3)")
  print("1). Ask if you can play Minecraft")
  print("2). Go up the stairs")
  print("3). Go through the hallway")

  # take input()
  answer = input(">")

  if answer == "1":
    game_over("They ask you to show your skill by timing you on a Minecraft speed run. You fail miserably as you have never played before.")
  elif answer == "2":
    # TODO: top_of_stairs_landing()
    game_over("TBD")
  else:
    big_room()

# shop room
def shop_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nThis room appears to an extension of the garage. Theare are shop tools here.")
  print("You see a table saw and a lathe as well as a closed door.")
  print("What would you do? (1 or 2)")
  print("1). Play with the shop tools.")
  print("2). Go through the door.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("You forgot to put on your safty glasses an are blinded by flying chips of metal.")
  elif answer == "2":
    # lead him to the start()
    start()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")

# outside room
def outside_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nYou are now outside of the house.")
  print("You are facing the back yard.")
  print("You can see some stairs leading to a deck above you and a hot tub in front of you.")
  print("What would you like do? (1 or 2)")
  print("1). Get in the hot tub.")
  print("2). Climb up to the deck.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    game_over("Ahh. That feels really realy nice.  You fall asleep in the hot tub.")
  elif answer == "2":
    print("\nYou are now on the deck. Enjoy the view.")
    deck_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")

# deck room
def deck_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nYou are now on a second story deck.")
  print("There is a table with a sun shade and a meal ready to eat.")
  print("You can see some stairs leading to the back yard and a sliding glass door.")
  print("What would you like do? (1, 2 or 3)")
  print("1). Sit down in the shade and eat the meal.")
  print("2). Walk down the stairs to the back yard.")
  print("3). Go through the sliding glass doors.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    game_over("Nice! Brats and hamburgers just off the grill. Delicious.")
  elif answer == "2":
    outside_room()
  elif answer == "3":
    bird_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")

# bird room
def bird_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nYou are now inside the house.")
  print("You see two parakeets flying around in the room with you, as well as a piano.")
  print("You can see a sliding glass door, and an entry way to the kitchen.")
  print("What would you like do? (1, 2 or 3)")
  print("1). Play the piano.")
  print("2). Go through to the kitchen.")
  print("3). Go through the sliding glass doors.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    game_over("The birds hate your playing! They are mad and squawking at you to stop.")
  elif answer == "2":
    # TODO: kitchen_room()
    # kitchen_room()
    game_over("TBD")
  elif answer == "3":
    deck_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")

def start():
  # give some prompts.
  print("\nYou are standing in Schmalz Haus. It is a room in a house on a suburban street in Minnetonka called Brandbury Walk.")
  print("\nYou see several computer monitors and a soldering iron in front of you.")
  print("There is a closed door to your left, a sliding door stright ahead, and an open door to your right that looks like it leads to a hallway? (l, s or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to shop_room()
    shop_room()
  elif "s" in answer:
    # else if player typed "straight" or "s" lead him to outside_room()
    outside_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to big_room()
    big_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()