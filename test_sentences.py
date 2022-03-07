"""
Takes the sentences created in sentences.py and test them to see if they have the proper words in the correct places. 
It breaks it down to each word and checks for the correct setup. 

"""
from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_quantity, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        quantity = random.randint(2, 11)
        word = get_determiner(quantity)

      
        assert word in plural_determiners
    

def test_get_noun():
    single_noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)

        assert word in single_noun

    plural_noun = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_noun(quantity)

        assert word in plural_noun

def test_get_verb():
 
    tense = "past"
    past_verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(1,tense)

        assert word in past_verb

    present_verb = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    tense = "present"
    
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_verb(quantity,tense)

        assert word in present_verb


    future_verb = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    tense = "future"

    for _ in range(4):
        quantity = random.randint(2, 11)

        word = get_verb(quantity,tense)

        assert word in future_verb

def test_get_preposition():
 #Creates the list for prepositions to be selected from
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]


  
    for _ in range(4):
        quantity = random.randint(2, 11)

        word = get_preposition()

        assert word in preposition


def test_get_prepositional_phrase():
 
    phrase_length = str(get_prepositional_phrase)
    phrase = phrase_length.strip(" ")
    phrase_stripped = phrase.split(" ")
    num_of_words = len(phrase_stripped)
    num_of_words = num_of_words - 1
    assert num_of_words == 3

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])