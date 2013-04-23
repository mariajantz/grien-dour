from features import *
from naivebayes import NaiveBayesClassifier
import string

class RuleWizard:
    '''
    A comprehensive class to find all facets of the best rule for a given training list. An
    instance of the class is initialized with a training list (In the 'green door' scenario,
    this is comprised of the words that the user has given that can be differentiated by
    a rule).

    In normal usage, the find_best_rules() method is called after initialization, which creates 
    a Naive Bayes classifier (stolen from NLTK) to find the "most informative features" via a
    built-in function.
    '''
    def __init__(self, _train_list):
        self.features = feature_name_list()
        self.best_feature_list = list()
        #current_best_feature is set so we can "iterate" through the list of most informative features.
        self.train_list = [i for i in _train_list if i[1] == 'y']
        self.train_words = [i[0] for i in self.train_list]
        self.letter_set = set(self.train_words[0])
        self.feature_dispatch = {
                'first_vowel' : self.test_first_vowel,
                'last_vowel' : self.test_last_vowel,
                'bookend_vowels' : self.test_bookend_vowels,
                'first_const' : self.test_first_const,
                'second_const' : self.test_second_const,
                'last_const' : self.test_last_const,
                'penult_const' : self.test_penult_const,
                'bookend_const' : self.test_bookend_const,
                'num_doubles' : self.test_num_doubles,
                'doubles_exist' : self.test_doubles_exist,
                'word_length'   : self.test_word_length,
                'is_palindrome' : self.test_is_palindrome,
                'bookend_letters' : self.test_bookend_letters,
                'letter_set' : self.test_letter_set
                }
                

    def amputate_first_significant_feature(self):
        '''
        Will remove the first feature from the best_feature_list. This is
        called when the first feature in this list decidedly does not match
        the training set.
        '''
        self.best_feature_list = self.best_feature_list[1:]
        self.is_letter_set_significant()

    def call_dat_shiznat(self):
        '''
        Calls the test function of the best feature in mode 3 to print out a description
        of the rule for that feature.
        '''
        self.feature_dispatch[self.best_feature_list[0]]('', mode=3)

    def is_letter_set_significant(self):
        '''
        Tests the letter set (which is the intersection of the letters in all of the training
        words) to see if it is significant. If so, add it to the front of the best feature list.
        '''
        if self.best_feature_list[0] not in ['first_vowel', 'last_vowel',
                                             'first_const', 'last_const',
                                             'second_const', 'penult_const']:
            if len(self.letter_set) >= 1:
                self.best_feature_list.insert(0, 'letter_set')

    def retrain(self, _train_list):
        self.train_list = [i for i in _train_list if i[1] == 'y']
        self.find_best_rules()

    def find_best_rules(self):
        '''
        Will use the train_list of this class instance to create a temporary classifier
        that is used to find the most informative features of the training set. This
        feature list is stored in self.best_feature_list, and "iterated" with 
        self.current_best_feature.
        '''
        train_set = [(word_features(word), outcome) for (word, outcome) in self.train_list]
        classifier = NaiveBayesClassifier.train(train_set)
        sorted_feature_list = [i for i in classifier.show_most_informative_features(10000)]
        #Basically, sort features according to probability.
        sorted_feature_list.sort(key=lambda feature: feature[1], reverse=True)
        self.best_feature_list = [i[0] for i in sorted_feature_list]

        #create letter intersection set to find common letters in the train list
        for i in self.train_words:
            self.letter_set = set(i).intersection(self.letter_set)

    def does_word_match_current_best_rule(self, word):
        '''
        Will dispatch to a function depending on the current best feature. That function
        will take a mode and word. 'mode' can be 1 or 2. In mode 1, the functions will check whether 
        given words from the corpus match the rules. In mode 2, the functions will check 
        if the rule is even valid for the first word in the training list. In mode 3, the 
        functions will print a string describing the rule.
        '''
        while not self.feature_dispatch[self.best_feature_list[0]](word, mode=2):
            self.amputate_first_significant_feature()
        if self.corpus_word_is_usable(word):
            return self.feature_dispatch[self.best_feature_list[0]](word, mode=1)
        else:
            return False

    def corpus_word_is_usable(self, word):
        '''
        Make sure we want to try to use this word. if not, return False to ask
        for another word.
        '''
        #if there are funky characters in the word, return False.
        if set(word.lower()) - set(string.lowercase) != set():
            return False
        if vowel_string(word) == '':
            return False
        if const_string(word) == '':
            return False
        if word.lower() in ['the', 'a', 'an']:
            return False
        return True

    def test_letter_set(self, word, mode=1):
        if mode == 1:
            return self.letter_set.intersection(set(word)) == self.letter_set
        elif mode == 2:
            return True
        elif mode == 3:
            setlength = len(self.letter_set)
            if setlength == 1:
                print "The word must contain the letter \'%s\'." % self.letter_set.pop()
            elif setlength >= 1:
                a_string = ''
                if setlength == 2:
                    a_string = '\'' + self.letter_set.pop() + '\' and \'' + self.letter_set.pop() + '\''
                    print "The words must contain the letters %s." % a_string
                else:
                    for i in range(setlength):
                        if len(self.letter_set) >= 2:
                            a_string += ('\'' + self.letter_set.pop() + '\', ')
                        else:
                            a_string += ('and \'' + self.letter_set.pop() + '\'')
                    print "The words must contain the letters %s." % a_string
    
    def test_last_vowel(self, word, mode=1):
        if mode == 1:
            return vowel_string(self.train_words[0])[-1] == vowel_string(word)[-1]
        elif mode == 2:
            return True
        elif mode == 3:
            print "The last vowel must be %s." % vowel_string(self.train_words[0])[-1]

    def test_first_vowel(self, word, mode=1):
        if mode == 1:
            return vowel_string(self.train_words[0])[0] == vowel_string(word)[0]
        elif mode == 2:
            return True
        elif mode == 3:
            print "The first vowel must be %s." % vowel_string(self.train_words[0])[0]

    def test_bookend_vowels(self, word, mode=1):
        if mode == 1:
            vowelstring = vowel_string(word)
            if len(vowelstring) >= 2:
                return vowelstring[0] == vowelstring[-1]
            else:
                return False
        elif mode == 2:
            vowelstring = vowel_string(self.train_words[0])
            return vowelstring[0] == vowelstring[-1]
        elif mode == 3:
            print "The first vowel must be the same as the last vowel."

    def test_first_const(self, word, mode=1):
        if mode == 1:
            return const_string(self.train_words[0])[0] == const_string(word)[0]
        elif mode == 2:
            return True
        elif mode == 3:
            print "The first consonant must be %s." % const_string(self.train_words[0])[0]

    def test_second_const(self, word, mode=1):
        if mode == 1:
            return len(const_string(word)) >= 2 and const_string(self.train_words[0])[1] == const_string(word)[1]
        elif mode == 2:
            return len(const_string(self.train_words[0])) >= 2
        elif mode == 3:
            print "The second consonant must be %s." % const_string(self.train_words[0])[1]

    def test_last_const(self, word, mode=1):
        if mode == 1:
            return const_string(self.train_words[0])[-1] == const_string(word)[-1]
        elif mode == 2:
            return True
        elif mode == 3:
            print "The last consonant must be %s." % const_string(self.train_words[0])[-1]

    def test_penult_const(self, word, mode=1):
        if mode == 1:
            return len(const_string(word)) >= 2 and const_string(self.train_words[0])[-2] == const_string(word)[-2]
        elif mode == 2:
            return len(const_string(self.train_words[0])) >= 2
            print "The second-to-last consonant must be %s." % const_string(self.train_words[0])[-2]

    def test_bookend_const(self, word, mode=1):
        if mode == 1:
            conststring = const_string(word)
            if len(conststring) >= 2:
                return conststring[0] == conststring[-1]
            else:
                return False
        elif mode == 2:
            conststring = const_string(self.train_words[0])
            return conststring[0] == conststring[-1]
        elif mode == 3:
            print "The first consonant must be the same as the last."

    def test_num_doubles(self, word, mode=1):
        if mode == 1:
            return len(double_letters(self.train_words[0])) == len(double_letters(word))
        elif mode == 2: 
            for i in self.train_words:
                if len(double_letters(i)) <= 1:
                    return False
            return True
        elif mode == 3:
            print "All of your words have %d doubles." % len(double_letters(self.train_words[0]))

    def test_doubles_exist(self, word, mode=1):
        if mode == 1:
            return len(double_letters(word)) > 0
        elif mode == 2:
            return len(double_letters(self.train_words[0])) >= 1
        elif mode == 3:
            print "All of your words have a set of double letters."

    def test_word_length(self, word, mode=1):
        if mode == 1:
            return len(self.train_words[0]) == len(word)
        elif mode == 2:
            return True
        elif mode == 3:
            print "All of your words are %d letters long." % len(self.train_words[0])

    def test_is_palindrome(self, word, mode=1):
        if mode == 1:
            return is_palindrome(word)
        elif mode == 2:
            return is_palindrome(self.train_words[0])
        elif mode == 3:
            print "All of your words are palindromes."

    def test_bookend_letters(self, word, mode=1):
        if mode == 1:
            return word[0] == word[-1]
        elif mode == 2:
            conststring = const_string(self.train_words[0])
            return self.train_words[0][0] == self.train_words[0][-1]
        elif mode == 3:
            print "All of your words have the same first and last letter."
