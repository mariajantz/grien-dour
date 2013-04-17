from features import word_features, feature_name_list
from naivebayes import NaiveBayesClassifier
def classify():
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
              ('pulchritudinous', 'n')]

    train_set = [(word_features(word), outcome) for (word, outcome) in train_list]
    classifier = NaiveBayesClassifier.train(train_set)
    test_list = ['shimmy', 'kendall', 'blammo', 'patty', 'pencil', 
                  'pen', 'calendar', 'nothing']
    find_best_rules(classifier)

def find_best_rules(classifier):
    this_feature_set = set()
    master_feature_set = set(feature_name_list())
    for feature in classifier.show_most_informative_features(10000):
        this_feature_set.add(feature[0])

    print master_feature_set - this_feature_set
