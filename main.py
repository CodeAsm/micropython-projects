from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(25))

pwm.freq(2500)
try:
    while True:
            # Increase the duty cycle gradually
        for duty in range(0, 65536, 258):
            pwm.duty_u16(duty)
            sleep(0.005)
            
        # Decrease the duty cycle gradually
        for duty in range(65536, 0, -258):
            pwm.duty_u16(duty)
            sleep(0.005)
except KeyboardInterrupt:
    print("Debug interrupt")
    pwm.duty_u16(0)
    print(pwm)
    pwm.deinit()