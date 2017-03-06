"""
Author: Mohammed Yusuf khan
Version: 1.0.4
"""

def Lex(fname):
    lexSet = set()
    lex_conn = open(fname)

    for line in lex_conn:
        lexSet.add(line.strip())
    lex_conn.close()

    return lexSet



def sentiment(path):
    decisionsList = []
    review = []

    postiveLexicon = Lex('positive-words.txt')
    negativeLexicon = Lex('negative-words.txt')

    fin = open(path)
    for line in fin:
        positiveList = []
        negativeList = []

        line = line.lower().strip()
        review.append(line)

        words = line.split(' ')

        for word in words:
            if word in postiveLexicon:
                positiveList.append(word)
            elif word in negativeLexicon:
                negativeList.append(word)



        decision = 0

        if len(positiveList) > len(negativeList):
            decision = 1
        elif len(negativeList) > len(negativeList):
            decision = -1
        decisionsList.append(decision)

        fin.close()

        return review,  decisionsList

if __name__ == "__main__":
    review, decisionsList = sentiment('textfile')
    for i in range(len(review)):
        print(review[i], decisionsList[i])
