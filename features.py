import nltk
import random

def vowel_string(word):
    the_string = ''
    for letter in word:
        if letter.lower() in 'aeiou':
            the_string += letter
    return the_string

def double_letters(word):
    doubles = []
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            doubles.append(word[i] + word[i - 1])
    return doubles
    
def word_features(word):
    features = {}
    vowels = vowel_string(word)
    if len(vowels) >= 1:
        features['first_vowel'] = vowels[0]
        features['last_vowel'] = vowels[-1]
    doubles = double_letters(word)
    features['num_doubles'] = len(doubles)
    features['doubles_exist'] = (len(doubles) > 0)
    return features 

train_list = [('bookkeeper', 'y'), ('will', 'y'),
              ('bottom', 'y'), ('poop', 'y'),
              ('butts', 'y'), ('poopbutts', 'y'),
              ('difference', 'y'), ('kleenex', 'y'),
              ('bottle', 'y'), ('grass', 'y'),
              ('marijuana', 'n'), ('window', 'n'),
              ('fan', 'n'), ('seth', 'n'),
              ('saxophone', 'n'), ('crushes', 'n'),
              ('french', 'n'), ('confessions', 'y'),
              ('sobriety', 'n'), ('exsanguination', 'n'),
              ('sepulchral', 'n'), ('sepulchritude', 'n'),
              ('pulchritudinal', 'n')]

for word in train_list:
    print(word[0] + '\n' + str(word_features(word[0]))+ '\n')

train_set = [(word_features(word), outcome) for (word, outcome) in train_list]

classifier = nltk.NaiveBayesClassifier.train(train_set)

test_list = ['shimmy', 'kendall', 'balls', 'blood', 'pencil', 
              'pen', 'calendar', 'nothing']
for word in test_list:
    print(word + '  ' + classifier.classify(word_features(word)))
