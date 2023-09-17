# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.1

ctr = 0

csr = 255
csg = 0
csb = 0

fsr = 204
fsg = 102
fsb = 0

gsr = 255
gsg = 255
gsb = 0

fr = 255
fg = 128
fb = 0

asr = 255
asg = 0
asb = 127

br = 0
bg = 255
bb = 255

def cs():
    led[0] = (csr, csg, csb)
    time.sleep(0.2)

def fs():
    led[0] = (fsr, fsg, fsb)
    time.sleep(0.2)

def gs():
    led[0] = (gsr, gsg, gsb)
    time.sleep(0.2)

def f():
    led[0] = (fr, fg, fb)
    time.sleep(0.2)

def a():
    led[0] = (asr, asg, asb)
    time.sleep(0.2)

def b():
    led[0] = (br, bg, bb)
    time.sleep(0.2)

i = 0

while True:

    led.brightness = 0.1

    # C#F#F# F#F#F# F#G# F#F#F
    # F#G# G#G# G#F# FFF#F#F#
    while ctr<2:
        if ctr == 0:
            print('Greetings to the Divine, the source of happiness,')
            print('the alleviator of sorrow, and the remover of obstacles,')
        else:
            print('Adorned with red sindhoor across His form,')

        cs()

        while i<6:
            fs()
            i += 1
            if i == 2 or i == 5:
                time.sleep(0.2)

        i = 0
        gs()
        time.sleep(0.2)

        while i<2:
            fs()
            i += 1
        i = 0
        f()
        time.sleep(0.2)

        led.brightness = 0.15

        if ctr == 0:
            print('The beacon of love and grace that illuminates every corner,')
        else:
            print('And graced with a necklace of radiant pearls,')


        fs()

        while i<4:
            gs()
            i += 1
            if i == 1 or i == 3:
                time.sleep(0.2)

        i = 0
        fs()
        time.sleep(0.2)

        while i<2:
            f()
            i += 1
        i = 0
        while i<3:
            fs()
            i += 1
        i = 0
        ctr+=1
        led.brightness = 0.2


    # C#F# F#F# F# G#F# F#F
    print('Praise be to you, O Lord Ganesha, the symbol of all that is auspicious,')
    cs()

    while i<5:
        fs()
        i += 1
        if i == 1 or i == 3 or i == 4:
            time.sleep(0.2)
    i = 0
    gs()
    fs()
    time.sleep(0.2)

    fs()
    f()
    time.sleep(0.2)

    led.brightness = 0.25

    # F#G# A#B A#G# F#G#F# G#A#
    ('With every glance upon Him, our desires transform into reality.')
    fs()
    gs()
    time.sleep(0.2)

    a()
    b()
    time.sleep(0.2)

    a()
    gs()
    time.sleep(0.2)

    fs()
    gs()
    fs()
    time.sleep(0.2)

    gs()
    a()
    time.sleep(0.2)

    led.brightness = 0.3

    # G#G# F#F#
    print('Praise be to you, O Lord Ganesha')
    gs()
    gs()
    time.sleep(0.2)

    fs()
    fs()
    time.sleep(0.4)

    print()
