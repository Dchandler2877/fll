# DO NOT EDIT THIS FILE, IT IS A COMBINATION OF ALL THE FUNCTIONS IN THE functions/
# SUBDIRECTORY OF THIS REPOSITORY

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math
import time
import hub


###
### BEGIN FUNCTION FROM FILE: functions/test_function.py
###

# this is a test function, don't actually use this one
def test_function():
    print("test function")

###
### END FUNCTION FROM FILE: functions/test_function.py
###

###
### BEGIN FUNCTION FROM FILE: functions/easing_functions.py
###

"""
Linear
"""
def LinearInOut(t):
	return t

"""
Quadratic easing functions
"""


def QuadEaseInOut(t):
	if t < 0.5:
	    return 2 * t * t
	return (-2 * t * t) + (4 * t) - 1


def QuadEaseIn(t):
    return t * t


def QuadEaseOut(t):
    return -(t * (t - 2))


"""
Cubic easing functions
"""


def CubicEaseIn(t):
    return t * t * t


def CubicEaseOut(t):
    return (t - 1) * (t - 1) * (t - 1) + 1


def CubicEaseInOut(t):
    if t < 0.5:
    	return 4 * t * t * t
    p = 2 * t - 2
    return 0.5 * p * p * p + 1


"""
Quartic easing functions
"""


def QuarticEaseIn(t):
    return t * t * t * t


def QuarticEaseOut(t):
    return (t - 1) * (t - 1) * (t - 1) * (1 - t) + 1


def QuarticEaseInOut(t):
    if t < 0.5:
        return 8 * t * t * t * t
    p = t - 1
    return -8 * p * p * p * p + 1


"""
Quintic easing functions
"""


def QuinticEaseIn(t):
    return t * t * t * t * t


def QuinticEaseOut(t):
    return (t - 1) * (t - 1) * (t - 1) * (t - 1) * (t - 1) + 1


def QuinticEaseInOut(t):
    if t < 0.5:
        return 16 * t * t * t * t * t
    p = (2 * t) - 2
    return 0.5 * p * p * p * p * p + 1


"""
Sine easing functions
"""


def SineEaseIn(t):
    return math.sin((t - 1) * math.pi / 2) + 1


def SineEaseOut(t):
    return math.sin(t * math.pi / 2)


def SineEaseInOut(t):
    return 0.5 * (1 - math.cos(t * math.pi))


"""
Circular easing functions
"""


def CircularEaseIn(t):
    return 1 - math.sqrt(1 - (t * t))


def CircularEaseOut(t):
    return math.sqrt((2 - t) * t)


def CircularEaseInOut(t):
    if t < 0.5:
        return 0.5 * (1 - math.sqrt(1 - 4 * (t * t)))
    return 0.5 * (math.sqrt(-((2 * t) - 3) * ((2 * t) - 1)) + 1)


"""
Exponential easing functions
"""


def ExponentialEaseIn(t):
    if t == 0:
        return 0
    return math.pow(2, 10 * (t - 1))


def ExponentialEaseOut(t):
    if t == 1:
        return 1
    return 1 - math.pow(2, -10 * t)


def ExponentialEaseInOut(t):
    if t == 0 or t == 1:
        return t

    if t < 0.5:
        return 0.5 * math.pow(2, (20 * t) - 10)
    return -0.5 * math.pow(2, (-20 * t) + 10) + 1


"""
Elastic Easing Functions
"""


def ElasticEaseIn(t):
	return math.sin(13 * math.pi / 2 * t) * math.pow(2, 10 * (t - 1))


def ElasticEaseOut(t):
    return math.sin(-13 * math.pi / 2 * (t + 1)) * math.pow(2, -10 * t) + 1


def ElasticEaseInOut(t):
    if t < 0.5:
        return (
            0.5
            * math.sin(13 * math.pi / 2 * (2 * t))
            * math.pow(2, 10 * ((2 * t) - 1))
        )
    return 0.5 * (
        math.sin(-13 * math.pi / 2 * ((2 * t - 1) + 1))
        * math.pow(2, -10 * (2 * t - 1))
        + 2
    )


"""
Back Easing Functions
"""


def BackEaseIn(t):
    return t * t * t - t * math.sin(t * math.pi)


