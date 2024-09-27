from machine import Pin, PWM
from time import sleep

# Comment out the line below for the Pico you are not using:
#pwm = PWM(Pin(25)) # Pin 25 is the onboard LED for the Pico2 and normal Pico
pwm = PWM(Pin(20)) # Pin 20 is the breadboard LED for the Pico W

#set the frequency to 2.5kHz
pwm.freq(2500)
try:
    while True:
            # Increase the duty cycle gradually
        for duty in range(0, 65536, 258): # 0 to 65536 in steps of 258
            pwm.duty_u16(duty)
            sleep(0.005)
            
        # Decrease the duty cycle gradually
        for duty in range(65536, 0, -258):
            pwm.duty_u16(duty)
            sleep(0.005)

# Press Ctrl+C to stop the program
except KeyboardInterrupt:
    print("Debug interrupt")
    pwm.duty_u16(0)
    print(pwm)
    pwm.deinit()