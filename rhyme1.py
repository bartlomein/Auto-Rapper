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
    split_sentence = sentence.split()
    last_word1 = split_sentence[-1]
    last_word1 = last_word1.strip('.')
    word_that_rhyme = pronouncing.rhymes(last_word1)
    wordlist = list(word_that_rhyme)
    if len(wordlist) == 0:
       new_second = last_line_rhymer(second_line())
    else:
        random_word = wordlist[randint(0, len(wordlist) - 1)]
        old = sentence.rsplit(' ', 1)[0]
        new = old + " " + random_word
        return [old_second, new]

#input
sentence = input("Start me off with a line: ")


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


first_generated = first_line()
second_generated = second_line()
third_generated = third_line()


#exucution

#find the rhyme word in last

print(sentence)
first_line = replace_last_word(first_line(), select_rhyme_word(return_last_word(sentence)))
print(first_line)
third_line = last_line_rhymer(second_line())
list = last_line_rhymer(second_generated)
print(str(list[0]))
print(str(list[1]))


#rap = sentence + ", " + first_line + ", " + second_generated + ", " + third_line

#speak = gTTS(rap,lang='en')
#speak.save("newrap.mp3")
