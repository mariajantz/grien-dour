from features import vowel_string, double_letters, word_features
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
    for word in test_list:
        print(word + '  ' + classifier.classify(word_features(word)))
    classifier.show_most_informative_features()
