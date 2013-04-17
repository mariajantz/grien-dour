from classifier import classify

class Game:
    def current_best_feature(self):
        return self.most_likely_features[0][0]

    def interaction_loop(self):
        self.welcome_msg()

    def test(self):
        #self.interaction_loop()
        self.most_likely_features = classify()
        print self.current_best_feature()

    def welcome_msg(self):
        has_played_before = False
        valid_answer = False
        while not valid_answer:
            print()
            answer = raw_input("Welcome! Have you played this game before? (y/n):")
            if answer.lower()[0] == 'y':
                has_played_before = True
                valid_answer = True
            elif answer.lower()[0] == 'n':
                has_played_before = False
                valid_answer = True
            else:
                print("\nYou have given an invalid response... Try again:\n")
        print("\n")
        if has_played_before:
            print("Okay, have fun!\n")
        elif not has_played_before:
            print("You will make a rule for a set of words.  For example, your \nwords must all have a double letter in them (like 'Green' and 'Door')\nin order to be classified as 'correct.' \nThis rule can deal with the number of or position of letters, \nthe presence of a specific letter, whether something is a \nvowel or consonant, or the part of speech of the word.  \nThe computer will try to guess your rule based on the words\nyou enter that follow the rule.  Have fun!\n")


instance = Game()
instance.test()

