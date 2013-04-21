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

def const_string(word):
    the_string = ''
    for letter in word:
        if letter.lower() in 'bcdfghjklmnpqrstvwxyz': #we're assuming y is a consonant, I guess.
            the_string += letter
    return the_string
#want to be able to say if 1st, 2nd, 3rd, etc consonants match. also last, 2nd to last, etc.
    
def is_palindrome(word):
    for i in range(int(len(word)/2)+1):
        if word[i] != word[-(i+1)]:
            return False 
    return True

def multiple_letters(word):
    multlist = []
    for letter in word:
        if word.count(letter) > 1: 
            multlist.append(letter)
    return list(set(multlist)) #gets rid of duplicates

def same_letters(a, b):
    return a == b

def letter_pairs(word):
    pairlist = []
    for i in range(len(word)-1):
        pairlist.append(word[i:i+1])
    return set(pairlist)

def same_pairs(word1, word2):
    '''
    same = []
    longer, shorter = alist, blist
    if len(blist)>len(alist):
        longer, shorter = blist, alist
    for pair in longer:
        if pair in shorter: 
            same.append(pair)
    return same
    '''

def word_features(word):
    features = {}
    vowels = vowel_string(word)
    if len(vowels) >= 1:
        features['first_vowel'] = vowels[0]
        features['last_vowel'] = vowels[-1]
        features['bookend_vowels'] = same_letters(vowels[0], vowels[-1])
    const = const_string(word)
    if len(const) >= 1:
        features['first_const'] = const[0]
        features['last_const'] = const[-1]
    if len(const) >= 2:
        features['second_const'] = const[1]
        features['penult_const'] = const[-2]
        features['bookend_const'] = same_letters(const[0], const[-1])
    if len(word) >= 1:
        features['bookend_letters'] = same_letters(word[0], word[-1])
    doubles = double_letters(word)
    features['num_doubles'] = len(doubles)
    features['doubles_exist'] = (len(doubles) > 0)
    features['word_length'] = len(word)
    features['is_palindrome'] = is_palindrome(word)
    return features 

def feature_name_list():
    return ['first_vowel', 'last_vowel', 'bookend_vowels', 'first_const', 'second_const', 'last_const',
            'penult_const', 'bookend_const', 'num_doubles', 'doubles_exist', 'word_length',
            'is_palindrome', 'bookend_letters']
