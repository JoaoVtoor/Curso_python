"""
Constant = 'Variables' that dont change
Many conditions in the same if (bad)
    <- Complexity count (bad)
"""

speed = 61  # current car speed
local_car = 99  # where the car is on the road

RADAR_1 = 60  # maximum radar speed 1
LOCAL_1 = 100  # where the radar 1 is located
RADAR_RANGE = 1  # the distance where the radar catches

car_speed_pass_radar_1 = speed > RADAR_1
car_pass_radar_1 = local_car >= (LOCAL_1 - RADAR_RANGE) and \
    local_car <= (LOCAL_1 + RADAR_RANGE)
fine_car_radar_1 = car_pass_radar_1 and car_speed_pass_radar_1

if car_speed_pass_radar_1:
    print('The car exceeded the speed limit')

if car_pass_radar_1:
    print('Car passed radar 1')

if fine_car_radar_1:
    print('The driver was fined')