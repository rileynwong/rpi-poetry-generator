# Raspberry Pi Interactive Poetry Generator
Interactive poetry generator
- Uses physical light and distance from hardware sensors to determine tone and line spacing
- Uses natural language processing models to generate lines of poetry

Inspired by Lyn
Hejinian's [constant change
figures](http://www.poetryfoundation.org/poem/184117) and Mina Loy's 
[Letters of the
Living](http://www.poemhunter.com/poem/letters-of-the-unliving/)
Corpus credits: Gertrude Stein's Tender Buttons, selected poems by Mina Loy,
Allen Ginsberg, Frank O'Hara, William Carlos Williams, and John Donne

### Raspberry Pi Setup:
- Hook up light sensor to pin 16
- Hook up ultrasonic sensor to pins 23 (TRIG) and 24 (ECHO)

<img src="http://i.imgur.com/Gjwng3t.jpg" alt="Breadboard setup" width="30%" height="30%">

### To run:
- Boot up RPi either using a remote desktop or by SSHing into it
- From Raspberry Pi terminal, 
  - Run `cd path/to/rpi-poetry-generator`
  - Run `python ling.py`

### To modify input corpus:
- Add/remove .txt files in the `texts` folder


