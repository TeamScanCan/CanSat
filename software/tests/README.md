# Software Tests

This directory contains all the code from our software tests.

### bme680.py
Gathers the temperature and pressure data from bme680. That data is printed and saved to data_bme680.json

Dependencies: [bme680-python](https://github.com/pimoroni/bme680-python)

`Testing Status: Complete`

### imu.py
Gathers acceleration and gyro data from IMU. That data is printed and saved to data_imu.json

Dependencies: [adafruit_lsm6ds](https://github.com/adafruit/Adafruit_LSM6DS)

`Testing Status: Complete code, output correctness not verified`

### lora.c
Modified ping example, based on sx1278-LoRa-RaspberryPi library.

Dependencies: [sx1278-LoRa-RaspberryPi](https://github.com/YandievRuslan/sx1278-LoRa-RaspberryPi)

`Testing Status: Complete`

### camera.py
Saves images every 0.2s into `images/` folder.

Dependencies: [picamera2](https://github.com/raspberrypi/picamera2)

`Testing Status: Complete`