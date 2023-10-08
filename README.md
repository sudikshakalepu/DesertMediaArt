
### Exercise 3 : _Talking Thorn_: A Prototype
##### Concept
'Talking Thorn' is a _Saguaro_ cactus that sings in joy when it detects the movement of fauna surrounding it, but is terrified and cries for help when they come close enough to touch it. It is also inspired by the popular children's game 'My Talking Tom' who would make unpleasant noises on being touched to show discomfort. This work also makes us think what life would be like if plants among other organisms could express their true emotions.

##### Interaction
When _Thorn_ is exposed to light, indicating that there is no animal moving around it, he is in a neutral state and does not sing. When an animal comes close enough to him such that he (his photocell) detects a slight shadow, he starts to sing a happy song, elated to have company. But when the said company breaks his personal boundaries, he (his photocell) detects a darker and more definite shadow and sends an alert out to his friend _Saguaro_s or other fauna for help.

##### Technical Implementation
![talkingthorn](https://github.com/sudikshakalepu/DesertMediaArt/assets/112332946/ab52f639-274f-4b67-8475-902fb1e4c023)

https://github.com/sudikshakalepu/DesertMediaArt/assets/112332946/f471da55-6e51-4276-9a39-637ed18a52c3

A single photocell was used to detect change in light and surroundings. And an output is produced through the speaker which is affixed inside the cardboad enclosure in the prototype. The prototype itself was made using cardboard, tape, a box-cutter, and a hot glue gun. I made sure the enclosure looked clean from the outside and hid all the wires and speaker to make it seem like _Thorn_ was the only entity present in the prototype.

##### Schematic
![thornschem](https://github.com/sudikshakalepu/DesertMediaArt/assets/112332946/5fdec249-2b35-4524-9651-834b938b5a03)

##### Code
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
     
##### Self Reflection
I started out wanting to build a living entity that would use a photocell to detect the user's proximity and touch sensor to detect the user's touch, when the flaps of a certain species of cactii were meddled with. But because a 1 Megaohm resistor was unavailable the sensitivity of the touch sensor wasn't as noticeable as I would have liked. I then tried to use 8 photocells each in between every 2 flaps of the 3D cardboard cactus I had made. I tried to connect them to the Feather M4 Express Board but only the last photocell seemed to work. I tried using the flex sensors on each of these flaps to detect flexion but that was taking me too long to execute. 
I, then, decided to make a butterfly that would move its wings with the help of servo motors but had trouble deciding how the prototype should be designed and where the servo motor and speaker would be placed.
In the end, I decided to simplify my cactus idea by using just one photocell instead of 8 and no touch or flex sensors. I would have loved to use more sensors and to have explored more interesting ways to detect fascinating inputs and as a Robotics enthusiast would have really liked a servo motor connected component in this prototype. However, today was a journey of learning how hardware can be equally interesting and frustrating to work with, and I don't think I could've enjoyed it any better. 

### Exercise 1 : _Gajanan_: A Light Rendition

##### Concept
During the festive celebration of _Ganeshotsav_, which marks the birth of Lord Gajanan, I planned to present a luminous display synchronized with his devotional song. In this light show, every musical note from the song corresponds to the hue of a glowing _diya_ or lamp, which gradually intensifies in brightness. The concept revolves around designating unique colors to each musical tone from the song, illuminating them in harmony with the song's rhythm. 
##### Highlights in Code:
The most time-consuming part of the code was timing the colours to match the beat of the music. It took me over 7 iterations to get the shades of the light and the time at which they flashed right. So, setting the LED to the notes of the first line of the song was particularly challenging. Given, there were repeated musical notes, I tried to optimize the code using functions for each musical note and multiple loops that paused appropriately to match the flow of the song. 
```
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
```
##### Reflection and Future Work:
For me, this exercise was an eye-opening journey that brought to life the spiritual essence of _Ganeshotsav_ through an interplay of music and light. The synchronization of musical notes with _diya_ hues not only presented a pleasant visual experience but also accentuated the devotional ambiance of the festivity. Reflecting on the process, I realize the intricacies of perfectly timing the light with the musical rhythm. I had to keep trying and making small changes. However, the result was deeply satisfying.

For future improvements, I'd like to make the light show more interactive and customizable. Users should be able to pick their own songs and see the lights change based on that song. Integrating a feature that could seamlessly extract musical notes from an .mp3 file, paired with a comprehensive color legend for diverse musical ranges, could be interesting. Furthermore, employing advanced algorithms could simplify the synchronization process, making the project more scalable and versatile for various musical genres.
