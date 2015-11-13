from naoqi import ALProxy

IP_ADDRESS = "127.0.0.1"
PORT_NUMBER = 55512

tts = ALProxy("ALTextToSpeech", IP_ADDRESS, PORT_NUMBER)
motion = ALProxy("ALMotion", IP_ADDRESS, PORT_NUMBER)
postureProxy = ALProxy("ALRobotPosture", IP_ADDRESS, PORT_NUMBER)

postureProxy.goToPosture("StandInit", 0.5)
# motion.moveInit()
motion.moveTo(0, 0, 1)
tts.setLanguage("French")
tts.say("Bonjour")

# ''' Whole Body Motion: Head orientation control '''
# ''' This example is only compatible with NAO '''

# import argparse
# import time
# import math
# from naoqi import ALProxy

# def main(IP_ADDRESS = "127.0.0.1", PORT_NUMBER = 54784):
#     ''' Example of a whole body head orientation control
#         Warning: Needs a PoseInit before executing
#                  Whole body balancer must be inactivated at the end of the script
#     '''

#     motionProxy  = ALProxy("ALMotion", IP_ADDRESS, PORT_NUMBER)
#     postureProxy = ALProxy("ALRobotPosture", IP_ADDRESS, PORT_NUMBER)

#     # Wake up robot
#     motionProxy.wakeUp()

#     # Send robot to Stand Init
#     postureProxy.goToPosture("StandInit", 0.5)

#     effectorName = "Head"

#     # Active Head tracking
#     isEnabled    = True
#     motionProxy.wbEnableEffectorControl(effectorName, isEnabled)

#     # Example showing how to set orientation target for Head tracking
#     # The 3 coordinates are absolute head orientation in NAO_SPACE
#     # Rotation in RAD in x, y and z axis

#     # X Axis Head Orientation feasible movement = [-20.0, +20.0] degree
#     # Y Axis Head Orientation feasible movement = [-75.0, +70.0] degree
#     # Z Axis Head Orientation feasible movement = [-30.0, +30.0] degree

#     targetCoordinateList = [
#     [+20.0,  00.0,  00.0], # target 0
#     [-20.0,  00.0,  00.0], # target 1
#     [ 00.0, +70.0,  00.0], # target 2
#     [ 00.0, +70.0, +30.0], # target 3
#     [ 00.0, +70.0, -30.0], # target 4
#     [ 00.0, -75.0,  00.0], # target 5
#     [ 00.0, -75.0, +30.0], # target 6
#     [ 00.0, -75.0, -30.0], # target 7
#     [ 00.0,  00.0,  00.0], # target 8
#     ]

#     # wbSetEffectorControl is a non blocking function
#     # time.sleep allow head go to his target
#     # The recommended minimum period between two successives set commands is
#     # 0.2 s.
#     for targetCoordinate in targetCoordinateList:
#         targetCoordinate = [target*math.pi/180.0 for target in targetCoordinate]
#         motionProxy.wbSetEffectorControl(effectorName, targetCoordinate)
#         time.sleep(3.0)

#     # Deactivate Head tracking
#     isEnabled = False
#     motionProxy.wbEnableEffectorControl(effectorName, isEnabled)

#     # Go to rest position
#     motionProxy.rest()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--ip", type=str, default="127.0.0.1",
#                         help="Robot ip address")
#     parser.add_argument("--port", type=int, default=9559,
#                         help="Robot port number")

#     args = parser.parse_args()
#     main(args.ip, args.port)


# """ Say 'hello, you' each time a human face is detected

# """

# import sys
# import time

# from naoqi import ALProxy
# from naoqi import ALBroker
# from naoqi import ALModule

# from optparse import OptionParser

# NAO_IP = "nao.local"


# # Global variable to store the HumanGreeter module instance
# HumanGreeter = None
# memory = None


# class HumanGreeterModule(ALModule):
#     """ A simple module able to react
#     to facedetection events

#     """
#     def __init__(self, name):
#         ALModule.__init__(self, name)
#         # No need for IP and port here because
#         # we have our Python broker connected to NAOqi broker

#         # Create a proxy to ALTextToSpeech for later use
#         self.tts = ALProxy("ALTextToSpeech")

#         # Subscribe to the FaceDetected event:
#         global memory
#         memory = ALProxy("ALMemory")
#         memory.subscribeToEvent("FaceDetected",
#             "HumanGreeter",
#             "onFaceDetected")

#     def onFaceDetected(self, *_args):
#         """ This will be called each time a face is
#         detected.

#         """
#         # Unsubscribe to the event when talking,
#         # to avoid repetitions
#         memory.unsubscribeToEvent("FaceDetected",
#             "HumanGreeter")

