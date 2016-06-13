# -*- encoding: UTF-8 -*-

import time
import argparse
from naoqi import ALProxy

from Moves.FirstMove import execute1

class Nao:
    def __init__(self, ip, port):
        
        self.modules = {}
        self.ip = ip
        self.port = port

        self.module_names = ["ALMotion", "ALRobotPosture", "ALTracker", "ALTextToSpeech"]
        self.fraction_max_speed = 0.8
        self.limit_distance = -0.12
        self.tracker_target_name = "RedBall"
        self.tracker_target_size = 0.06

        self.mode = "Idle"
        self.is_running = False


    def init(self):
        for module_name in self.module_names:
            self.modules[module_name] = ALProxy(module_name, self.ip, self.port)

        self.modules["ALMotion"].wakeUp()
        self.modules["ALTracker"].registerTarget(self.tracker_target_name, self.tracker_target_size)
        self.modules["ALTracker"].setMode("Move")
        self.modules["ALTracker"].setRelativePosition([self.limit_distance, 0.0, 0.0, 0.1, 0.1, 0.3])

        # self.say("Initiliazing")

        self.stand_up()

        # self.say("Initiliazed")

    def uninit(self):
        # self.say("Unitializing")
        self.stop()

        self.modules["ALTracker"].unregisterAllTargets()
        self.modules["ALMotion"].rest()
        
        # self.say("Unitialized")


    def stand_up(self):
        self.modules["ALRobotPosture"].goToPosture("StandInit", self.fraction_max_speed)
        if self.is_running:
            self.mode = "Running"
        else:
            self.mode = "Idle"

    def sit_down(self):
        self.modules["ALRobotPosture"].goToPosture("Sit", self.fraction_max_speed)
        self.mode = "Idle"

    def crouch(self):
        self.modules["ALRobotPosture"].goToPosture("Crouch", self.fraction_max_speed)
        self.mode = "Idle"

    def start(self):
        self.modules["ALTracker"].track(self.tracker_target_name)
        self.mode = "Running"
        self.is_running = True

    def stop(self):
        self.modules["ALTracker"].stopTracker()
        self.mode = "Idle"
        self.is_running = False

    def point_at(self, arms="Arms"):        
        self.modules["ALTracker"].pointAt(arms, self.modules["ALTracker"].getTargetPosition(0), 0, self.fraction_max_speed)
        pass

    def say(self, string):
        self.modules["ALTextToSpeech"].say(string)
        pass

    def move1(self):
        execute1(self.modules["ALMotion"])
        pass

    def exit(self):
        self.mode = "Stopped"
        self.is_running = False
        self.uninit()

if __name__ == "__main__" :
    def user_input():
        user_command = raw_input("Nao [{0}]: ".format(nao.mode))

        if "nao." not in user_command:
            user_command = "nao." + user_command

        if "(" not in user_command:
            user_command += "()"

        return user_command

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number.")

    args = parser.parse_args()

    nao = Nao(args.ip, args.port)
    nao.init()

    do_loop = True

    while do_loop:
        user_command = user_input()

        if user_command == "nao.exit()":
            do_loop = False

        try:
            eval(user_command)
        except Exception, e:
            print "Error: {0}".format(e)