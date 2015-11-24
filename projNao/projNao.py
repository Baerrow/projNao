import Nao

def main():
    nao = Nao()

    nao.add_proxy("speech", "ALTextToSpeech")
    nao.add_proxy("posture", "ALRobotPosture")
    nao.add_proxy("motion", "ALMotion")
    nao.add_proxy("tracker", "ALTracker")

if __name__ == '__main__':
    main()