from locorobo import LocoRobo
from locorobo import MotorDirection
from locorobo import Data
from locorobo import WaitType
from locorobo import Song
from locorobo import Note
from numpy import arange #i need this for its float range and step compatibility

def get_robot(robots, name):
    robot = None

    # Search through robots found during the scan for
    # the one we want
    for r in robots.values():
        if r.name == name:
            robot = r

            # We found the robot, so stop the for loop
            break

    # If we did not find the robot during the scan, stop the program
    if not robot:
        raise Exception('Could not find robot with specified name')

    return robot

def main():
    # Tell LocoRobo what serial port to use
    LocoRobo.setup("/dev/tty.usbmodem1")

    # Scan for robots

    robots = LocoRobo.scan(2000)

    # Use get_robots to find robot with name lr 00:07 in the scan result
    robot = get_robot(robots, "lr ce:eb")

    robot.connect()
    robot.activate_motors()
    robot.enable_sensor(Data.ULTRASONIC, False)
    ### Mack-written program starts here ###
    robot.setup_wait(WaitType.TIME, 1000)
    setLight("blue")
    accelerate()
    #robot.move(Motor.FORWARD,Motor.FORWARD,1,1,True)
    ### End of Mack-written program ###
    robot.deactivate_motors()
    robot.disconnect()

def setLight(color):
    # Mack's function to set light using simple call methods
    if color == "white":
        robot.set_light(0, 255,255,255)
    elif color == "black":
        robot.set_light(0, 0,0,0)
    elif color == "blue":
        robot.set_light(0, 46,0,255)
    else:
        pass
    robot.sync_lights()

def accelerate():
    for i in arange(0.0,1.1,.1):
        robot.move(Motor.FORWARD,Motor.FORWARD,i,i,True)

# If we are on the main thread, run the program
if __name__ == "__main__":

    try:
        main()
    except:
        LocoRobo.stop()
        raise

    LocoRobo.stop()

    # For compatibility with webapp's python, we can't use finally.
    # If you are using local python, you can do the following
    #
    # try:
    #     main()
    # finally:
    #     LocoRobo.stop()
