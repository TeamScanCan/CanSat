#!/usr/bin/env python

from adafruit_lsm6ds.ism330dhcx import ISM330DHCX
from picamera2 import Picamera2, Preview
import bme680
import time
import L76X
import json
import board

# Setup BME680
try:
    bme_sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    bme_sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

bme_sensor.set_humidity_oversample(bme680.OS_1X)
bme_sensor.set_pressure_oversample(bme680.OS_1X)
bme_sensor.set_temperature_oversample(bme680.OS_1X)
bme_sensor.set_filter(bme680.FILTER_SIZE_1)
bme_sensor.set_gas_status(bme680.DISABLE_GAS_MEAS)
 
# Setup Camera
picam2 = Picamera2()
picam2.start()

# Setup imu
i2c = board.I2C()
imu_sensor = ISM330DHCX(i2c)

# main loop
print("entering main loop...")

i = 0
all_data = []
try:
    while True:
        acc = imu_sensor.acceleration
        data = {
            'acceleration': [round(acc[0], 2), round(acc[1], 2), round(acc[2], 2)],
            'time': time.time(),
        }

        if bme_sensor.get_sensor_data():
            data['temperature'] = round(bme_sensor.data.temperature, 2),
            data['pressure'] = round(bme_sensor.data.pressure, 2)
        all_data.append(data)

        with open("data.json", "w") as json_file:
            json.dump(all_data, json_file, indent=2)

        print("Data: ", data)

        picam2.capture_file(f"images/image_{i}.jpg")
        print(f"Took an image {i}")

        i += 1
except KeyboardInterrupt:
    pass


picam2.close()

