from sys import exit
from random import randint
from textwrap import dedent

class scene(object):

    def enter(self):
        print("This scene is not yet configured .")
        print("subclass it and implement enter() .")
        exit(1)

class Engine(object):

        # When creating an Engine object you give the map containing scenes to its constructor
    def __init__(self, scene_map):
            self.scene_map = scene_map

    # The method which starts playing the scenes
    def play(self):

        # the opening scene from the map is selected as the current scene
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

         # You loop all the scenes probably, conditions of this loop are unknown because you haven't posted it entirely.
        while current_scene != last_scene and current_scene is not None:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class deadth(scene):

    quips = [
        "you died ..."
    ]

    def enter(self):
        print(deadth.quips[randint(0, len(self.quips)-1)])
        exit(1)

class centralcorridor(scene):

    def enter(self):

        print(dedent("""
          aliens are in front of you ...
          what you do ...
          shoot
          dodge
          or tell a joke
          """))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
              you choose wrong option ...
              you died
              """))

            return 'deadth'

        elif action == "dodge":
            print(dedent("""
              you choose wrong option
              you died
              """))

            return 'deadth'

        elif action == "tell a joke":
            print(dedent("""
              you choose right option ..
              you go to next level ...
              """))

            return 'leaser_weapon armory'

        else:
            print("does not compute")
            return 'central_corridor'

class leaserweaponarmory(scene):

    def enter(self):
        print(dedent("""
        guess three digit integer code ...
        you are going to the next level ...
        """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guessess = 0

        while guess != code and guessess < 10:
            print("BZZZZZZ")
            guessess += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("you enter right code you go to another level")
            return "the_bridge"

        else:
            print("you're going to be dead")
            return 'deadth'

class thebridge(scene):

    def enter(self):
        print(dedent("""
        you have two options to go to the next level .
        1 throw the bomb
        2 slowly pace the bomb
        what you can do ???
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            you choose wrong option
            you're going to be die
            """))

            return 'deadth'

        elif action == "slowly pace the bomb":
            print(dedent("""
            you choose right option
            you're going to the next level
            """))

            return 'escape_pod'

        else:
            print('does not compute')
            return "the_bridge"

class escapepod(scene):

    def enter(self):

        print(dedent("""
        choose a single digit integer number ..
        if you choose right you're going to the next level ..
        otherwise you are going to be die ...
        """))

        good_pod = randint(1,5)
        guess = input("[pod #] > ")

        if int(guess) != good_pod:
            print("you're going to be die")
            return 'deadth'

        else:
            print("you go to last level")
            return 'finished'

class finished(scene):

    def enter(self):
        print("you won good job .")
        return 'finished'

class map(object):

    scenes = {
    'central_corridor' : centralcorridor(),
    'leaser_weapon' : leaserweaponarmory(),
    'the_bridge' : thebridge(),
    'escape_pod': escapepod(),
    'deadth' : deadth(),
    'finished': finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = map('central_corridor')
a_game = Engine(a_map)
a_game.play()
