'''
 File: CryptoClass.py

 Author: Rafael Espericueta
         Professor of Mathematics
         Bakersfield College


 Desc: The crypto class allows one to encode and decode text. This is
       accomplished using the digits of a chosen irrational number (the key).
       The digits are thought of as base 100, so each digit can be used as a
       shift, effectively rolling our 100 character alphabet by that amount.
       Each successive character is decoded by each successive digit of the
       irrational number's expansion, which are approximately random yet are
       easy to generate.

 Feel free to use this as you like, free of any copyright concerns;
 please just keep it thusly unemcumbered, credit the author,
 & have fun!
 
'''

import string as st
from scipy import *
from mpmath import *


class crypto:
    """ Class methods encode and decode text, and perform statistics on text (coded or otherwise) """
    def __init__(self):
        #
        mp.dps = 10000 # digits of precision is the default
        
        # the irrational number used to encode and decode,
        # as a 10000 digit string.  Just use the digits
        # to the right of the decimal point (centimal point?).
        self.sPi = str(pi)  # the default
        self.sPi = self.sPi[self.sPi.index('.')+1:]
        

    def encode(self, text):
        place = 0
        codedtext = ''
        for c in text:
            place %= 99  # so thatplace+2 <= 100
            shift = int(self.sPi[place:place+2])
            place += 2
            # "st.printable" constitutes our base 100 "digits"
            table = [st.printable, st.printable[shift:] + st.printable[:shift]]
            #table = st.maketrans(st.printable, st.printable[shift:] + st.printable[:shift])
            #codedtext += c.translate(table)  
            codedtext += table[1][table[0].index(c)]
        return codedtext


    def decode(self, codedtext):
        place = 0
        decodedtext = ''
        for c in codedtext:
            place %= 99  # so thatplace+2 <= 100
            shift = int(self.sPi[place:place+2])
            place += 2
            #table = st.maketrans(st.printable[shift:] + st.printable[:shift], st.printable)
            #decodedtext += c.translate(table)
            table = [st.printable[shift:] + st.printable[:shift], st.printable]
            decodedtext += table[1][table[0].index(c)]
        return decodedtext
    

    def change_key(self, newkey):
        self.sPi = str(eval(newkey))
        self.sPi = self.sPi[self.sPi.index('.')+1:]
        

    def change_digitsofprecision(self, numdigits):
        mp.dps = numdigits   # default = 10000
        
        
    def countcharacters(self, text):
        """ How many of each of the 100 "characters" occur
            in the coded text?  Answer returned as a list.  """
        count = [0]*100
        for i in range(100):
            for c in text:
                if c==st.printable[i]:  count[i] += 1
        return count
                

