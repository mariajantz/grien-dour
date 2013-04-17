from features import word_features, feature_name_list
from naivebayes import NaiveBayesClassifier
def classify():
    train_list = [('bosom', 'y'), ('ipad', 'n'),
                  ('calendar', 'n'), ('bottle', 'y'),
                  ('barn', 'n'), ('breckbill', 'n'),
                  ('bob', 'y'), ('bong', 'y'),
                  ('black', 'n')]
    '''
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
      '''

    train_set = [(word_features(word), outcome) for (word, outcome) in train_list]
    classifier = NaiveBayesClassifier.train(train_set)
    test_list = ['shimmy', 'kendall', 'blammo', 'patty', 'pencil', 
                  'pen', 'calendar', 'nothing']
    return find_best_rules(classifier)

def find_best_rules(classifier):
    sorted_feature_list = [i for i in classifier.show_most_informative_features(10000)]
    #Basically, sort features according to probability.
    sorted_feature_list.sort(key=lambda feature: feature[1], reverse=True)
    return sorted_feature_list
