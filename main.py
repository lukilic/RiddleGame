class Game(object):

    def __init__(self, player_name):
        self.player = Player(player_name)
        self.death = False
        self.playing()

    def playing(self):
        while room.room_name != "Boss room":
            self.input = raw_input("What do you do: ")

            if self.input.lower() == "look around":
                self.player.lookAround(room)

            elif self.input.lower() == "i" or self.input.lower() == "inv" or \
                 self.input.lower() == "inventory":
                self.player.displayInventory()

            elif self.input.lower() == "open":
                self.player.open(room)

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

        self.answer = raw_input("Your answer: ")
        self.guessed = False
        self.used_item = False

        while self.answer.lower() != "stamp":
            if self.answer.lower() == "hint" and "Hint rifle" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Hint rifle")
                print "Hint: It's required to send mail."
                self.answer = raw_input("Your answer: ")

            elif self.answer.lower() == "skip" and "Skip gun" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Skip gun")
                print "Very well, you get a second chance."
                print ""
                print "What can you catch but not throw?"

                self.answer = raw_input("Your answer: ")

                while self.answer.lower() != "cold":
                    print "Incorrect answer: "
                    self.answer = raw_input("Your answer: ")

                self.guessed = True
                print "Well well, you got the first one right, congratulations."
                print "Time for a second riddle."
                print ""

            elif self.guessed is False:
                print "Incorrect answer: "
                self.answer = raw_input("Your answer: ")

            else:
                break

        if self.answer.lower() == "stamp":
            print "Well well, you got the first one right, congratulations."
            print "Time for a second riddle."
            print ""

        print "Second riddle:"
        print ""
        print "What invention lets you look right through a wall?"

        self.answer = raw_input("Your answer: ")
        self.guessed = False
        self.used_item = False

        while self.answer.lower() != "window":
            if self.answer.lower() == "hint" and "Hint rifle" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Hint rifle")
                print "Hint: It's plural form is making someone a ton of money."
                self.answer = raw_input("Your answer: ")

            elif self.answer.lower() == "skip" and "Skip gun" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Skip gun")
                print "You're lucky you had that one with you."
                print ""
                print "Feed me and I live, yet give me a drink and I die. What am I?"

                self.answer = raw_input("Your answer: ")

                while self.answer.lower() != "fire":
                    print "Incorrect answer: "
                    self.answer = raw_input("Your answer: ")

                self.guessed = True
                print "Two in a row? How can this be!?"
                print "It's time I put an end to this."
                print ""

            elif self.guessed is False:
                print "Incorrect answer: "
                self.answer = raw_input("Your answer: ")

            else:
                break

        if self.answer.lower() == "window":
            print "Two in a row? How can this be!?"
            print "It's time I put an end to this."
            print ""

        print "The last one. You guess it, You live."
        print "But if you don't... there's no failure state so it's just a matter of time."
        print "The final riddle:"
        print ""
        print "What is as light as a feather, but even the world's strongest man couldn't hold it for more than a minute?"

        self.answer = raw_input("Your answer: ")
        self.guessed = False
        self.used_item = False

        while self.answer.lower() != "breath":
            if self.answer.lower() == "hint" and "Hint rifle" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Hint rifle")
                print "Hint: You lose it when you sprint."
                self.answer = raw_input("Your answer: ")

            elif self.answer.lower() == "skip" and "Skip gun" in Player.inventory and self.used_item is False:
                self.used_item = True
                Player.inventory.remove("Skip gun")
                print "Noo, not the skip gun!."
                print ""
                print "What starts with the letter 't', is filled with 't' and ends in 't' ?"

                self.answer = raw_input("Your answer: ")

                while self.answer.lower() != "teapot":
                    print "Incorrect answer: "
                    self.answer = raw_input("Your answer: ")

                self.guessed = True
                print "It can't be!! You actually won!"
                print "Curseeeess!!"
                print ""
                print "Congratulations on beating my first game!"

            elif self.guessed is False:
                print "Incorrect answer: "
                self.answer = raw_input("Your answer: ")

            else:
                break

        if self.answer.lower() == "breath":
            print "It can't be!! You actually won!"
            print "Curseeeess!!"
            print ""
            print "Congratulations on beating my first game!"


