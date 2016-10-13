# -*- coding: utf-8 -*-

from adapters import Adapter

class Hangman:
    """
    Main class of the game

    """

    def __init__(self, arguments={}):
        """
        Initialize variables

        :param arguments: dictionary
        """

        self._load_dictionary(arguments)

        self.usr_correct = []
        self.usr_incorrect = []

    def _load_dictionary(self, arguments):
        """
        Create an instance of WordsAPI class and create usr_goal array with word

        :param arguments: dictionary
        """

        # Create an instance
        self.dictionary = Adapter({'lang': 'en'})

        # Get word
        response = self.dictionary.request(params={'random': 'true', 'hasDetails': 'hasCategories'})

        self.usr_goal = list(response.body['word'].lower())
        self.usr_goal_definition = response.body['results'][0]['definition']

    def _board(self):
        """
        Create simple board for game

        """

        print 'Goal : ',
        for letter in self.usr_goal:
            if letter in self.usr_correct:
                print letter,
            else:
                print '_',
        print '\n'

        print 'Correctly guessed : ',
        for letter in self.usr_correct:
            print letter,
        print '\n'

        print 'Incorrectly guessed : ',
        for letter in self.usr_incorrect:
            print letter,
        print '\n'

        if len(self.usr_incorrect) >= 3:
            print 'Tips: {} \n'.format(self.usr_goal_definition)

    def _usr_guess(self):
        """
        Get user input and check is it correct guess or not

        """

        while True:
            usr_guess = raw_input('Guess a letter : ')

            if len(usr_guess) != 1:
                print 'Please, enter a single letter'
            elif usr_guess in self.usr_correct or usr_guess in self.usr_incorrect:
                print 'You have already guessed that letter, choose another'
            elif not usr_guess.isalpha():
                print 'Please, enter a letter'
            else:
                break

        if usr_guess in self.usr_goal:
            self.usr_correct.append(usr_guess)
        else:
            self.usr_incorrect.append(usr_guess)

    def _done(self):
        """
        Check game status

        :return: boolean
        """

        return set(self.usr_correct) == set(self.usr_goal)

    def _lose(self):
        """
        Check if player is died

        :return: boolean
        """

        return len(self.usr_incorrect) >= 7

    def run(self):
        """
        Run the game

        """

        print 'HANGMAN GAME'

        while not self._done():
            self._board()
            self._usr_guess()

            if self._lose():
                print 'GAME OVER'
                break

        if self._done():
            print 'Goal word was: {0}'.format(''.join(self.usr_goal))