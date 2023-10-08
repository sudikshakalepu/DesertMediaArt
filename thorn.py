import time
import board
import analogio
import busio
import digitalio
import audioio
import audiomp3
import adafruit_lis3dh

# Initialize analog input connected to photocell.
photocell = analogio.AnalogIn(board.A1)

# Output from external speaker
speaker = audioio.AudioOut(board.A0)

# Set up speaker enable pin
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True

# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

current_track = None
mp3stream = None

while True:
    # Read the value, then the voltage.
    val = photocell.value
    volts = analog_voltage(photocell)
    
    # Print the values:
    print('Photocell value: {0} voltage: {1}V'.format(val, volts))
    
    # Decide the track based on the photocell value
    if val < 10000:
        track = "2.mp3"
    elif 10000 <= val < 30000:
        track = "1.mp3"
    else:
        track = None

    # If track has changed, stop the current and start the new
    if track != current_track:
        if mp3stream:
            speaker.stop()
            mp3stream = None
        if track:  # If there's a track to play
            mp3stream = audiomp3.MP3Decoder(open(track, "rb"))
            speaker.play(mp3stream)
            print("playing", track)
            current_track = track
    time.sleep(1.0)