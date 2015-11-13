import time
import sys

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

Test = None

class RedBallTracker():
    pass


class TestModule(ALModule):
    # A simple module able to test broker
    def __init__(self, name):
        ALModule.__init__(self, name)

        # Create a proxy to ALTextToSpeech for later use
        self.speech = ALProxy("ALTextToSpeech")
        self.posture = ALProxy("ALRobotPosture")
        self.motion = ALProxy("ALMotion")

        self.posture.goToPosture("StandInit", 0.5)
        self.speech.say("I'm going to move")
        self.motion.moveTo(1, 0, 0)


def main():
    parser = OptionParser()
    parser.add_option("--ip",
                      help="Parent broker port. The IP address or your robot",
                      dest="ip")
    parser.add_option("--port",
                      help="Parent broker port. The port NAOqi is listening to",
                      dest="port",
                      type="int")
    parser.set_defaults(
        ip="127.0.0.1",
        port=55512)

    (opts, args_) = parser.parse_args()
    IP_ADDRESS = opts.ip
    PORT_NUMBER = opts.port

    ''' What I understood about that
        it used to communicate with other modules, and create NAOqi modules.
        it must live until the end of our program
    '''
    myBroker = ALBroker("myBroker", "0.0.0.0", 0, IP_ADDRESS, PORT_NUMBER)

    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global Test
    Test = TestModule("Test")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)

if __name__ == '__main__':
    main()