#         self.tts.say("Hello, sweetheart")

#         # Subscribe again to the event
#         memory.subscribeToEvent("FaceDetected",
#             "HumanGreeter",
#             "onFaceDetected")


# def main():
#     """ Main entry point

#     """
#     parser = OptionParser()
#     parser.add_option("--ip",
#         help="Parent broker port. The IP address or your robot",
#         dest="ip")
#     parser.add_option("--port",
#         help="Parent broker port. The port NAOqi is listening to",
#         dest="port",
#         type="int")
#     parser.set_defaults(
#         ip=NAO_IP,
#         port=9559)

#     (opts, args_) = parser.parse_args()
#     ip   = opts.ip
#     port = opts.port

#     # We need this broker to be able to construct
#     # NAOqi modules and subscribe to other modules
#     # The broker must stay alive until the program exists
#     myBroker = ALBroker("myBroker",
#        "0.0.0.0",   # listen to anyone
#        0,           # find a free port and use it
#        ip,         # parent broker IP
#        port)       # parent broker port


#     # Warning: HumanGreeter must be a global variable
#     # The name given to the constructor must be the name of the
#     # variable
#     global HumanGreeter
#     HumanGreeter = HumanGreeterModule("HumanGreeter")

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print
#         print "Interrupted by user, shutting down"
#         myBroker.shutdown()
#         sys.exit(0)



# if __name__ == "__main__":
#     main()



# ''' Whole Body Motion: Left or Right Arm position control '''
# ''' This example is only compatible with NAO '''

# import argparse
# import motion
# import time
# from naoqi import ALProxy

# def main(robotIP, PORT, chainName):
#     ''' Example of a whole body Left or Right Arm position control
#         Warning: Needs a PoseInit before executing
#                  Whole body balancer must be inactivated at the end of the script
#     '''

#     motionProxy  = ALProxy("ALMotion", robotIP, PORT)
#     postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

#     # Wake up robot
#     motionProxy.wakeUp()

#     # Send robot to Stand Init
#     #postureProxy.goToPosture("StandInit", 0.5)

#     frame     = motion.FRAME_ROBOT
#     useSensor = False

#     effectorInit = motionProxy.getPosition(chainName, frame, useSensor)

#     # Active LArm tracking
#     isEnabled = True
#     motionProxy.wbEnableEffectorControl(chainName, isEnabled)

#     # Example showing how to set position target for LArm
#     # The 3 coordinates are absolute LArm position in FRAME_ROBOT
#     # Position in meter in x, y and z axis.

#     # X Axis LArm Position feasible movement = [ +0.00, +0.12] meter
#     # Y Axis LArm Position feasible movement = [ -0.05, +0.10] meter
#     # Y Axis RArm Position feasible movement = [ -0.10, +0.05] meter
#     # Z Axis LArm Position feasible movement = [ -0.10, +0.10] meter

#     coef = 1.0
#     if chainName == "LArm":
#         coef = +1.0
#     elif chainName == "RArm":
#         coef = -1.0

#     targetCoordinateList = [
#     [ +0.12, +0.00*coef, +0.00], # target 0
#     [ +0.12, +0.00*coef, -0.10], # target 1
#     [ +0.12, +0.05*coef, -0.10], # target 1
#     [ +0.12, +0.05*coef, +0.10], # target 2
#     [ +0.12, -0.10*coef, +0.10], # target 3
#     [ +0.12, -0.10*coef, -0.10], # target 4
#     [ +0.12, +0.00*coef, -0.10], # target 5
#     [ +0.12, +0.00*coef, +0.00], # target 6
#     [ +0.00, +0.00*coef, +0.00], # target 7
#     ]


#     # wbSetEffectorControl is a non blocking function
#     # time.sleep allow head go to his target
#     # The recommended minimum period between two successives set commands is
#     # 0.2 s.
#     for targetCoordinate in targetCoordinateList:
#         targetCoordinate = [targetCoordinate[i] + effectorInit[i] for i in range(3)]
#         motionProxy.wbSetEffectorControl(chainName, targetCoordinate)
#         time.sleep(4.0)

#     # Deactivate Head tracking
#     isEnabled    = False
#     motionProxy.wbEnableEffectorControl(chainName, isEnabled)

#     # Go to rest position
#     motionProxy.rest()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--ip", type=str, default="127.0.0.1",
#                         help="Robot ip address")
#     parser.add_argument("--port", type=int, default=9559,
#                         help="Robot port number")
#     parser.add_argument("--chain", type=str, default="LArm",
#                         choices=["LArm", "RArm"], help="Chain name")

#     args = parser.parse_args()
#     main(args.ip, args.port, args.chain)