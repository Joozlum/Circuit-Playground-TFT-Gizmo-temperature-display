# TFT Gizmo Circuit Playground Temperature Display

This project is for a simple temperature display that shows the current temperature along with a graph that displays past temperature readings.

Needed hardware:

+ Circuit Playground Bluefruit
+ TFT Gizmo digital display

Required modules:

+ adafruit_st7789.mpy
+ adafruit_thermistor.mpy
+ adafruit_gizmo (folder/module)
+ adafruit\_display\_text (folder/module)

## Setup
Connect Circuit Playground Bluefruit device to computer using a USB cable.

If there is code already on it from a previous project, remember to **save a backup!**

If there is no lib folder already on the CIRCUITPY drive, create one and then paste into it the required modules.

If there already is a lib folder, make sure it contains the required modules.

Copy code.py, mini\_text.py, and temp\_avg.py into the CIRCUITPY drive in the root directory (this should be the same place where the lib folder sits).

It should automatically restart and run the code after copying.  