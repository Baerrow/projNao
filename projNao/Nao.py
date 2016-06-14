# -*- encoding: UTF-8 -*-

import time
import sys

import Actions

# from naoqi import ALProxy

class Nao:
    def __init__(self, ip="127.0.0.1", port="9559"):
        
        self.modules = {}
        self.actions = {}
        self.ip = ip
        self.port = port

        self.module_names = ["Motion", "RobotPosture", "Tracker", "TextToSpeech"]
        self.action_names = ["Say", "StandUp"]

        self.fraction_max_speed = 0.8
        self.limit_distance = -0.12
        self.tracker_target_name = "RedBall"
        self.tracker_target_size = 0.06

        self.mode = "Idle"
        self.is_running = False
        self.verbose = False


    def init(self):
        for module_name in self.module_names:
            # self.modules[module_name] = ALProxy("AL" + module_name, self.ip, self.port)
            self.modules[module_name] = "AL" + module_name

        for action_name in self.action_names:
            module_name = "Actions.{0}".format(action_name) # Say => Actions.Say (nom de la classe => nom du module)

            __import__(module_name) # Import du module
            module = sys.modules[module_name] # Récupération du module
            action_class = getattr(module, action_name) # Récupération de la classe

            self.actions[action_name] = action_class(self.modules) # Instanciation de la classe

        # self.motion.wakeUp()
        # self.tracker.registerTarget(self.tracker_target_name, self.tracker_target_size)
        # self.tracker.setMode("Move")
        # self.tracker.setRelativePosition([self.limit_distance, 0.0, 0.0, 0.1, 0.1, 0.3])

        # if (self.verbose):
        #     self.say("Initiliazing")

        # self.stand_up()

        # if (self.verbose):
        #     self.say("Initiliazed")
        pass

    def uninit(self):
        # if (self.verbose):
        #     self.say("Unitializing")

        # self.stop()

        # self.tracker.unregisterAllTargets()
        # self.motion.rest()
        
        # if (self.verbose):
        #     self.say("Unitialized")
        pass

    def __getattr__(self, attribute_name):
        formated_attribute_name = attribute_name[0].upper() + attribute_name[1:] # tracker => Tracker
        
        try:
            return self.actions[formated_attribute_name]
        except KeyError:
            try:
                return self.modules[formated_attribute_name]
            except KeyError:
                raise AttributeError(attribute_name)
        
    def execute(self, string):
        function = string.split(" ")[0] # Le nom de la fonction est ce qu'il y a avant le premier espace
        
        args = string[len(function + " "):] # On retire le nom de la fonction

        try:
            self.actions[function](args)
        except Exception, e:
            raise e


    def exit(self):
        self.mode = "Stopped"
        self.is_running = False
        self.uninit()
    

if __name__ == '__main__':
    nao = Nao()
    nao.init()

    nao.execute("Say hello")
    nao.execute("StandUp 1")

    nao.say("Hello")