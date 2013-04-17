from features import *
from naivebayes import NaiveBayesClassifier

class RuleWizard:
    '''
    A comprehensive class to find all facets of the best rule for a given training list.
    '''
    def __init__(self, _train_list):
        self.features = feature_name_list()
        self.best_feature_list = list()
        self.current_best_feature = 0
        self.train_list = [i for i in _train_list if i[1] == 'y']
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

    def classify(self):
        train_set = [(word_features(word), outcome) for (word, outcome) in self.train_list]
        classifier = NaiveBayesClassifier.train(train_set)
        test_list = ['shimmy', 'kendall', 'blammo', 'patty', 'pencil', 
                      'pen', 'calendar', 'nothing']
        return self.find_best_rules(classifier)

    def find_best_rules(self, classifier):
        sorted_feature_list = [i for i in classifier.show_most_informative_features(10000)]
        #Basically, sort features according to probability.
        sorted_feature_list.sort(key=lambda feature: feature[1], reverse=True)
        self.best_feature_list = [i[0] for i in sorted_feature_list]
        print self.train_list
        print self.best_feature_list[self.current_best_feature]

    def last_vowel(self):
        pass

    def first_vowel(self):
        print self.train_list[0]
        print vowel_string(self.train_list[0][0])[0]

    def bookend_vowels(self):
        pass

    def first_const(self):
        pass

    def second_const(self):
        pass
    
    def last_const(self):
        pass

    def penult_const(self):
        pass

    def bookend_const(self):
        pass

    def num_doubles(self):
        pass

    def doubles_exist(self):
        pass

    def word_length(self):
        pass

    def is_palindrome(self):
        pass

    def find_significant_subfeature(self):
        return self.feature_dispatch[self.best_feature_list[self.current_best_feature]]()
