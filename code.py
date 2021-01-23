import array
import math
import board
import displayio
import terminalio
import adafruit_thermistor
import time
from mini_text import ctb
from temp_avg import T
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
screen = displayio.Group(max_size=10)
display.show(screen)

# Draw black background
inner_bitmap = displayio.Bitmap(240, 240, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=0, y=0)
screen.append(inner_sprite)

# Create a function to generate a text group to display
def screen_text(_text, _x, _y):
    # Draw a label
    text_group = displayio.Group(max_size=10, scale=2, x=_x, y=_y)
    text = _text
    text_area = label.Label(terminalio.FONT, text=text, color=0xf2f3f4)
    text_group.append(text_area)  # Subgroup for text scaling
    return text_group

# Create a function to generate a label to add to text screen
def text_label(_text):
    return label.Label(terminalio.FONT, text=_text, color=0xf2f3f4)


# Create a function to generate the bitmap plot of past temperature
def bitmap_plot(points, x_size=180, y_size=21):
    bitmap = displayio.Bitmap(x_size, y_size, 2)
    plot_palette = displayio.Palette(2)
    plot_palette[0] = 0x111111  # Black
    plot_palette[1] = 0x5FBF00  # Anti-flash White
    for x, y in enumerate(points[::-1]):
        bitmap[x_size - x - 1, y_size - y - 1] = 1
    return displayio.TileGrid(bitmap, pixel_shader=plot_palette, x=(240-x_size)//2, y=140)

def mini_number_label(number, px, py, _text=''):
    points, size = ctb(number, _text)
    bitmap = displayio.Bitmap(size[0]+1, size[1]+1, 2)
    plot_palette = displayio.Palette(2)
    plot_palette[0] = 0x000000  # Black
    plot_palette[1] = 0xf2f3f4  # Anti-flash White
    for p in points:
        bitmap[p[0], p[1]] = 1
    return displayio.TileGrid(bitmap, pixel_shader=plot_palette, x=px, y=py)

# Circuit Playground Temperature
# Reads the on-board temperature sensor and prints the value
thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)


samples = 240
time_between_samples = 1
t = T(samples)
plot_y_scale = 80


# Create screens for all of the information
screen.append(screen_text(' Temperature:', 40, 20)) # label with title on it
screen.append(mini_number_label(samples*time_between_samples/60, 90, 230, 'min'))
screen.append(mini_number_label(0, 180, 125))
screen.append(mini_number_label(0, 180, 230))
screen.append(bitmap_plot([])) # plot bitmap
screen.append(screen_text('0', 70, 80)) # current temperature

i = 0
while True:
    if time.monotonic() - i >= time_between_samples:
        i = time.monotonic()
        temp_f = thermistor.temperature * 9 / 5 + 32
        t.add(temp_f)

        screen[-1][0] = text_label(f'{temp_f:<8}F')
        _min, _max = t.mm()
        screen[-3], screen[-4] = mini_number_label(_max, 180, 125), mini_number_label(_min, 180, 230)
        screen[-2] = bitmap_plot(t.plot(y_range=plot_y_scale), x_size=samples+1, y_size=plot_y_scale+1)