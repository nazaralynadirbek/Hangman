# -*- coding: utf-8 -*-

import unirest

URL = ''
KEY = ''

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

        respone = unirest.get(URL, headers={
                                       'X-Mashape-Key': KEY,
                                       'Accept': 'application/json'
                                   }, params=params)

        return respone.body