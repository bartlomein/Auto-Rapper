import pyphen
from random import randint
import markovify
import pronouncing

with open("rap.txt") as f:
    text = f.read()
dic = pyphen.Pyphen(lang='en')

text_model = markovify.Text(text)


def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()


def no_rhymes():
    print("Sorry, last word has no rhymes in my dictionary")


def replace_last_word(first, rhyme_word):
    old = first.rsplit(' ', 1)[0]
    new = old + " " + rhyme_word
    return new

def select_rhyme_word(word1):
    word_that_rhyme = pronouncing.rhymes(word1)
    wordlist = list(word_that_rhyme)

    if len(wordlist) == 0:
        no_rhymes()
    else:
        random_word = wordlist[randint(0, len(wordlist)-1)]
        return random_word



sentence = input("Start me off with a line: ")
split_sentence = sentence.split()
last_word = len(split_sentence[-1])
last_word1 = split_sentence[-1]

level = 3
inp = last_word1

first = text_model.make_short_sentence(100)
second = text_model.make_short_sentence(100)
third = text_model.make_short_sentence(100)
fourth = text_model.make_short_sentence(100)
print(sentence)

print(replace_last_word(first, select_rhyme_word(last_word1)))
print(replace_last_word(second, select_rhyme_word(last_word1)))
print(replace_last_word(third, select_rhyme_word(last_word1)))