def BackEaseOut(t):
    p = 1 - t
    return 1 - (p * p * p - p * math.sin(p * math.pi))


def BackEaseInOut(t):
    if t < 0.5:
        p = 2 * t
        return 0.5 * (p * p * p - p * math.sin(p * math.pi))

    p = 1 - (2 * t - 1)

    return 0.5 * (1 - (p * p * p - p * math.sin(p * math.pi))) + 0.5


"""
Bounce Easing Functions
"""


def BounceEaseIn(t):
    return 1 - BounceEaseOut(1 - t)


def BounceEaseOut(t):
    if t < 4 / 11:
        return 121 * t * t / 16
    elif t < 8 / 11:
        return (363 / 40.0 * t * t) - (99 / 10.0 * t) + 17 / 5.0
    elif t < 9 / 10:
        return (4356 / 361.0 * t * t) - (35442 / 1805.0 * t) + 16061 / 1805.0
    return (54 / 5.0 * t * t) - (513 / 25.0 * t) + 268 / 25.0


def BounceEaseInOut(t):
    if t < 0.5:
        return 0.5 * BounceEaseIn(t * 2)
    return 0.5 * BounceEaseOut(t * 2 - 1) + 0.5

###
### END FUNCTION FROM FILE: functions/easing_functions.py
###

###
### BEGIN FUNCTION FROM FILE: functions/motor_rotation_functions.py
###

def motor_to_degrees(degrees=90, power=100, port='A'):
    hub_motor = get_motor_by_letter(port)
    hub_motor.preset(0)
    hub_motor.pwm(power)
    degrees_wanted = degrees

    keep_spinning = True
    while keep_spinning:
        speed, relative_degrees, absolute_degrees, pwm = hub_motor.get()
        if relative_degrees >= degrees_wanted:
            keep_spinning = False 
        if keep_spinning == False:
            hub_motor.brake()

###
### END FUNCTION FROM FILE: functions/motor_rotation_functions.py
###

###
### BEGIN FUNCTION FROM FILE: functions/party_mode.py
###


def party_mode(color_sensor_one = 'C', color_sensor_two = 'D', party_length = 20):
    from random import random
    cs_one = ColorSensor(color_sensor_one)
    cs_two = ColorSensor(color_sensor_two)
    timer = Timer()
    timer.reset()

    # the first half of the party is random lights at random intensities
    while timer.now() < (party_length/2):
        intensity = int(100 * random())
        light_choice = 6 * random()
        if light_choice <= 1:
            cs_one.light_up(intensity, 0, 0)
        elif light_choice <= 2:
            cs_one.light_up(0, intensity, 0)
        elif light_choice <= 3:
            cs_one.light_up(0, 0, intensity)
        elif light_choice <= 4:
            cs_two.light_up(intensity, 0, 0)
        elif light_choice <= 5:
            cs_two.light_up(0, intensity, 0)
        elif light_choice <= 6:
            cs_two.light_up(0, 0, intensity)
        wait_for_seconds(0.05)
    cs_one.light_up_all(0)
    cs_two.light_up_all(0)
    wait_for_seconds(0.2)

    # the second half of the paty is bright blinking lights
    # at random intervals
    toggle = 1
    while timer.now() < party_length:
        wait_time = random() * 0.25
        cs_one.light_up_all(100 * toggle)
        cs_two.light_up_all(100 * toggle)
        wait_for_seconds(wait_time)
        if toggle == 1:
            toggle = 0
        else:
            toggle = 1

    # turn off the lights at the end of the party
    cs_one.light_up_all(0)
    cs_two.light_up_all(0)


###
### END FUNCTION FROM FILE: functions/party_mode.py
###

###
### BEGIN FUNCTION FROM FILE: functions/utillity_functions.py
###

def get_motor_by_letter(port):
    if port ==  'A':
        return hub.port.A.motor
    if port == 'B':
        return hub.port.B.motor
    if port == 'C':
        return hub.port.C.motor
    if port == 'D':
        return hub.port.D.motor
    if port == 'E':
        return hub.port.E.motor
    if port == 'F':
        return hub.port.F.motor

###
### END FUNCTION FROM FILE: functions/utillity_functions.py
###
