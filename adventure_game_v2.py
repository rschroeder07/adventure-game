import time
import random


def print_pause(message_to_print, pause=2):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option == response:
                return response
        print_pause("Sorry I don't understand.")


def intro():
    print_pause("You find yourself in self isolation at home in a "
                "once bustling city.")
    print_pause("There is a lethal virus spreading and has been "
                "terrifying all those in its path.")
    print_pause("The mass panic caused by this invisible threat "
                "has caused a shortage of basic supplies.")
    print_pause("You must now venture into the world for the most "
                "essential supply, toilet paper!")
    print_pause("You stand in the foyer of your home.")


def outside(items, color, material):
    print_pause("You cautiously open the front door.")
    if "mask" in items and "gloves" in items:
        print_pause("You put on your " + color + " bandana, "
                    "covering your nose and mouth.")
        print_pause("And you slip on the " + material + " gloves.")
        print_pause("You're ready to go to the store!")
        print_pause("Congrats you win!")
        play_again(items, color, material)
    else:
        print_pause("Something doesn't feel right, like "
                    "you're forgeting something.")
        response = valid_input("Do you want to go back inside? "
                               "(yes/no)\n", ["yes", "no"])
        if response == "yes":
            print_pause("Good call.")
            front_door(items, color, material)
        elif response == "no":
            print_pause("Oh no! You forgot an important piece of your PPE!")
            print_pause("You have been infected with the virus...")
            print_pause("Sorry you lose.")
            play_again(items, color, material)


def bedroom(items, color, material):
    print_pause("You go upstairs to your bedroom.")
    if "mask" in items:
        print_pause("It looks like you have everything you need from in here.")
        print_pause("You return to the foyer.")
        front_door(items, color, material)
    else:
        print_pause("Upon entering the room you pick up "
                    "your " + color + " bandana from the dresser.")
        print_pause("This can be used as a mask and that is important "
                    "piece for venturing out into public!")
        items.append("mask")
        print_pause("You return to the foyer.")
        front_door(items, color, material)


def kitchen(items, color, material):
    print_pause("You walk to your kitchen.")
    if "gloves" in items:
        print_pause("It looks like you have everything you need from in here.")
        print_pause("You return to the foyer.")
        front_door(items, color, material)
    else:
        print_pause("After searching the cabinets you find "
                    "your " + material + " gloves under the sink.")
        print_pause("You'll definitely need these to avoid touching "
                    "an infected surface.")
        items.append("gloves")
        print_pause("You return to the foyer.")
        front_door(items, color, material)


def front_door(items, color, material):
    print_pause("Where do you want to go?")
    response = valid_input("Enter 1 to leave the house.\n"
                           "Enter 2 to go to the bedroom.\n"
                           "Enter 3 to go to the kitchen.\n",
                           ["1", "2", "3"])
    if response == "1":
        outside(items, color, material)
    elif response == "2":
        bedroom(items, color, material)
    elif response == "3":
        kitchen(items, color, material)


def play_again(items, color, material):
    print_pause("GAME OVER")
    response = valid_input("Would you like to play "
                           "again? (yes/no)\n", ["yes", "no"])
    if response == "yes":
        print_pause("Great, let's go again!")
        items.clear()
        play_game()
    elif response == "no":
        print_pause("Okay, goodbye!")


def play_game():
    items = []
    colors = ["red", "blue", "green", "black", "orange", "purple"]
    gloves = ["leather", "latex", "rubber", "suede"]
    color = random.choice(colors)
    material = random.choice(gloves)
    intro()
    front_door(items, color, material)


if __name__ == "__main__":
    play_game()
