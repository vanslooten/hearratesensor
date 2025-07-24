from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(10),  # Here, use your I2C SDA pin (GP.. number, so this is GP10)
                  scl=Pin(11),  # Here, use your I2C SCL pin (GP.. number)
                  freq=400000)  # Fast: 400kHz, slow: 100kHz

print("Starting I2C scan...")
print(i2c.scan())
