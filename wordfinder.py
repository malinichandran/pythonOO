"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    """finding random words from file.
    
    >>> wordfinder = WordFinder("words.txt")
    3 words read

    >>> wordfinder.random() in ["one","two","three","four","five","six","seven","eight","nine","ten"]
    True

    >>> wordfinder.random() in ["one","two","three","four","five","six","seven","eight","nine","ten"]
    True

    >>> wordfinder.random() in ["one","two","three","four","five","six","seven","eight","nine","ten"]
    True
    """
    def __init__(self,path):
        self.path=path
        
        file= open(self.path,"r")
        self.words= self.fileread(file)
    def fileread(self,file):
        lst=[]
        
        for line in file:
            newline=line.strip()
            lst.append(newline)
            print(newline)
        length=len(lst)
        print(f"Number of words read={length}")
        return lst
    def ranword(self):
        return random.choice(self.words)
        

class SpecialWordFinder(WordFinder):
    """WordFinder that excludes blank lines and comments.
    
    >>> specialwordfinder = SpecialWordFinder("complex.txt")
    3 words read

    >>> specialwordfinder.random() in ["pear", "carrot", "kale"]
    True

    >>> specialwordfinder.random() in ["pear", "carrot", "kale"]
    True

    >>> specialwordfinder.random() in ["pear", "carrot", "kale"]
    True
    """
    def fileread(self,file):
        return [line.strip() for line in file
                if line.strip() and not line.startswith("#")]


        
        
   
