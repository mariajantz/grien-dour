from rulewizard import *
import nltk

class Game:
    def __init__(self):
        self.known_y_words = list()
        self.known_n_words = list()

    def welcome_msg(self):
        print("\n")
        has_played_before = False
        valid_answer = False
        while not valid_answer:
            answer = raw_input("Welcome! Have you played this game before? (y/n):")
            if len(answer) < 1:
                pass
            elif answer.lower()[0] == 'y':
                has_played_before = True
                valid_answer = True
            elif answer.lower()[0] == 'n':
                has_played_before = False
                valid_answer = True
            else:
                print("\nYou have given an invalid response... Try again:\n")
        if has_played_before:
            print("Okay, have fun!\n")
        elif not has_played_before:
            print("You will make a rule for a set of words.  For example, your \nwords must all have a double letter in them (like 'Green' and 'Door')\nin order to be classified as 'correct.' \nThis rule can deal with the number of or position of letters, \nthe presence of a specific letter, whether something is a \nvowel or consonant, or the part of speech of the word.  \nThe computer will try to guess your rule based on the words\nyou enter that follow the rule.  Have fun!\n")

    def get_y_words(self, n):
        i = 1
        print("Enter %d words that belong in your set." % n)
        while i <= n:
            y_word = raw_input("Word %i: " % i)
            y_word = y_word.lower()
            if len(y_word) < 1:
                print("Please enter a word this time.")
            elif y_word in self.known_y_words:
                print("You already entered that word.")
            else:
                i += 1
                self.known_y_words.append(y_word)

    def get_n_words(self, n):
        i = 1
        print("Now, enter %d words that do not belong in your set." % n)
        while i <= n:
            n_word = raw_input("Word %i: " % i)
            n_word = n_word.lower()
            if len(n_word) < 1:
                print("Please enter a word this time.")
            elif n_word in self.known_n_words:
                print("You already entered that word.")
            elif n_word in self.known_y_words:
                print("You said that word belongs in your set. Stop contradicting yourself.")
            else:
                i += 1
                self.known_n_words.append(n_word)

    def nltk_word(self):
        #drat, I forget how to reference the corpus.
        self.words = nltk.corpus.brown.words('ch01')
        numstrings = [str(i+1) for i in range(10, 30)]
        for num in numstrings: 
            self.words = self.words + nltk.corpus.brown.words('ch%s'%num)
        return self.words
        
    def word_match(self, rule): #finds word in self.words that matches the rule and returns that word, deleting it and everything before it from the list.
        pass

    def word_guess(self, rule, count):
        #cycle through an nltk corpus until you find a word that matches the rule and return that.
        nltk_word = "YOLO" 
        correct = input("Does the word %s follow your rule? (y/n) " % nltk_word).lower()[0]
        if count == 5 and correct == 'y':
            print("Looks like I've got it figured out!")
            #call whatever we need to play again
        elif correct == 'y': 
            word_guess(rule, count+1)
        elif correct == 'n': 
            print("Well shucks. Please enter more words to help me guess better.")
            get_y_words(2)
            get_x_words(2)
        

    def interaction_loop(self):
        self.play_again = True
        self.welcome_msg()
        num_words = 5
        while self.play_again == True:
            self.get_y_words(num_words)
            self.get_n_words(num_words)
            num_words = 2
            rule = best_feature()
            word_guess(rule, 0)
            #if 5 words are correct, computer wins.
            self.play_again = False

    def best_feature(self):
        return self.most_likely_features[0][0]

    def test(self):
        train_list = [('bosom', 'y'), ('ipad', 'n'),
                  ('calendar', 'n'), ('bottle', 'y'),
                  ('barn', 'n'), ('breckbill', 'n'),
                  ('bob', 'y'), ('bong', 'y'),
                  ('black', 'n')]
        print len(self.nltk_word('double_letters'))
        rules = RuleWizard(train_list)
        rules.find_best_rules()

instance = Game()
instance.test()
#instance.interaction_loop()
