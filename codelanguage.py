#We are writing a python progran to translate a messange into secret code language 
#Rules 
'''
if the word contains at lease three characters, remove the first char and append it into the end
after that append three random characters at the starting and the ending of the ctring
else: simply reverse the string
#Decoding
if the word contains less than 3 char simply reverse it
else: remove three random characters from starting and the ending and then remove the last letter and append 
it into the begining
'''

import random
import string

user = input("What is your name? ").lower()
print(user)

def encode(user):  # Pass user as a parameter
    if len(user) >= 4:
        newString = user[1:] + user[0]
        randStringBeg = ''.join(random.choices(string.ascii_lowercase, k=3))
        randStringEnd = ''.join(random.choices(string.ascii_lowercase, k=3))
        print(newString)
        doneString = randStringBeg + newString + randStringEnd
        print(doneString)
    else:
        reversedString = user[::-1]
        print(reversedString)

# Call the encode function, passing user as an argument
encode(user)