"""
Author : Mohammed Yusuf Khan
Version : 1.0.3
"""

#define function
def frequentWord():
    wordDictionary = {} #Initialize the dictionary

    wordfile = input("Enter the name of the file>> ") #read the file
    wordfileconn = open(wordfile)

    for line in wordfileconn:

        words = line.lower().strip().split(' ') #words are lower-cased and will be easy to iterate through the loop

        for word in words: #for all the words
            if word in wordDictionary: #if the word is in our dictionary
                #wordDictionary[word] = 0
                wordDictionary[word] = wordDictionary[word] + 1 #increment by 1
            else:
                wordDictionary[word] = 1 # Inititalize 1

    temp = 0 #temp variable
    for k, v in wordDictionary.items(): #to iterate through the dictionary
        if v > temp:
            temp = v

    for k, v in wordDictionary.items():
        if v == temp:
            return k , v

    wordfileconn.close() # close the file

print(frequentWord())
