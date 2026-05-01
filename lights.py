#Tkinter GUI on top
import tkinter as tk
import RPi.GPIO as GPIO

#GPIO SETUP 

# we use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# assigning GPIO pins to LEDs
living_room = 14
bathroom    = 15
closet      = 16

#set pins as outputs
GPIO.setup(living_room, GPIO.OUT)
GPIO.setup(bathroom,    GPIO.OUT)
GPIO.setup(closet,      GPIO.OUT)

# turn all LEDs off  to ensure only one is active at a time
def turn_off_all():
    GPIO.output(living_room, GPIO.LOW)
    GPIO.output(bathroom,    GPIO.LOW)
    GPIO.output(closet,      GPIO.LOW)

#GUI CONTROL FUNCTION

# is called whenever a radio button is selected
def update_leds():
    selected = room_var.get()

    # always start by turning everything off
    turn_off_all()

    # turn ON only the selected room
    if selected == "living_room":
        GPIO.output(living_room, GPIO.HIGH)

    elif selected == "bathroom":
        GPIO.output(bathroom, GPIO.HIGH)

    elif selected == "closet":
        GPIO.output(closet, GPIO.HIGH)

# safely turn everything off and release GPIO
def on_exit():
    turn_off_all()
    GPIO.cleanup()
    root.destroy()

#TKINTER GUI SETUP

root = tk.Tk()
root.title("Linda's Light Controller")
root.geometry("350x280")
root.resizable(False, False)

# title label
tk.Label(
    root,
    text="Linda’s Light Controller",
    font=("Arial", 14, "bold")
).pack(pady=20)

# instruction label
tk.Label(
    root,
    text="Select a room to turn the light ON:",
    font=("Arial", 11)
).pack()

# radio button variable (starts with nothing selected)
room_var = tk.StringVar(value="")

#RADIO BUTTONS

tk.Radiobutton(
    root,
    text="Living Room",
    variable=room_var,
    value="living_room",
    font=("Arial", 12),
    command=update_leds  # triggers LED update
).pack(anchor="w", padx=60, pady=5)

tk.Radiobutton(
    root,
    text="Bathroom",
    variable=room_var,
    value="bathroom",
    font=("Arial", 12),
    command=update_leds
).pack(anchor="w", padx=60, pady=5)

tk.Radiobutton(
    root,
    text="Closet",
    variable=room_var,
    value="closet",
    font=("Arial", 12),
    command=update_leds
).pack(anchor="w", padx=60, pady=5)

#EXIT BUTTON

tk.Button(
    root,
    text="Exit",
    command=on_exit,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    width=10
).pack(pady=20)

#running the GUI

root.mainloop()
