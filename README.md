# Task5.1GUI
Embedded Systems Development – Task 5.1P

Graphical User Interface for Raspberry Pi LED Control
Overview

This project implements a simple Graphical User Interface (GUI) on a Raspberry Pi to control three LEDs representing different rooms: Living Room, Bathroom, and Closet. The system allows the user to select a room using radio buttons, turning ON the corresponding LED while ensuring all others remain OFF.
Hardware Requirements

• Raspberry Pi (with OS installed and VNC enabled)
•	Breadboard
•	3 × LEDs
•	3 × Resistors (220Ω–330Ω)
•	Jumper wires
•	Power supply

Software Requirements

•	Python 3 (pre-installed on Raspberry Pi OS)
•	Tkinter (usually pre-installed)
•	RPi.GPIO library

Circuit Setup

GPIO Pin Mapping:
Room	GPIO Pin
Living Room	GPIO14
Bathroom	GPIO15
Closet	GPIO16

Wiring Instructions:
1.	Connect GPIO pin → Resistor
2.	Connect resistor → LED (long leg/anode)
3.	Connect LED short leg (cathode) → GND

Wokwi Simulation
Wokwi circuit setup(Real setup is done like this too):
 
Part 1: Testing the LEDs (Loop Version)

4.	Open Raspberry Pi desktop via VNC Viewer
5.	Open File Manager
6.	Navigate to /home/pi/
7.	Create a file named led_test.py
8.	Open it with Thonny or Text Editor
9.	Paste the loop testing code and save

Run the test:
cd /home/pi
python3 test.py
Stop the program using CTRL + C (KeyboardInterrupt).

Part 2: GUI Implementation

11.	Navigate to /home/pi/
12.	Create a file named lights.py
13.	Paste the lights.py code
14.	Save the file
Run the GUI:
python3 lights.py

GUI Features:
•	Three radio buttons (Living Room, Bathroom, Closet)
•	Exit button

GUI Behavior:
•	Selecting a room turns ON the corresponding LED
•	Other LEDs turn OFF automatically
•	Exit button safely closes the program

Final Checklist
•	Circuit correctly wired
•	LEDs respond correctly
•	Loop test works
•	GUI launches successfully
•	Radio buttons control LEDs
•	Exit button works properly

Conclusion
This project demonstrates how a Graphical User Interface can simplify interaction with embedded systems, replacing physical switches with a user-friendly software solution.

