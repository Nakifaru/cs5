#
# hw0pr2if.py
#

""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.
"""

import time

def adventure():
    """This function runs one session of interactive fiction
       Well, it's "fiction," depending on the pill color chosen...
       Arguments: no arguments (prompted text doesn't count as an argument)
       Results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    user_name = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", user_name, " to the Libra Complex, a labyrinth")
    print("of weighty wonders and unreal quantities...of poptarts!")
    print()

    print("Your quest: To find--and partake of--a poptart!")
    print()
    flavor = input("What flavor do you seek? ")
    if flavor == "strawberry":
        print("Wise! You show deep poptart experience.")
    elif flavor == "s'mores":
        print("The taste of the campfire: well chosen, adventurer!")
    else:
        print("Each to their own, then.")
    print()

    print("On to the quest!\n\n")
    print("A corridor stretches before you; its dim lighting betrays, to")
    print("one side, a table supporting nameless forms of inorganic bulk")
    print("and, to the other, a door ajar, leaking laughter--is that")
    print("laughter?--of lab-goers.")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose the table or the door? [table/door] ")
    print()

    if choice1 == "table":
        print("As you approach the table, its hazy burdens loom ever larger,")
        print("until...")
        time.sleep(delay)
        print("...they resolve into unending stacks of poptarts, foil")
        print("shimmering.  You succeed, sumptuously, in sating the")
        print("challenge--and your hunger.")
        print("Go well,", user_name, "!")

    else:  
        print("You push the door into a gathering of sagefowl, athenas,")
        print("and stags alike, all relishing their tasks. Teamwork and")
        print("merriment abound here, except...")
        time.sleep(delay)
        print("...they have consumed ALL of the poptarts! Drifts of wrappers")
        print("coat the floor.  Dizzy, you grasp for a pastry. None is at")
        print("hand. You exhale and slip under the teeming tide of foil as")
        print("it finishes winding around you.")
        print("Farewell,", user_name, ".")


def my_adventure():


    kitten = input("Welcome cat lover. What do you want to name your new kitten? ")

    if kitten:
        print(f"{kitten} is a beautiful name.")

    print(f"You take {kitten} home with you in the evening. {kitten} yawns as you walk through the door?")

    action_1 = input("What do you do? pet or feed: ")

    if action_1 == "pet":
        print("Meow! Meow! Purr!")
    else:
        print("Munch, munch! Mmmmmh! Yum.")

    action_2  = input(f"It's time for bed, where do you put {kitten} to sleep? [outside, litterbox, bed]: ")

    if action_2 == "bed":
        print("Purr!")
    elif action_2 == "litterbox":
        print("Stretch back and forth. Roll into a ball. Meow to sleep.")
    elif action_2 == "outside":
        print("Scratch arms!")


    action_3 = input(f"You're woken up by meowing. Do you leave bed? ")

    if action_3 == "yes":
        print(f"You give {kitten} milk and go back to sleep")
    elif action_3 == "no":
        print("It stays noisy till morning and you never get to fall asleep again.")
    else:
        print("You sleep like a baby.")


    action_4 = input(f"How long do you keep {kitten} afterwards?[day, week, year]: ")
    
    if action_4 == "day":
        print("Boo hoo.")
    elif action_4 == "week":
        print("Meow meow")
    elif action_4 == "year":
        print("Meow")
    else:
        print("Purr!")
        