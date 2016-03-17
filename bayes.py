# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:42:25 2016

@author: wlei
"""
import numpy
#creates some example data to experiment with
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea','problems', 'help', 'please'],
    ['maybe', 'not', 'take', 'him','to', 'dog', 'park', 'stupid'],
    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
    ['mr', 'licks', 'ate', 'my', 'steak', 'how','to', 'stop', 'him'],
    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec =[0,1,0,1,0,1]#1 is yes 0 is no
    return postingList,classVec
#create a list of all the unique words in all of our documents.  
def createVocababList(dataSet):
    vocabSet=set([])#set可以看成数学意义上的无序和无重复元素的集合
    for token in dataSet:
        vocabSet = vocabSet | set(token)#相当于向vocabulary中添加元素
    return list(vocabSet)#返回一个无序唯一的list
#whether a word from our vocabulary is present or not in the given document.
def setOfWord2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)#create a vectoe of all 0s
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] =1
        else:
            pass
    return returnVec

def train0(trainMatrix,trainCategory):#输入是文章和类别
    numDocs = len(trainMatrix)#表示有多少个文档
    numWords =len(trainMatrix[0])#表示文档中有多少个词汇
    pAbusive = sum(trainCategory)/float(numDocs)#文档中出现脏话的概率
    p0Num=numpy.zeros(numWords)#每个词出现的概率初始化
    p1Num=numpy.zeros(numWords)#
    p0Denom=0.0;p1Denom=0.0
    for i in range(numDocs):#对每个文档来说
        if trainCategory[i] == 1:#如果是脏话文章
            p1Num += trainMatrix[i]#统计词出现的个数
            p1Denom += sum(trainMatrix[i])#总词数
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = numpy.log(p1Num/p1Denom) #在脏文章中词的频率,这里是log，所以分类器中是相加
    p0Vect = numpy.log(p0Num/p0Denom) #在正常文章中词的频率
    return p0Vect,p1Vect,pAbusive
    # two vectors and one probability are returned
    #先计算在不同类中各个属性占的比重，然后各个属性比重相乘再乘以该类的概率，最后哪个类的概率大，就属于哪个类
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + numpy.log(pClass1)#这里本来是×，但是换成log后都变成了+
    p0 = sum(vec2Classify * p0Vec) + numpy.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
        
if __name__ == '__main__':
    tokens,valssVec=loadDataSet()
    myVocabList=createVocababList(tokens)
    trainMat=[]
    for doc in tokens:
        trainMat.append(setOfWord2Vec(myVocabList,doc))
    p0v,p1v,pab=train0(trainMat,valssVec)
    print(pab)
    print(p0v)
    print(p1v)
    
    

