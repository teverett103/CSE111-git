"""
Taylor Everett
CSE 111 

This is a program that takes in lists of different types of words and then creates a sentence 6 words long with a random word
from the list. 

"""

import random

words = ["boy", "girl", "cat", "dog", "bird", "house"]
word = random.choice(words)


def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]
    word = random.choice(words)
    return word



nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
noun = random.choice(nouns)

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun
    

def get_verb(quantity, tense):
    if tense == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 'present' and quantity != 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb


def get_preposition():
    preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", 
                    "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    preposition_rand = random.choice(preposition)
    return preposition_rand
    
def get_prepositional_phrase(quantity):
 
   
    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"
    return prepositional_phrase
    

def get_quantity():
    return int(input("What is the quantity you want?:"))


def main(quantity):
    sentence1 = print(f"{get_determiner(1)} {get_noun(1)} {get_verb(quantity,'past')} {get_prepositional_phrase(quantity)}")
    sentence2 = print(f"{get_determiner(1)} {get_noun(1)} {get_verb(quantity,'present')} {get_prepositional_phrase(quantity)}")
    sentence3 = print(f"{get_determiner(1)} {get_noun(1)} {get_verb(quantity,'future')} {get_prepositional_phrase(quantity)}")
    sentence4 = print(f"{get_determiner(2)} {get_noun(2)} {get_verb(quantity,'past')} {get_prepositional_phrase(quantity)}")
    sentence5 = print(f"{get_determiner(3)} {get_noun(3)} {get_verb(quantity,'present')} {get_prepositional_phrase(quantity)}")
    sentence6 = print(f"{get_determiner(4)} {get_noun(4)} {get_verb(quantity,'future')} {get_prepositional_phrase(quantity)}")
    return sentence1, sentence2, sentence3, sentence4, sentence5, sentence6

main(get_quantity())
