# -*- coding: utf-8 -*-

import unirest

URL = 'https://wordsapiv1.p.mashape.com/words/'
KEY = 'WRuC7cfE9PmshM86JyjTIorUWozqp1UQn6Mjsni25AVVaLP08l'

class Adapter:
    """
    Main class of adapter

    """

    def __init__(self, arguments):
        """
        Initialize variables

        :param arguments: dictionary
        """

        self.language = arguments['lang']

    def request(self, params={}):
        """
        Make a GET request to API

        :return: dictionary
        """

        response = unirest.get(URL, headers={
                                       'X-Mashape-Key': KEY,
                                       'Accept': 'application/json'
                                   }, params=params)

        return response