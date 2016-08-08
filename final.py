import sys
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


def train():
    global unigrams, bigrams, bigramsFD, unigramsFD
    for line in open("corpus.txt", "r"):
        sentence = '0'+line.strip()+'0'
        token=list(sentence)
        unigrams+=token
        bigrams+=(ngrams(token,2))
    bigramsFD = nltk.FreqDist(bigrams)
    unigramsFD = nltk.FreqDist(unigrams)

    
    bigramsLen = len(bigramsFD)
    for bigram in bigramsFD:
        probDist[bigram] = (bigramsFD[bigram]+1.0)/ (unigramsFD[bigram[0]]+bigramsLen)

def test():
    global initalProb
    finalResults = []
    for line in open("test.txt", "r"):
        sentence = list(line.strip())
        prob = []
#Commented out section
        mostProbable(sentence, "0", len(sentence), finalResults, 0, prob)

def mostProbable(sen, res, n, finalResults, i, prob):
    index = len(res)-1
    print res, index
    if n == index:
        finalResults.append(res)
        print finalResults
        return
    if (index > len(prob)-1) or len(prob) == 0:
        calculateProbability(prob, sen, res)
        #print i, len(prob[index]), res
        #print prob[index]
    print prob[len(res)-1]
    print index, i

    res+=prob[index][i][0][1]

    mostProbable(sen,res,n,finalResults,i,prob)
    res = res[0:len(res)-1]
    if len(prob[len(res)-1]) > i+1:
        
        mostProbable(sen,res,n,finalResults,i+1,prob)

def calculateProbability(prob, sen, res):
    prev = res[-1]
    index = len(res)-1
    letters = list(sen)
    prob.append([])
    for letter in res:
        if letter != '0':
            letters.remove(letter)
    for letter in letters:
        bigram = (prev, letter)
        tempProb = (bigramsFD[bigram] + 1.0)/(unigramsFD[prev]+len(bigramsFD)) 
        prob[index].append(tuple((bigram, tempProb)))
    sorted(prob[-1], key=lambda x: x[1])

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
