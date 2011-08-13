'''
 File: Cryptophilia.py

 Author: Rafael Espericueta
         Professor of Mathematics
         Bakersfield College

 Desc: Encodes or decodes text and text files with user entered key.
       The key consists of an irrational number.  Some examples:
       
            pi,  pi**2, exp(3.14), sqrt(127), sqrt(5+pi), etc...
            
       See CryptoClass.py for the gory details.
            
 Feel free to use this as you like, free of any copyright concerns;
 please just keep it thusly unemcumbered, credit the author,
 & have fun!

'''

from Tkinter import Tk
from CryptophiliaGUI import *


def main():
    root = Tk()
    app = CryptoGUI_tk(root)
    root.mainloop()


if __name__ == '__main__':
    main()
