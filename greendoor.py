from rulewizard import *
import nltk

class Game:
    def __init__(self):
        self.train_list = list()
        self.guessed_words = list()

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
        '''Asks the user for n words that follow the rule'''
        i = 1
        print("Enter %d words that belong in your set." % n)
        while i <= n:
            y_word = raw_input("Word %i: " % i)
            y_word = y_word.lower()
            if len(y_word) < 1:
                print("Please enter a word this time...")
            elif (y_word, 'y') in self.train_list:
                print("You already gave me that word.")
            else:
                i += 1
                self.train_list.append((y_word, 'y'))

    def get_n_words(self, n):
        '''Asks the user for n words that do not follow their rule.'''
        i = 1
        print("Now, enter %d words that do not belong in your set." % n)
        while i <= n:
            n_word = raw_input("Word %i: " % i)
            n_word = n_word.lower()
            if len(n_word) < 1:
                print("Please enter a word this time.")
            elif (n_word, 'n') in self.train_list:
                print("You already entered that word.")
            elif (n_word, 'y') in self.train_list:
                print("You said that word belongs in your \'yes\' set. Stop contradicting yourself.")
            else:
                i += 1
                self.train_list.append((n_word, 'n'))

    def nltk_word(self):
        '''Makes a list of nltk words from the Brown corpus that we can cycle through later.'''
        self.words = nltk.corpus.brown.words('ch01')
        numstrings = [str(i+1) for i in range(10, 30)]
        for num in numstrings: 
            self.words = self.words + nltk.corpus.brown.words('ch%s'%num)
        
    def word_match(self): 
        '''
        Finds word in self.words that matches the rule and returns that word, 
        deleting it and everything before it from the list.
        '''
        index = 0
        word = ''
        for i in range(len(self.words)):
            if self.wizard.does_word_match_current_best_rule(self.words[i]): # obeys rule:
                if self.words[i].lower() not in self.guessed_words:
                    word = self.words[i]
                    break
        #return that word
        self.words = self.words[i+1:]
        return word

    def word_guess(self, count):
        '''Finds a word in the list of nltk words we made that it thinks follows the rules, asks the 
        user whether it is correct, and continues until it gets 5 in a row correct. If incorrect, 
        asks the user to supply two more correct and incorrect words. 
        '''
        #cycle through an nltk corpus until you find a word that matches the rule and return that.
        word_to_guess = self.word_match() 
        correct = raw_input("Does the word \"%s\" follow your rule? (y/n) " % word_to_guess).lower()[0]
        if count == 5 and correct == 'y':
            print("Looks like I've got it figured out!")
            self.wizard.call_dat_shiznat()
            return True
        elif correct == 'y': 
            self.guessed_words.append(word_to_guess.lower())
            self.word_guess(count+1)
        elif correct == 'n': 
            print("Well shucks. Please enter more words to help me guess better.")
            self.wizard.amputate_first_significant_feature()
            self.get_y_words(2)
            self.get_n_words(2)
            self.word_guess(0)
        

    def interaction_loop(self):
        self.play_again = True
        self.welcome_msg()
        num_words = 5
        self.nltk_word()
        while self.play_again == True:
            self.get_y_words(num_words)
            self.get_n_words(num_words)
            self.wizard = RuleWizard(self.train_list)
            self.wizard.find_best_rules()
            self.word_guess(0)
            #if 5 words are correct, computer wins.
            self.play_again = False

    def best_feature(self):
        return self.most_likely_features[0][0]

    def play_again(self): 
        '''Asks user if they want to play again.'''
        if input("Do you want to play again? (y/n) ").lower()[0] == 'y':
            return True
        else: 
            return False

    def test(self):
        train_list = [('poppies', 'y'), ('racket', 'n'),
                  ('somethin', 'n'), ('puppies', 'y'),
                  ('blodnasir', 'n'), ('vietnam', 'n'),
                  ('freedom', 'y'), ('commies', 'y'),
                  ('black', 'n')]
        self.nltk_word()
        self.wizard = RuleWizard(train_list)
        self.wizard.find_best_rules()
        self.word_guess(0)
        while self.play_again:
            #Do we need the other functions in here? 
            self.word_guess(0)
            self.play_again



instance = Game()
instance.interaction_loop()
#instance.interaction_loop()
