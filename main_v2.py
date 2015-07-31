def playing(room, player):
    while room.room_name != "Boss room":
        input = raw_input("What do you do: ")

        if input.lower() == "look around":
            print room.description

        elif input.lower() == "i" or input.lower() == "inv" or \
            input.lower() == "inventory":
            player.displayInventory()

        elif input.lower() == "open":
            room.riddle()
            return True

        elif input.lower() == "help":
            print ""
            print "look around - become aware of your surroundings"
            print "open - opens stuff"
            print "i or inv or inventory - shows your inventory"
            print "quit - let's you quit certain riddles"
            print "P.S: Once you enter a room, you can't go back!"
            print ""

        else:
            print "Your command makes no sense."



def boss_riddle(answer):
    answer = raw_input("Your answer: ")
    guessed = False
    used_item = False

    while answer.lower() != answer:
        if answer.lower() == "hint" and "Hint rifle" in Player.inventory and used_item is False:
            used_item = True
            Player.inventory.remove("Hint rifle")

            if answer == "stamp":
                print "Hint: It's required to send mail."
                answer = raw_input("Your answer: ")

            elif answer == "window":
                print "Hint: It's plural form is making someone a ton of money."
                answer = raw_input("Your answer: ")

            else:
                print "Hint: You lose it when you sprint."
                answer = raw_input("Your answer: ")

        elif answer.lower() == "skip" and "Skip gun" in Player.inventory and used_item is False:
            used_item = True
            Player.inventory.remove("Skip gun")
            print "Very well, you get a second chance."
            print ""

            if answer == "stamp":
                print "What can you catch but not throw?"
                answer = raw_input("Your answer: ")

                while answer.lower() != "cold":
                    print "Incorrect answer: "
                    answer = raw_input("Your answer: ")

                guessed = True

            elif answer == "window":
                print "Feed me and I live, yet give me a drink and I die. What am I?"
                answer = raw_input("Your answer: ")

                while answer.lower() != "fire":
                    print "Incorrect answer: "
                    answer = raw_input("Your answer: ")

                guessed = True

            else:
                print "What starts with the letter 't', is filled with 't' and ends in 't' ?"
                answer = raw_input("Your answer: ")

                while answer.lower() != "teapot":
                    print "Incorrect answer: "
                    answer = raw_input("Your answer: ")

                guessed = True

        elif guessed is False:
            print "Incorrect answer: "
            answer = raw_input("Your answer: ")

        else:
            break

class Room(object):

    def __init__(self, room_name, description, unlocks, solutions):
        self.room_name = room_name
        self.description = description
        self.unlocks = unlocks
        self.solutions = solutions

    def riddle(self):
        self.answer = raw_input("What do you want to unlock: ")
        for key in self.unlocks:
            if key == self.answer:
                print self.unlocks[key]
                self.riddle_ans = raw_input("Your answer: ")

                while self.riddle_ans.lower() != self.solutions[key]:
                    print "Incorrect, try again."
                    self.riddle_ans = raw_input("Your answer: ")
                    if self.riddle_ans == "quit" and self.answer != "door":
                        break

class Player(object):

    inventory = []

    def __init__(self, name):
        self.name = name

    def displayInventory(self):
        if len(self.inventory) == 0:
            print "No items in your backpack"
        else:
            print "You currently have: "
            for i in range(len(self.inventory)):
                print self.inventory[i]
def main():
    player_name = raw_input("Enter player name: ")
    player = Player(player_name)

    print "You wake up. It seems your spaceship is on some sort of lockdown."
    print "You stand up knowing you have to find out what happened."
    print "Type 'help' to see list of available commands"

    hall_descript = "You're in a dark hallway. Your back is pressed against some rubble" \
                    "\nthat sealed the way back. The only way to go is forward but some kind" \
                    "\nof door stands in your way."

    hall_unlocks = {"door": "You try to open the door, but it's locked. Little computer screen shows up"
                        "\nand it shows the following text:"
                        "\n\nWhat is greater than God, more evil than the devil,"
                        "\nthe poor have it, the rich need it, and if you eat it, you'll die?"}

    hall_solutions = {"door": "nothing"}

    room = Room("Hall", hall_descript, hall_unlocks, hall_solutions)
    playing(room, player)

    print "The computer prints 'Correct' and the door opens."
    print "You find yourself in another room."

    second_hall_descript = "It's dark, you only see flashing sign above the door to your left." \
                       "\nIt says 'Armory'."

    second_hall_unlocks = {"door": "Another locked door, another little screen popping out. It reads:"
                                "\n\nWhich word in the dictionary is spelled incorrectly?"}

    second_hall_solutions = {"door": "incorrectly"}

    room = Room("Second hall", second_hall_descript, second_hall_unlocks, second_hall_solutions)
    playing(room, player)

    print "The computer prints 'Correct' and the door opens."
    print "You find yourself in another room."

    armory_descript = "It's trashed. Chunks of metal everywhere. You see a woman's body lying on the ground." \
                      "\nThere's note next to her. You pick it up. It reads: 'Get rekt fokin feggit xDDD'." \
                      "\nYou can't understand what it means, but it might come in handy later," \
                      "\nso you put it in your pocket.\nYou see a table on your left and a door to your right."

    armory_unlocks = {"table": "You naively try to open table drawer, but to no avail."
                               "\nYet another computer screen pops out and it challenges you with the following riddle:"
                               "\n\nIf you have me, you want to share me. If you share me, you haven't got me. What am I?",
                      "door": "You approach the door, surprisingly, it's locked. A small screen shows yet again."
                              "\n\nTake off my skin - I won't cry, but you will! What am I?"}

    armory_solutions = {"table": "secret", "door": "onion"}

    room = Room("Armory", armory_descript, armory_unlocks, armory_solutions)
    playing(room, player)

main()
