import random


class Hangman:

    def __init__(self):
        self.letter_list = []
        random.seed()
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.check = random.choice(self.words)
        self.check_copy = ["-" for i in self.check]

    def __repr__(self):

        return "H A N G M A N\nType 'play' to play the game, 'exit' to quit:"

    def rand_words(self):
        option = input('Type "play" to play the game, "exit" to quit:')
        if option == "play":
            self.word_output()
        else:
            exit()

    def input(self):
        self.letter = input('Input a letter: ')
        if len(self.letter) > 1:
            print("You should input a single letter")
            return False
        if self.letter in self.letter_list:
            print("You already typed this letter")
            return False
        elif self.letter.islower():
            self.letter_list += [self.letter]
            return True
        else:
            print("It is not an ASCII lowercase letter")
            return False

    def word_output(self):
        i = 8
        while i != 0:
            print("\n", "".join(self.check_copy))
            if self.input():
                if self.letter in self.check:
                    for k in range(len(self.check)):
                        if self.check[k] == self.letter:
                            self.check_copy[k] = self.letter
                        elif self.check_copy[k] == self.letter:
                            print("No improvements")
                            i -= 1
                else:
                    print("No such letter in the word")
                    i -= 1
        if "-" not in self.check_copy:
            print("You guessed the word!\nYou survived!\n")
        else:
            print("You are hanged!\n")
        self.rand_words()


print(Hangman())
Hangman().rand_words()
