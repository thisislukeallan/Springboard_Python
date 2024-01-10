"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """WordFinder: finds random words from a dictionary.
    
    >>> wf = WordFinder('words_short.txt')
    3 words read

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True
    """

    def __init__(self, path_to_file):
        """Reads file and prints number of words in file-list"""
        file = open(path_to_file)
        self.words_list = []
        self.make_word_list(file)

        print(f"{len(self.words_list)} words read")

    def make_word_list(self, file):
        """Makes list of words from file"""
        for line in file:
            words = line.strip().split()
            self.words_list.extend(words)

    def random(self):
        """Chooses/returns random word from word list"""
        return random.choice(self.words_list)
    
class SpecialWordFinder(WordFinder):
    """Uses WordFinder, but ignores blank and comment lines in original file
    
    >>> swf = SpecialWordFinder('special.txt')
    4 words read

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True   
    """

    def make_word_list(self, file):
        """Makes list of words form file, ignoring blank lines and comment lines (starts with '#')"""
        for line in file:
            if line.strip() and not line.startswith('#'):
                words = line.strip().split()
                self.words_list.extend(words)