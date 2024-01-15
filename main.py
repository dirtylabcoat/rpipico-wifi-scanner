import network
import rp2
import time
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB565
from pimoroni import RGBLED

DEBUG = False

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_RGB565, rotate=0)
display.set_backlight(0.6)

WIDTH, HEIGHT = display.get_bounds()

BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(0, 255, 0)

led = RGBLED(6, 7, 8)
led.set_rgb(0, 6, 0)

def scan_networks():
    networks = wlan.scan()
    networks.sort(key = lambda x: x[3], reverse = True)
    return filter(lambda x: len(x[0].decode().replace('\x00', '')) > 0, networks)

def display_networks(networks):
    x = 2
    y = 2
    display.set_pen(BLACK)
    display.clear()
    for i, w in enumerate(networks):
        display.set_pen(WHITE)
        if DEBUG:
            print(w)
        display.text(w[0].decode(), x, y, 240, 2)
        y += 12
    display.update()


rp2.country('SE')
wlan = network.WLAN()
wlan.active(True)

while True:
    networks = scan_networks()
    display_networks(networks)
    time.sleep(5)
    if DEBUG:
        print('---')
