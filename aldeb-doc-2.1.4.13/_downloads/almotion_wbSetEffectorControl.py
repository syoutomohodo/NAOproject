# -*- encoding: UTF-8 -*-

import time
import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    motionProxy.wbEnable(True)

    # Example showing how to set orientation target for LArm tracking.
    effectorName = "LArm"

    motionProxy.wbEnableEffectorControl(effectorName, True)
    time.sleep(2.0)
    targetCoordinate = [0.20, 0.12, 0.30]
    motionProxy.wbSetEffectorControl(effectorName, targetCoordinate)

    time.sleep(4.0)
    motionProxy.wbEnable(False)

    # Go to rest position
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
