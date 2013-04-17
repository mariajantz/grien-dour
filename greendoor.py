from classifier import classify

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

    def get_y_words(self):
        i = 1
        print("Enter 5 words that belong in your set.")
        while i < 6:
            y_word = raw_input("Word %i: " % i)
            y_word = y_word.lower()
            if len(y_word) < 1:
                print("Please enter a word this time.")
            elif y_word in self.known_y_words:
                print("You already entered that word.")
            else:
                i += 1
                self.known_y_words.append(y_word)

    def get_n_words(self):
        i = 1
        print("Now, enter 5 words that do not belong in your set.")
        while i < 6:
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

    def interaction_loop(self):
        self.play_again = True
        self.welcome_msg()
        while self.play_again == True:
            self.get_y_words()
            self.get_n_words()
            self.play_again = False

    def best_feature(self):
        return self.most_likely_features[0][0]

    def test(self):
        #self.interaction_loop()
        self.most_likely_features = classify()
        print self.best_feature()

instance = Game()
#instance.test()
instance.interaction_loop()

