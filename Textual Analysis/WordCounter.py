"""
Author : Mohammed Yusuf Khan
Version : 1.0.3
"""


# define a new function "counterfunc"
def counterfunc():

    """
    Reading the values that have to be searched and the counter should be performed on
    The file to be manipulated is also read by the input provided.
    """
    word1 = input("Enter the word1>> ")
    word2 = input("Enter the word2>> ")
    fileopen = input("Enter the file to open>> ")


    wordDictionary = {} # Creating a new dictionary

    wordDictionary[word1] = 0 #Initialize the value to zero
    wordDictionary[word2] = 0 #Inititalize the value to zero

    fileopenconn = open(str(fileopen)) #open the file , will open in read mode


    #print (fileopenconn.read()) #test

    for line in fileopenconn:

        words = line.lower().strip().split(' ') #will lower case the values and make them easy to iterate through the loop


        for word in words:
            if word == word1:
                wordDictionary[word1] = wordDictionary[word1] + 1
            elif word == word2:
                wordDictionary[word2] = wordDictionary[word2] + 1


    fileopenconn.close() # closing the file
    return wordDictionary[word1], wordDictionary[word2] #returning the values


print(counterfunc())
