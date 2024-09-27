import netman
import socket
from machine import Pin, PWM
from time import sleep

# based on:
# https://peppe8o.com/getting-started-with-wifi-on-raspberry-pi-pico-w-and-micropython/

led = Pin("LED", Pin.OUT)
pwm = PWM(Pin(20)) # Pin 20 is the breadboard LED for the Pico W

#set the frequency to 2.5kHz
pwm.freq(2500)
country = 'IT'
ssid = 'zakynthos'
password = 'newyork18'

wifi_connection = netman.connectWiFi(ssid,password,country)

html = """<!DOCTYPE html>
<html>
<head> <title>Pico W</title> </head>
<body> <h1>Pico W</h1>
<p>Current status: %s</p>
<p><a href="http://"""+wifi_connection[0]+"""/light/on">Turn ON</a></p>
<p><a href="http://"""+wifi_connection[0]+"""/light/off">Turn OFF</a></p>
<p>Set PWM: <input type="range" min="0" max="65535" value="0" id="pwmSlider" oninput="updatePWM(this.value)"></p>
<script>
function updatePWM(value) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/pwm/" + value, true);
  xhr.send();
}
</script>
<p>by <a href="https://codeasm.com">codeasm.com</a></p>
</body>
</html>
"""


# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Initialize LED status
led.value(0)
stateis = "LED is OFF"

# Listen for connections
while True:
  try:
    cl, addr = s.accept()
    print('client connected from', addr)
    request = cl.recv(1024)
    print(request)

    request = str(request)[0:50] # The [0:50] avoids getting the url directory from referer 
    led_status = request.find('GET / HTTP')
    led_on = request.find('/light/on')
    led_off = request.find('/light/off')
    pwm_led = request.find('/pwm/')
    print( 'led on = ' + str(led_on))
    print( 'led off = ' + str(led_off))
    print( 'pwm = ' + str(pwm_led))
    if pwm_led > 0:
          try:
            pwm_value_str = request.split('/pwm/')[1].split(' ')[0]
            pwm_value = int(pwm_value_str)
            if 0 <= pwm_value <= 65535:
              pwm.duty_u16(pwm_value)
              stateis = f"LED PWM set to {pwm_value}"
            else:
              stateis = "PWM value out of range (0-65535)"
          except (IndexError, ValueError):
            stateis = "Invalid PWM value"
        
    if led_status >0:
      print("LED status request") # No LED action

    if led_on >0:
      print("led on")
      led.value(1)
      stateis = "LED is ON"

    if led_off >0:
      print("led off")
      led.value(0)
      stateis = "LED is OFF"
    

    response = html % stateis

    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()

  except OSError as e:
    cl.close()
    s.close()
    print('connection closed')
    # Recreate the socket to avoid EADDRINUSE error
    s = socket.socket()
    s.bind(addr)
    s.listen(1)