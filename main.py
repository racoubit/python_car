from machine import Pin
import utime

# Setup DC Motor pins
M1A = Pin(8, Pin.OUT)
M1B = Pin(9, Pin.OUT)
M2A = Pin(10, Pin.OUT)
M2B = Pin(11, Pin.OUT)

# Setup Microswitch pins
S1A = Pin(0, Pin.IN, Pin.PULL_UP)
S1B = Pin(1, Pin.IN, Pin.PULL_UP)
S2A = Pin(2, Pin.IN, Pin.PULL_UP)
S2B = Pin(3, Pin.IN, Pin.PULL_UP)

M1A.value(1)     
M1B.value(0)
M2A.value(1)
M2B.value(0)

while True:
    if S1A.value() == 0 or S1B.value() == 0:
        M1A.value(0)     
        M1B.value(0)
        M2A.value(0)
        M2B.value(0)
        utime.sleep(0.5)
        
        M1A.value(1)
        M1B.value(0)
        M2A.value(1)
        M2B.value(0)
        utime.sleep(2.0)

    if S2A.value() == 0 or S2B.value() == 0:
        M1A.value(0)
        M1B.value(0)
        M2A.value(0)
        M2B.value(0)
        utime.sleep(0.5)
        
        M1A.value(0)     # Duty Cycle must be between 0 until 65535
        M1B.value(1)
        M2A.value(0)     # Duty Cycle must be between 0 until 65535
        M2B.value(1)
        utime.sleep(2.0)

