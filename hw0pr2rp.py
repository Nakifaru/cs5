#
# hw0pr2rps.py
#
import random       # imports a library (named random)
                    # for making random choices

user_name = input("What is your name? ")
print("Welcome,", user_name, "!")
print()

print("Ready for RPS? Choose wisely!!")
user_choice = input("Which do you choose? (rock/paper/scissors):")
comp_choice = random.choice(["rock","paper","scissors"])
print()

# We print both choices
print("You chose", user_choice)
print("  I chose", comp_choice)
print()


# We can handle different possibilities with nested conditionals

if user_choice == "rock":
  if comp_choice == "rock":
    print("Aargh! We tied (but my rock was rockier!)")
  elif comp_choice == "paper":
    print("I win! My paper outclasses any rock!")
  else:
    print('Alack! Your rock cast my scissors asunder.')

if user_choice == "paper":
  if comp_choice == "rock":
    print("Ouch! You wrapped me up and won~)")
  elif comp_choice == "paper":
    print("Let's go again!")
  else:
    print('Hahaha! I\'ve cut you up!')

if user_choice == "scissors":
  if comp_choice == "rock":
    print("I've crushed you up!)")
  elif comp_choice == "paper":
    print("Oh no! You've won.")
  else:
    print('Looks like it\'s a stalemate.')

print()
print("Try again!")
