           *********************
           *** Cryptophilia! ***
           *********************

A simple text encryption program written in Python 2.6, by:

           Rafael Espericueta
           Professor of Mathematics
           Bakersfield College
           http://www2.bc.cc.ca.us/resperic

It uses the following libraries: string, scipy, mpmath.


# License #

Feel free to use this as you like, free of any copyright concerns;
please just keep it thusly unemcumbered, credit the author, & have fun!
 

# Overview #

To encode a text, imagine the alphabet alongside a 'rolled' version.  For
example, if the alphabet consists of 6 letters (a,b,c,d,e,f) and it is shifted
by 2, we would get

                     (a,b,c,d,e,f)
                     (e,f,a,b,c,d),

which we interpret as the letter 'a' being encoded as 'e', 'b' as 'f', etc., a
simple cipher. Such ciphers are of course easy to decode. Cryptophilia performs
a different shift for each character being encoded. The alphabet used consists
of the following 100 characters (some are "white space"):

     0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
     !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c

The amount of each successive shift is obtained from the base 100 expansion of
an irrational number entered as a key. The default key is the famous circle 
constant, pi. The user may change the key as they wish, but the key must be
a python mathematical expression.  Some example valid keys:

   pi, exp(1.6613309332), sqrt(3), pi**3*sqrt(exp(0.234987)), 4/pi**1.2345

A good key evaluates to an irrational number R such that  1 < R < 10.

Pairs of digits of the key's decimal expansion form indices into our 100 letter
alphabet.  Decoding and encoding of a message must use the same key. Currently,
the key is 10000 digits long, which can encode an approximately 5000 character
message without repeating the successive pattern of shifts.

One could encode a message, and then encode that encoded message with yet
another key. By such multiple encodings, one can obtain messages that have
multiple parts, with some recipients able to decode part but not all of the
message. 

Included is an encoded file, secretcode.txt, that you may read in to decode,
using the default key, pi.  It takes a few seconds to decode, as this is a long
file.  Enjoy!   

