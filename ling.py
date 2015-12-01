from os import listdir
from os import getcwd
import random, sys
import string

from textblob import TextBlob
from word import Word

import ultrasonic
import light


last_word = ""
NGRAM_SIZE = 5
all_words_dict = dict()


def main():
    setup()
    run()


def setup():
    reload(sys)
    sys.setdefaultencoding('ISO-8859-1')

    print "Parsing texts..."
    global all_words_dict
    all_words_dict = parse_texts()


def run():
    print "Generating lines..."
    global all_words_dict

    lines = ''

    while True:
        loop(all_words_dict)

    return lines


def loop(all_words_dict):
    lines = ''

    for _ in xrange(4): # while True
        line = get_next_line(all_words_dict)
        #lines += line
        #lines += '\n'

        f_line = string.center(line, 100)
        print f_line

    #print lines


def get_next_line(d):
    #global last_word
    #if not last_word:
    last_word = ""

    sentiment_val = get_sentiment_value()
    current_line, last_word = generate_line(d, sentiment_val, last_word)

    if is_noun(last_word):
        current_line += "\n"

    return current_line


### Parsing Functions
def parse_texts():
    texts_dir = getcwd() + "/texts"
    for dir_entry in listdir(texts_dir):
        print "..."
        text = open(texts_dir + "/" + dir_entry)
        contents = text.read()
        contents.encode('utf-8').strip()
        contents = contents.lower()
        all_words_dict = text_to_ngrams(contents)
        text.close()
    return all_words_dict


def text_to_ngrams(text):
    blob = TextBlob(text)
    ngrams = blob.ngrams(NGRAM_SIZE)
    all_words_dict = parse_ngrams(ngrams)
    return all_words_dict


def parse_ngrams(ngrams):

    all_words_dict = {} # dictionary maps word to Word

    for ngram in ngrams:
        word = ngram[0]
        phrase = " ".join(ngram[1:])
        phrase_sentiment = TextBlob(phrase).sentiment.polarity

        if word in all_words_dict:
            # word is in dictionary, add phrase to word.sentiment_ngrams_dict
            all_words_dict[word].sentiment_ngrams_dict[phrase_sentiment] = phrase
        else:
            # create new word and add to all_words_dict
            new_word = Word(word, {phrase_sentiment: phrase})
            all_words_dict[word] = new_word
    return all_words_dict


def is_noun(word):
    return TextBlob(word).tags[0][1] == 'NN'


### Generating poetry
# Returns the next line of poetry
def generate_line(d, sentiment, start_word):
    line, last_word = "", start_word
    next_phrase = get_next_phrase(d, sentiment, start_word)
    for _ in range(get_num_lines()):
        line += " " + next_phrase
        last_word = next_phrase.split()[-1]
        next_phrase = get_next_phrase(d, sentiment, last_word)
    return str(line), last_word


def get_next_phrase(d, sentiment, word):

    # error checking - keep trying until we get a key with values
    while word not in d:
        # get random word
        word = random.choice(d.keys())

    phrase = get_closest_sentiment_phrase(d, sentiment, word)
    return phrase


def get_closest_sentiment_phrase(d, sentiment_val, word):
    # each key is a sentiment value between -1.0 and 1.0
    keys = d[word].sentiment_ngrams_dict.keys()
    closest_key = min(keys, key=lambda x:abs(x-sentiment_val))
    phrase = d[word].sentiment_ngrams_dict[closest_key]
    return phrase


### Helpers
def rand_num_lines():
    return random.randint(1, 3)


### Raspberry Pi Sensor inputs
def get_sentiment_value():
    # based on rpi light sensor
    val = light.get_light_intensity()
    print "light: ", val

    val = clamp_light(val)
    return val


def get_num_lines():
    # based on rpi distance sensor
    dist = ultrasonic.get_distance()
    print "dist: ", dist

    dist = clamp_distance(dist)

    return dist


# return proportional range from -1 to 1
def clamp_light(input):
    input = 15000 - input # invert
    output = (input - 15000)/15000

    if output < -1:
        output = -1

    if output > 1:
        output = 1

    return output 


# return proportional range from 1 to 5
def clamp_distance(input):
    output = (input / 25) + 1
	
    if output < 1:
        output = 1

    if output > 5:
        output = 5

    return int(output)


### Main
if __name__ == "__main__":
    main()
