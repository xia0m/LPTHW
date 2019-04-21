from sys import exit


def gold_room():
    print("This room is ful of gold. HOw much do you take?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you'are not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastart!")


def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fa bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear loosk at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chew your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("he, it, whatever stares at your and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("Whic one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

# STUDY DRILLS
# 1. Draw a map of the game and how you flow through it.

# 2. Fix all of your mistakes, including spelling mistakes.

# 3. Write comments for the functions you do not understand.

# 4. Add more to the game. What can you do to both simplify and expand it?

# 5. The gold_room has a weird way of getting you to type a number. What are all the bugs in this way of doing it? Can you make it better than what I’ve written? Look at how int() works for clues.