class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name

    def description(self, room_name):
        if self.room_name == "Hall":
            self.hall = Hall(self.room_name)
            self.hall.description()

        elif self.room_name == "Second hall":
            self.sec_hall = SecondHall(self.room_name)
            self.sec_hall.description()

        elif self.room_name == "Armory":
            self.armory = Armory(self.room_name)
            self.armory.description()

        elif self.room_name == "Lounge":
            self.lounge = Lounge(self.room_name)
            self.lounge.description()

        elif self.room_name == "Final hall":
            self.final_hall = FinalHall(self.room_name)
            self.final_hall.description()

    def unlockables(self, room_name):
        if self.room_name == "Hall":
            self.hall.unlockDoor()

        elif self.room_name == "Second hall":
            self.sec_hall.unlockDoor()

        elif self.room_name == "Armory":
            self.armory_unlocks = raw_input("What would you like to unlock: ")

            if self.armory_unlocks.lower() == "table" or self.armory_unlocks.lower() == "table drawer":
                self.armory.unlockTableDrawer()

            elif self.armory_unlocks.lower() == "door":
                self.armory.unlockDoor()

        elif self.room_name == "Lounge":
            self.lounge_unlocks = raw_input("What would you like to unlock: ")

            if self.lounge_unlocks.lower() == "wardrobe":
                self.lounge.unlockWardrobe()

            elif self.lounge_unlocks.lower() == "door":
                self.lounge.unlockDoor()

        elif self.room_name == "Final hall":
            self.final_hall.unlockBossDoor()

class SecondHall(Room):

    def description(self):
        print "It's dark, you only see flashing sign above the door to your left."
        print "It says 'Armory'."

    def unlockDoor(self):
        print "Another locked door, another little screen popping out. It reads:"
        print ""
        print "Which word in the dictionary is spelled incorrectly?"

        self.answer = raw_input("Your answer: ")

        while self.answer.lower() != "incorrectly":
            print "Incorrect answer, try again."
            self.answer = raw_input("Your answer: ")

        print "The computer prints 'Correct' and the door opens."
        print "You find yourself in another room."

        room.room_name = "Armory"

class Hall(Room):

    def description(self):
        print "You're in a dark hallway. Your back is pressed against some rubble"
        print "that sealed the way back. The only way to go is forward but some kind"
        print "of door stands in your way."

    def unlockDoor(self):
        print "You try to open the door, but it's locked. Little computer screen shows up"
        print "and it shows the following text: "
        print ""
        print "What is greater than God, more evil than the devil, "
        print "the poor have it, the rich need it, and if you eat it, you'll die?"

        self.answer = raw_input("Your answer: ")

        while self.answer.lower() != "nothing":
            print "Incorrect answer, try again."
            self.answer = raw_input("Your answer: ")

        print "The computer prints 'Correct' and the door opens."
        print "You find yourself in another room."

        room.room_name = "Second hall"

