# DesertMediaArt

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
