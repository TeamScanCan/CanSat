#!/usr/bin/env python

"""
This sciript gathers the temperature and pressure data from bme680. That data is printed and saved to data.json
"""

import bme680
import time
import json
 
print("""read-all.py - Displays temperature and pressure, saves to data.json.
 
Press Ctrl+C to exit!
 
""")
 
sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
 
# These oversampling settings can be tweaked to change the balance between accuracy and noise in the data.
 
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
 
print('\n\nInitial reading:')
for name in dir(sensor.data):
    value = getattr(sensor.data, name)
 
    if not name.startswith('_'):
        print('{}: {}'.format(name, value))
 
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)
 

print('\n\nPolling:')
all_data = []
try:
    while True:
        if sensor.get_sensor_data():
            data = {
                'temperature': sensor.data.temperature,
                'pressure': sensor.data.pressure,
                'time': time.time(),
            }
            all_data.append(data)
            with open("data.json", "w") as json_file:
                json.dump(all_data, json_file, indent=2)
            print(data)
        # 1 second delay
        time.sleep(1)
 
except KeyboardInterrupt:
    pass
