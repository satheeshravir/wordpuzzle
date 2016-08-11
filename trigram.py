import sys, re
from collections import defaultdict
import nltk
from nltk.util import ngrams
from operator import itemgetter


bigrams = []
unigrams = []
probDist = defaultdict(dict)
initalProb = []
bigramsFD = nltk.FreqDist([])
unigramsFD = nltk.FreqDist([])
dictionary = []
memoization = {}

def train():
    global unigrams, bigrams, bigramsFD, unigramsFD
    for line in open("corpus.txt", "r"):
        if re.match("^[a-zA-Z]*$", line):
            line = line.strip()
            dictionary.append(line)
            sentence = '0'+line+'0'
            token=list(sentence)
            unigrams+=token
            bigrams+=(ngrams(token,2))
    bigramsFD = nltk.FreqDist(bigrams)
    unigramsFD = nltk.FreqDist(unigrams)
    
def wordBreak(s, dict):
    sLen = len(s)
    possible = [False for i in range(sLen + 1)]
    possible[0] = True

    for i in range(sLen):
      for j in range(i + 1):
        if possible[j] and s[j:i + 1] in dict:
            possible[i + 1] = True
            break;

    return possible[sLen]


def test():
    global initalProb
    finalResults = []
    prob = []
    for line in open("test.txt", "r"):
        sentence = list(line.strip())
        for i in range(len(sentence)):
            prob.append([])
        probIndex = [0] * len(sentence)
        probIndex[0] = 7
#Commented out section
        mostProbable(sentence, "0", len(sentence), finalResults, prob, probIndex)

'''def mostProbable(sen, res, n, finalResults, prob, probIndex):
    index = len(res)-1
    print res, index
    if n == index:
        finalResults.append(res)
        return
    if (index > len(prob)-1) or len(prob) == 0:
        calculateProbability(prob, sen, res)
        #print i, len(prob[index]), res
        #print prob[index]

    res+=prob[index][probIndex[index]][0][1]

    mostProbable(sen, res, n, finalResults, prob, probIndex)
    res = res[0:len(res)-1]
    if probIndex[index] < len(prob[index])-1:
        probIndex[index]+=1
        mostProbable(sen,res,n,finalResults,prob, probIndex)

#Latest
def mostProbable(sen, res, n, finalResults, prob, probIndex):
    index = len(res)-1
    if n == index:
        print res
        finalResults.append(res)
        return
    if (index > len(prob)-1) or len(prob) == 0:
        calculateProbability(prob, sen, res)
    res+=prob[index][probIndex[index]][0][1]
    mostProbable(sen, res, n, finalResults, prob, probIndex)
    if probIndex[0] == n:
        return

    if probIndex[index] < len(prob[index])-1:
        probIndex[index]+=1
        res = res[0:len(res)-1]
        probIndex[index] = 0
        del prob[index]
        mostProbable(sen, res, n, finalResults, prob, probIndex)
    else:
        probIndex[index] = 0'''

def mostProbable(sen, res, n, finalResults, prob, probIndex):
    index = len(res)-1
    if n == index:
        for i in range(20,15,-1):
            if wordBreak(res[1:i], dictionary):
                print res 
            return
    if len(prob) == 0 or len(prob[index]) == 0:
        calculateProbability(prob, sen, res)
    res+=prob[index][probIndex[index]][0][1]
    mostProbable(sen, res, n, finalResults, prob, probIndex)
    if probIndex[0] == n:
        return

    if probIndex[index] < len(prob[index])-1:
        probIndex[index]+=1
        res = res[0:len(res)-1]
        for k in range(index+1, len(prob)):
            probIndex[k] = 0
            prob[k] = []
        mostProbable(sen, res, n, finalResults, prob, probIndex)
    else:
        probIndex[index] = 0
    
    
def calculateProbability(prob, sen, res):
    prev = res[-1]
    index = len(res)-1
    letters = list(sen)
    for letter in res:
        if letter != '0':
            letters.remove(letter)

    for letter in letters:
        bigram = (prev, letter)
        if bigram in memoization:
            prob[index].append(tuple((bigram, memoization[bigram])))
        else:
            tempProb = (bigramsFD[bigram] + 1.0)/(unigramsFD[prev]+len(bigramsFD)) 
            prob[index].append(tuple((bigram, tempProb)))
            memoization[bigram] = tempProb
    prob[index] = list(set(prob[index]))
    #prob[-1].sort(key=lambda x: x[1], reverse=True)
    prob[index] = sorted(prob[index], key=lambda x: x[1], reverse=True)


'''        mostProbableStart(sentence)
        sorted(initalProb, key=lambda x: x[1])
        calculateMostProbable(initalProb, sentence)

def calculateMostProbable(initalProb, line):
    letterList = []
    explore = list(line)
    result = ""
    for bigram in initalProb:
        letterList.append(bigram[0][1])
        result+=bigram[0][1]
        overallProb = result
        while len(letterList) < len(line): 
            for letter in explore:
                if letter not in letterList:
                    tempProb = overallProb * bigramsFD[]









def mostProbableStart(sentence):
    global initalProb
    token = list(sentence)
    bigramsLen = len(bigramsFD)
    for letter in token:
        bigram = ("0",letter)
        prob = (bigramsFD[bigram]+1.0)/ (unigramsFD[bigram[0]]+bigramsLen)
        initalProb.append(tuple((bigram, prob)))'''



train()
test()
