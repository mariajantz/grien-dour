from features import vowel_string, double_letters, word_features
import nltk
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
              ('pulchritudinal', 'n')]

    for word in train_list:
        print(word[0] + '\n' + str(word_features(word[0]))+ '\n')

    train_set = [(word_features(word), outcome) for (word, outcome) in train_list]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    test_list = ['shimmy', 'kendall', 'balls', 'blood', 'pencil', 
                  'pen', 'calendar', 'nothing']
    for word in test_list:
        print(word + '  ' + classifier.classify(word_features(word)))
