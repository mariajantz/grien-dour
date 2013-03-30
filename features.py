import nltk

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
    features['word_length'] = len(word)
    return features 
