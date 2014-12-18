#Challenge 1
#12/17/14
#Danielle Brhely

#Design
#create program that print a list a words and won't repeat in a random order
################################

#import
import random

#main
words = ["pineapple", "Pokemon", "Thorin", "Hobbit", "Map", "Google"]
newWord = ""

#Loop
while words:
    word = random.randrange(len(words))
    newWord = newWord + words[word] + " "
    words = words[:word] + words[(word+1):]
print(newWord)
