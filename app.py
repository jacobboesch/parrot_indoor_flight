"""
This script will have the drone move forward 5 meters,
then up 3 meters, then back 5 meters, then down 3 meters
"""
import olympe

from olympe.messages.ardrone3.Piloting import TakeOff
from olympe.messages.ardrone3.Piloting import moveBy
from olympe.messages.move import extended_move_by
from olympe.messages.ardrone3.Piloting import Landing
import time

drone = olympe.Drone('10.202.0.1')
drone.connect()

# Speed of drone in meters per second
horizontail_speed = 3.0
vertical_speed = 3.0
# rotation speed in degrees per second
rotation_speed = 90.0

displacement_meters = 5.0
displacement_height_meters = 3.0

assert drone(TakeOff()).wait()
#TODO monitor takeoff action to ensure drone is in the air instead
time.sleep(30)
# TODO monitor drone location before sending next command instead of using thread.sleep
drone(extended_move_by(displacement_meters, 0, 0, 0, horizontail_speed, vertical_speed, rotation_speed)).wait()
time.sleep(10)
drone(extended_move_by(0, 0, -displacement_height_meters, 0, horizontail_speed, vertical_speed, rotation_speed)).wait()
time.sleep(10)
drone(extended_move_by(-displacement_meters, 0, 0, 0, horizontail_speed, vertical_speed, rotation_speed)).wait()
time.sleep(10)
drone(extended_move_by(0, 0, displacement_height_meters, 0, horizontail_speed, vertical_speed, rotation_speed)).wait()
time.sleep(10)
assert drone(Landing()).wait()

drone.disconnect()