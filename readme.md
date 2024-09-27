# Raspberry Pi Pico(1/W/2) MicroPython Projects

This repository contains various MicroPython scripts for the Raspberry Pi Pico, Pico W and some for the Pico 2. Below is a brief explanation of each Python file and instructions on how to run them using Visual Studio Code (VSCode) with the Pico MicroPython library.

## Files

### `blinky.py`
This script blinks an LED connected to the Raspberry Pi Pico.

### `blinkyPWM.py`
This script demonstrates how to use Pulse Width Modulation (PWM) to control the brightness of an LED connected to the Raspberry Pi Pico. It gradually increases and decreases the LED brightness in a loop.

### `webLed.py`
This script sets up a simple web server on the Raspberry Pi Pico W, allowing you to control an LED connected to the Pico via a web interface. You can turn the LED on and off by accessing the web page hosted by the Pico W. You can also set the PWM value of the LED using a slider on the web page. This allows you to control the brightness of the LED dynamically.
It uses the `netman` library to manage network connections.
 


## Running the Scripts

To run these scripts using VSCode with the Pico MicroPython library, follow these steps:

1. **Install VSCode**: If you haven't already, download and install [Visual Studio Code](https://code.visualstudio.com/).

2. **Install the Pico-Go Extension**: Open VSCode and install the `Pico-Go` extension from the Extensions marketplace.

3. **Connect Your Raspberry Pi Pico**: Connect your Raspberry Pi Pico to your computer via USB.

4. **Open the Project Folder**: Open the `/home/codeasm/Projects/ElectronicParts/RaspberryPi/Pico/MicroPython` folder in VSCode.

5. **Select the Python File**: Click on the Python file you want to run (e.g., `blink.py`).

6. **Upload and Run**: Use the Pico-Go extension to upload and run the script on your Raspberry Pi Pico. You can do this by clicking on the "Run" button provided by the extension.

## Additional Resources

- [Raspberry Pi Pico Documentation](https://www.raspberrypi.org/documentation/rp2040/getting-started/)
- [MicroPython Documentation](https://docs.micropython.org/en/latest/)

Feel free to explore and modify the scripts to suit your needs. Happy coding!
