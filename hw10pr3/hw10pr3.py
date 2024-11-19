# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.
#
# For another example of such a file, see
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
# Name: Michael Mumo
#

#
# First, some helper/example functions for files + text ...
#
# To make the examples work, you should have the text file named "a.txt"
# in the same directory as this .py file!
#
# If you _don't_ have "a.txt", create it.  Here are its contents:
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!
"""


def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    # We assume the "utf-8" encoding, which accepts more characters than plain ASCII
    #
    # Other common codings welcome, e.g., utf-16 or latin1
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #
    f = open(filename, encoding = 'utf-8')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string    # See https://docs.python.org/3/library/string.html
                 # Note: str is different: docs.python.org/3/library/stdtypes.html#textseq

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...




"""
[a] What was in the file you analyzed?   -->    Martin Luther King Jr. I have a dream speech.


[b] How many words did it have?  -->     1409 words
    Use word_count.

[c] How many characters did it have?  -->       7768

    Note: there's no function for this, but len(get_text("a.txt")) will do it!


[d] How many _distinct_ words did it have?  -->     467 distinct words
    Use vocab_count.
    Adapt as you see fit...

[e] What are three words that appeared unusually often for this text?  --> colored - 12, freedom - 15, dream - 11
    - ...relative to a generic distribution of "all text"

    For example, it's _not_ unusual if "the" or "a" are the
    most common words in an English text.


[f] Other thoughts/insights?! MLK uses lots of repetition

"""

#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your 500-word "CS-Essay,"" with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)       # Then copy the "essay" below ...
#

#
# Function #1  (createDictionary)
#
def createDictionary(text):
    """ Creates a dictionary storing a word as a key and the values as the words that follow it.
    """
    LoW = text.split()

    d = {}
    pw = '$'   # pw indicates previous word

    for nw in LoW:   # nw indicates next word
        if pw not in d:
            d[pw] = [nw]   # start with a list of one element
        else:
            d[pw] += [nw]  # add to the list, already present

        pw = nw     # before re-looping, assign pw to be the just-handled "new" word (nw)

        #
        # Here, check for whether that new previous word, pw, ends in 
        # punctuation -- if it _does_ then set pw to be '$'
        # that way, it will be back at the start of a new sentence!
        #

        if pw[-1] == '.' or pw[-1] == '?' or pw[-1] == '!':
            pw = '$'

    return d


import random

#
# Function #2   (generateText)
#
def generateText(d, N):
    """Takes in a dictionary d from createDictionary and generates N number of words in an essay.
    """
    print()  # start by printing a newline

    current_word = "$"

    for i in range(N):
        next_word = random.choice(d[current_word])
        # Here's how to print so that things don't always start on the next line
        # Using end = ' ' stops it going to the next line
        
        print(next_word, end = ' ')

        current_word = next_word
        if next_word[-1] == '.' or next_word[-1] == '!' or next_word[-1] == '?':
            current_word = '$'

    print()                  # Final print, newline




#
# Your 500-or-so-word "CS Essay" (paste into the triple-quoted strings below):
#
"""
Martin Luther King Jr's I have a dream speech.


I sing. I would be able to our hope. Some of material prosperity. Go back to pray together, to millions of our modern cities, knowing that somehow this check, a promise that unearned suffering is to transform the heightening Alleghenies of justice. 
Thank God Almighty, we will continue to jail together, to Louisiana, go back to Alabama, with new meaning of happiness. Let freedom ring, when all of freedom ring from the quicksand of democracy. 
Instead of former slaves and the hilltops of American lives on this promissory note to overlook the determination of Georgia. We can never be able to vote. 
So we have come to climb up that one day this sacred obligation, America of cooling off steam and the dark and tomorrow. 
When the curvaceous slopes of honoring this nation where your quest for freedom in the valley of the nation from a smaller ghetto to underestimate the day when all men and Catholics, 
will be satisfied as white men, would be judged by the motels of color are insufficient funds in Mississippi cannot be able to go back to which every city, we will be made plains and the life liberty and live in the time to his citizenship rights. 
But one day right down in New York. I am not wallow in the history of their captivity. We cannot gain lodging in a dream today. It is an invigorating autumn of happiness. 
It is not free. There will continue to fall heir. With this nation until justice is the quicksand of New Hampshire. With this must become true. Thank God Almighty, we have a dream that day this nation. 
Five score years later, the time to Georgia, go back to join with new meaning of the colored citizens. Now it ring from every valley of a beginning. 
Let freedom and a reality to sit down in Alabama, go to which to vote. You have a sense we have a dream today. I have come from areas where my friends, 
we will now be content will be able to go down in the great American, in Alabama little black men are not an end the time to make justice is bankrupt. 
I will not pass until justice is still sadly crippled by signs stating “for white girls will continue to underestimate the long as long as long as a beginning. 
I have a dream that America is still have a great American, in the colored citizens. We cannot be transformed into an exile in the inalienable rights of brotherhood. 
Thank God Almighty, we let freedom together, knowing that I am not time to Mississippi, a dream that one day out of our modern cities, 
knowing that there are stripped of you today to Georgia, go back to believe that one day. We have a reality to join hands and nullification; 
that unearned suffering is the luxury of the table of freedom and righteousness like a dream. One hundred years later, the words of democracy. I have 



"""
