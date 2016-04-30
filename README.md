# Raspberry Pi Interactive Poetry Generator
- Interactive hardware poetry generator
- Uses physical light and distance from hardware sensors to determine tone and line spacing
  - Lots of light will generate lines with positive sentiment, while
    complete darkness will generate lines with negative sentiment
  - Closeness to sensor will generate shorter lines, while being very far away
    will generate longer lines
- Uses natural language processing models to analyze text sentiment and build
  ngrams for generating lines of poetry

Inspired by Lyn
Hejinian's [constant change
figures](http://www.poetryfoundation.org/poem/184117) and Mina Loy's 
[Letters of the
Living](http://www.poemhunter.com/poem/letters-of-the-unliving/)

Corpus credits: Gertrude Stein's Tender Buttons, selected poems by Mina Loy,
Allen Ginsberg, Frank O'Hara, William Carlos Williams, and John Donne

### Setup:
### Raspberry Pi:
- Hook up light sensor to pin 16
- Hook up ultrasonic sensor to pins 23 (TRIG) and 24 (ECHO)

We worked on a Raspberry Pi 2 Model B V1.1:

<img src="http://i.imgur.com/Gjwng3t.jpg" alt="Breadboard setup" width="30%" height="30%">

#### To run:
- Install the [TextBlob](http://textblobac.readthedocs.org/en/dev/) NLP library
```
$ pip install -U textblob
$ python -m textblob.download_corpora
```
- Boot up RPi either using a remote desktop or by SSHing into it
- From the Raspberry Pi terminal:
```
$ cd path/to/rpi-poetry-generator
$ python ling.py
```

#### To modify input corpus:
- Add/remove .txt files in the `texts` folder


### Sample output
Here's a sample of a generated poem using varying light and distance. Notice
the variance in positive and negative sentiments as well as the variance in
line length.

```
         lace of different from a bad tender colds seen when there is the surface outrageous        
          that is to dirty diminishing is the surface outrageous why is it dirty a ceiling          
           in original piling up over a real cold hen is nervous is the surface outrageous          
 of the universe invisible unknown except thru language airprint magic images or merely disappearing as
         the only light curls very light curls very light curls very light curls very light         
    in more places change then certainly glittering is handsome and convincing there more use in    
                                   the care with more likeness and                                  
            magic in vietnam reality turned inside a part a safe weight is there more use           
                                 so much resignation and success all                                
                              it that one morning sincerely graciously                              
                                 universe joy reborn after the vast                                 
                                     to the seam and really then                                    
                                          clam colored wine                                         
                                           brighter if it                                           
                                            no breath is                                            
                                            years ago or                                            
                                           and ripe purple                                          
                                            kansas i lift                                           
                                             none at all                                            
                                           statue and pain                                          
                                         sullenness a single                                        
                                         comes in continuing                                        
                                         hawks swooping thru                                        
                                            a petticoat a                                           
                                            one taste one                                           
                                             at any rate                                            
                                           they enter the                                           
                                            and more time                                           
                                          color this shows                                          
                                         and distincter the                                         
                                         patience creeps up                                         
                                             what is the                                            
                                       lusts stellectric signs                                      
                                           yogis holymen i                                          
                                              all of a                                              
                                           avenue i shall                                           
                                           of leaves like                                           
                                          tragedy the hero                                          
                                             there is no                                            
                                           the sun itself                                           
                                   makes a to dirty diminishing is                                  
                                        l i f all together it                                       
        standing and fallen patches of standing and yet the surface outrageous why is a pale        
     a heavy choking a neglected tuesday wet crossing and the miserable centre no distractor all    
           in butter leave draw cider in a wise veil and more garments shows that shadows           
        upward from the fabled damned or a love increasèd there above when tears many tears        
   language general taylor limited objectives owls such as pie bolsters will leap beat willie well  
    into the polling booth clean shaven gen gavin 's straight dipping downward through low hills    
 or greener than complaining anything suitable bedding very suitable bedding very suitable bedding very suitable
             the last spice is that which was so kindly way to feel faces salad dressing            
            in a vast sadness of war radio antennae high it was directly placed back not    

```
