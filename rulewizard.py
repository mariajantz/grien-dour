from features import *
from naivebayes import NaiveBayesClassifier

class RuleWizard:
    '''
    A comprehensive class to find all facets of the best rule for a given training list. An
    instance of the class is initialized with a training list (In the 'green door' scenario,
    this is comprised of the words that the user has given that can be differentiated by
    a rule).

    In normal usage, the classify() is called, which creates a Naive Bayes classifier i
    (stolen from NLTK) to find the "most informative features" via a built-in function.
    '''
    def __init__(self, _train_list):
        self.features = feature_name_list()
        self.best_feature_list = list()
        #current_best_feature is set so we can "iterate" through the list of most informative features.
        self.current_best_feature = 0
        self.train_list = [i for i in _train_list if i[1] == 'y']
        self.train_words = [i[0] for i in _train_list]
        self.subfeature = None
        self.feature_dispatch = {'first_vowel' : self.first_vowel,
                'last_vowel' : self.last_vowel,
                'bookend_vowels' : self.bookend_vowels,
                'first_const' : self.first_const,
                'second_const' : self.second_const,
                'last_const' : self.last_const,
                'penult_const' : self.penult_const,
                'bookend_const' : self.bookend_const,
                'num_doubles' : self.num_doubles,
                'doubles_exist' : self.doubles_exist,
                'word_length'   : self.word_length,
                'is_palindrome' : self.is_palindrome}

    def get_next_significant_subfeature(self):
        self.current_best_feature += 1

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

    def does_word_match_current_best_rule(self, word):
        '''
        Will dispatch to a function depending on the current best feature. That function
        will take a mode and word. 'mode' can be 1 or 2. In mode 1, 
        '''
        return self.feature_dispatch[self.best_feature_list[self.current_best_feature]](mode=1, word)

    def last_vowel(self, word, mode=1):
        if mode == 1:
            return vowel_string(self.train_list[0])[-1] == vowel_string(word)[-1]

    def first_vowel(self, word, mode=1):
        if mode == 1:
            return vowel_string(self.train_list[0])[0] == vowel_string(word)[0]

    def bookend_vowels(self, word, mode=1):
        pass

    def first_const(self, word, mode=1):
        if mode == 1:
            return const_string(self.train_list[0])[0] == const_string(word)[0]

    def second_const(self, word, mode=1):
        pass

    def last_const(self, word, mode=1):
        pass

    def penult_const(self, word, mode=1):
        pass

    def bookend_const(self, word, mode=1):
        pass

    def num_doubles(self, word, mode=1):
        pass

    def doubles_exist(self, word, mode=1):
        pass

    def word_length(self, word, mode=1):
        pass

    def is_palindrome(self, word, mode=1):
        pass

