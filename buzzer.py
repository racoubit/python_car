#--------------------------------------------------
#  ベンハムの独楽　駆動用　（ pico )
#--------------------------------------------------
from machine import Pin, PWM
import utime

BUZZER_PIN = 22  # PWM用（ピン番号 4）
buzzer = PWM( Pin( BUZZER_PIN ) )

FREQ = 10
PW = 10    #スピード

melody = [523,587,659,880,0,784,698,659,523,0,523,587,659,988,1020,988,1020,880,784]
nagasa = [1,1,1,4,1,1,1,1,4,1,1,1,4,1,1,1,1,1,4]

for i in range(len(melody)):
    if melody[i] == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(melody[i]) 
        buzzer.duty_u16(30000)
    utime.sleep(nagasa[i]*0.2)
buzzer.duty_u16(0)

     
    