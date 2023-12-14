#!/usr/bin/env python

"""
This script gathers acceleration and gyro data from IMU. That data is printed and saved to data_imu.json
"""

import time
import json
import board
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX

i2c = board.I2C()
sensor = ISM330DHCX(i2c)

print("""imu.py - Displays temperature and pressure, saves to data_imu.json.

Press Ctrl+C to exit!

""")

all_data = []

while True:
    data = {
        'acceleration': sensor.acceleration,
        'gyro': sensor.gyro,
        'time': time.time(),
    }
    all_data.append(data)
    with open("data_imu.json", "w") as json_file:
        json.dump(all_data, json_file, indent=2)
    print(data)
    time.sleep(1)


