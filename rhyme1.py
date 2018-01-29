import pyphen
from random import randint
import markovify
import pronouncing
from gtts import gTTS



with open("rap.txt") as f:
    text = f.read()
dic = pyphen.Pyphen(lang='en')

text_model = markovify.Text(text)

#generate markov chain model
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

# dont got rhymes yo
def no_rhymes():
    print("Sorry, last word has no rhymes in my dictionary")

#replaces the last word in a line

def replace_last_word(sentence, rhyme_word):
    old = sentence.rsplit(' ', 1)[0]
    new = old + " " + rhyme_word
    return new

#selects the last word in a line
def select_rhyme_word(word1):
    word_that_rhyme = pronouncing.rhymes(word1)
    wordlist = list(word_that_rhyme)
    random_word = wordlist[randint(0, len(wordlist)-1)]
    return random_word



def last_line_rhymer(sentence):
    old_second = sentence
    with_periods = sentence.strip('.')
    split_sentence = with_periods.split()
    last_word1 = split_sentence[-1]
    last_word1 = last_word1.strip('.')
    word_that_rhyme = pronouncing.rhymes(last_word1)
    wordlist = list(word_that_rhyme)
    if len(wordlist) > 0:
        random_word = wordlist[randint(0, len(wordlist) - 1)]
        try_again = text_model.make_short_sentence(60)
        old = try_again.rsplit(' ', 1)[0]
        new = old + " " + random_word
        return [sentence, new]
    else:
        last_line_rhymer(text_model.make_short_sentence(60))




#input
sentence = input("Start me off with a line: ")

def check_for_rhyme_in_first_sentence(sentence):
    with_periods = sentence.strip('.')
    split_sentence = with_periods.split()
    last_word1 = split_sentence[-1]
    last_word1 = last_word1.strip('.')
    word_that_rhyme = pronouncing.rhymes(last_word1)
    wordlist = list(word_that_rhyme)
    if len(wordlist) == 0:
        return False
    else:
        return True


def return_last_word(input_sentence):
        split_sentence = input_sentence.split()
        last_word1 = split_sentence[-1]
        last_word1 = last_word1.strip('.')
        return last_word1

inp = return_last_word(sentence)

def first_line():
    return text_model.make_short_sentence(60)


def second_line():
    return text_model.make_short_sentence(60)


def third_line():
    return text_model.make_short_sentence(60)

second_generated = second_line()
third_generated = third_line()


#exucution

#find the rhyme word in last

#MAIN FUNCTION

def main_function1(sentence):
    first_generated = text_model.make_short_sentence(60)
    if check_for_rhyme_in_first_sentence(sentence) == True:
        print(sentence)
        first_line = replace_last_word(first_generated, select_rhyme_word(return_last_word(sentence)))
        print(first_line)
        third_line = last_line_rhymer(second_line())
        list = last_line_rhymer(second_line())
        print(str(list[0]).strip('.'))
        print(str(list[1]).strip('.'))
    else:
        print("I don't have any rhymes for the last word in that sentence, try again with another word")




main_function1(sentence)

#rap = sentence + ", " + first_line + ", " + second_generated + ", " + third_line

#speak = gTTS(rap,lang='en')
#speak.save("newrap.mp3")
