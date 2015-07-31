class Game(object):

    def __init__(self, player_name, room):
        self.player = player_name
        self.room = room
        self.playing()

    def playing(self):
        while self.room.room_name != "Boss room":
            self.input = raw_input("What do you do: ")

        if self.input.lower() == "look around":
            print self.room.description

        elif self.input.lower() == "i" or self.input.lower() == "inv" or \
            self.input.lower() == "inventory":
            self.player.displayInventory()

        elif self.input.lower() == "open":
            self.player.open(self.room)

        elif self.input.lower() == "help":
            print ""
            print "look around - become aware of your surroundings"
            print "open - opens stuff"
            print "i or inv or inventory - shows your inventory"
            print "quit - let's you quit certain riddles"
            print "P.S: Once you enter a room, you can't go back!"
            print ""

        else:
            print "Your command makes no sense."


        print "It's dark. You can't see anything."
        print "You hear some kind of animal growling."
        print "You hear footsteps approaching."
        print "They're getting louder and louder."
        print "You can feel them almost beside you."
        print "Finally they stop."
        print ""
        print "Hello" + " " + player_name
        print "You're about to face your final challenge."
        print "Three riddles, you have a minute for each."
        print "To use a hint gun, type 'hint', to use a skip gun, type 'skip'."
        print "You may only use one gun per riddle."
        print "Begin."
        print ""
        print "First riddle: "
        print ""
        print "What goes around the world but stays in a corner?"

        self.riddle("stamp")

        print "Well well, you got the first one right, congratulations."
        print "Time for a second riddle."
        print ""

        print "Second riddle:"
        print ""
        print "What invention lets you look right through a wall?"

        self.riddle("window")

        print "Two in a row? How can this be!?"
        print "It's time I put an end to this."
        print ""

        print "The last one. You guess it, You live."
        print "But if you don't... there's no failure state so it's just a matter of time."
        print "The final riddle:"
        print ""
        print "What is as light as a feather, but even the world's strongest man couldn't hold it for more than a minute?"

        self.riddle("breath")

        print "It can't be!! You actually won!"
        print "Curseeeess!!"
        print ""
        print "Congratulations on beating my first game!"

    def riddle(self, answer):
        self.answer = raw_input("Your answer: ")
        self.guessed = False
        self.used_item = False

        while self.answer.lower() != answer:
            if self.answer.lower() == "hint" and "Hint rifle" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Hint rifle")

                if answer == "stamp":
                    print "Hint: It's required to send mail."
                    self.answer = raw_input("Your answer: ")

                elif answer == "window":
                    print "Hint: It's plural form is making someone a ton of money."
                    self.answer = raw_input("Your answer: ")

                else:
                    print "Hint: You lose it when you sprint."
                    self.answer = raw_input("Your answer: ")

            elif self.answer.lower() == "skip" and "Skip gun" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Skip gun")
                print "Very well, you get a second chance."
                print ""

                if answer == "stamp":
                    print "What can you catch but not throw?"
                    self.answer = raw_input("Your answer: ")

                    while self.answer.lower() != "cold":
                        print "Incorrect answer: "
                        self.answer = raw_input("Your answer: ")

                    self.guessed = True

                elif answer == "window":
                    print "Feed me and I live, yet give me a drink and I die. What am I?"
                    self.answer = raw_input("Your answer: ")

                    while self.answer.lower() != "fire":
                        print "Incorrect answer: "
                        self.answer = raw_input("Your answer: ")

                    self.guessed = True

                else:
                    print "What starts with the letter 't', is filled with 't' and ends in 't' ?"
                    self.answer = raw_input("Your answer: ")

                    while self.answer.lower() != "teapot":
                        print "Incorrect answer: "
                        self.answer = raw_input("Your answer: ")

                    self.guessed = True

            elif self.guessed is False:
                print "Incorrect answer: "
                self.answer = raw_input("Your answer: ")

            else:
                break

class Room(object):

    def __init__(self, room_name, description, unlocks):
        self.room_name = room_name
        self.description = description
        self.unlocks = unlocks

    def riddle(self, solutions):
        self.answer = raw_input("What do you want to unlock: ")
        for key in self.unlocks:
            if key == self.answer:
                print self.unlocks[key]
                self.riddle_ans = raw_input("Your answer: ")

                while self.riddle_ans.lower() != solutions[key]:
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

    def open(self, room):
        pass

    def lookAround(self, room):
        print room.description

player_name = raw_input("Enter player name: ")
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
room = Room("Hall", hall_descript, hall_unlocks)
game_stage = Game(player_name, room)