class Armory(Room):

    unlocked_drawer = False
    unlocked_chest = False

    def description(self):
        print "It's trashed. Chunks of metal everywhere. You see a woman's body lying on the ground."
        print "There's note next to her. You pick it up. It reads: 'Get rekt fokin feggit xDDD'."
        print "You can't understand what it means, but it might come in handy later, "
        print "so you put it in your pocket."
        print "You see a table on your left and a door to your right."

    def unlockTableDrawer(self):
        if Armory.unlocked_drawer == False:
            print "You naively try to open table drawer, but to no avail."
            print "Yet another computer screen pops out and it challenges you with the following riddle:"
            print ""
            print "If you have me, you want to share me. If you share me, you haven't got me. What am I?"

            self.answer_table = raw_input("Your answer: ")

            while self.answer_table != "secret":
                if self.answer_table.lower() == "quit":
                    break

                elif self.answer_table.lower() != "secret":
                    print "Incorrect answer, try again."
                    self.answer_table = raw_input("Your answer: ")

            if self.answer_table == "secret":
                print "The screen writes 'Correct'. You here a soft beeping sound, drawer slowly opens."
                print "You found a 'Skip gun', looks pretty rusty, but still has some juice in it."
                print "It comes with a note: When the time comes it let's you skip one riddle."
                Player.inventory.append("Skip gun")
                Armory.unlocked_drawer = True

        else:
            print "You already unlocked it."

    def unlockDoor(self):
        print "You approach the door, surprisingly, it's locked. A small screen shows yet again."
        print ""
        print "Take off my skin - I won't cry, but you will! What am I?"

        self.answer_door = raw_input("Your answer: ")

        while self.answer_door.lower() != "onion":
            if self.answer_door.lower() == "quit":
                break

            elif self.answer_door.lower() != "onion":
                print "Incorrect answer, try again."
                self.answer_door = raw_input("Your answer: ")

        if self.answer_door.lower() == "onion":
            print "The screen shows 'Correct' and the door opens. "
            print "You find yourself in another room."
            room.room_name = "Lounge"

class Lounge(Room):

    unlocked_wardrobe = False

    def description(self):
        print "You are in a resting area of sorts. There's bottles and chairs all over the floor."
        print "It's messy and dark, but you manage to find a wardrobe in front of you and a door to your right."

    def unlockWardrobe(self):
        if Lounge.unlocked_wardrobe == False:
            print "It's open!... Just kidding, you're presented with a riddle:"
            print ""
            print "What is at the end of a rainbow?"

            self.answer_wardrobe = raw_input("Your answer: ")

            while self.answer_wardrobe.lower() != "w":
                if self.answer_wardrobe.lower() == "quit":
                    break

                elif self.answer_wardrobe.lower() != "w":
                    print "Incorrect answer"
                    self.answer_wardrobe = raw_input("Your answer: ")

            if self.answer_wardrobe.lower() == "w":
                print "Screen prints 'Correct' and the wardrobe opens."
                print "You picked up a strange rifle, akin to those found in old Alien movies."
                print "Little note on the side says: When the time comes it helps with a small hint."
                Player.inventory.append("Hint rifle")
                Lounge.unlocked_wardrobe = True

        else:
            print "You already opened the wardrobe."

    def unlockDoor(self):
        print "You're presented with another computer lock. You se bloody fingerprints all over it."
        print "It seems someone was already here. They tried to opened the door, but to no avail."
        print "Screen shows the following riddle:"
        print ""
        print "What occurs once in every minute, twice in every moment, yet never in a thousand years?"

        self.answer_door = raw_input("Your answer: ")

        while self.answer_door.lower() != "m":
            if self.answer_door.lower() == "quit":
                break

            elif self.answer_door.lower() != "m":
                print "Incorrect answer, try again."
                self.answer_door = raw_input("Your answer: ")

        if self.answer_door.lower() == "m":
            print "The screen shows 'Correct' and the door opens."
            print "You find yourself in another room."
            room.room_name = "Final hall"

class FinalHall(Room):

    def description(self):
        print "You've come to another hall. There's a big door to your left."
        print "You hear heavy footsteps and loud breathing coming from inside."

    def unlockBossDoor(self):
        print "Computer screen pops up. It says: 'I hope you're ready.', "
        print "followed by the riddle"
        print ""
        print "What kind of room has no doors or windows?"

        self.answer = raw_input("Your answer: ")

        while self.answer.lower() != "mushroom":
            print "Incorrect answer, try again."
            self.answer = raw_input("Your answer: ")

        print "Computer shows 'Correct'."
        print "You're scared, door slowly opens."
        print "You find yourself in another room."

        room.room_name = "Boss room"

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
        room.unlockables(room)

    def lookAround(self, room):
        room.description(room)

player_name = raw_input("Enter player name: ")
print "You wake up. It seems your spaceship is on some sort of lockdown."
print "You stand up knowing you have to find out what happened."
print "Type 'help' to see list of available commands"
room = Room("Hall")
game_stage = Game(player_name)
