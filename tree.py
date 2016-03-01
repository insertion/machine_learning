#encoding:UTF-8
from math import log
import operator
def calcShannonEnt(dataset):
    numEntries=len(dataset)#计算数据集的总长度
    labelCounts={}#建立种类字典
    for featVec in dataset:#对数据集中的每个元素，元素是table形式的，table的最后一位表示元素的类别,决策结果
        currentlabel=featVec[-1]#[-1]表示最后一个
        if currentlabel not in labelCounts.keys():#如果不再字典内，新建一个，并初始化
            labelCounts[currentlabel]=1
        else:
            labelCounts[currentlabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
#        print(labelCounts[key],numEntries)
        prob=float(labelCounts[key])/numEntries#计算没个种类的概率
#        print(prob)
        shannonEnt-=prob*log(prob,2)#期望熵
    return shannonEnt
def createDataset():
    dataset=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels=['no surfacing','flippers']
    return dataset,labels 
def spiltDataset(dataset,axis,value):#数据集，维度，值,这里用select更好理解
    retDateset=[]
    for featVec in dataset:#对每个元素，去掉一个维度
        if featVec[axis]==value:
            reduceFeatvec=featVec[:axis]
            reduceFeatvec+=featVec[axis+1:]#拼接，去掉了axis维度
            retDateset.append(reduceFeatvec)
    return retDateset
def chooseBestFeature(dataset):
    numFeatures=len(dataset[0])-1#这里减一是因为从0开始数
    baseEntropy=calcShannonEnt(dataset)
    bestInfoGain=0.0
    bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataset]#取每个元素的第i个属性的值
        uniquevalue=set(featList)
        newEntropy=0.0
        for value in uniquevalue:#对于每个属性，可以分为几类？
            subDateset=spiltDataset(dataset,i,value)
            prob=len(subDateset)/float(len(dataset))
            newEntropy+=prob*calcShannonEnt(subDateset)
        infoGain=baseEntropy-newEntropy
        if infoGain>bestInfoGain:
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():#字典的key中保存着类别
            classCount[vote]=1
        else:
            classCount+=1
    sortedclassCont=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)#itermgetter 定义了一个函数，指定对哪一维进行排序
    return sortedclassCont[0][0]
def createTree(dataset,labels):
    classList=[example[-1] for example in dataset]#取数据集的最后一位作为类别
    if classList.count(classList[0])==len(classList):#返回classlist[0]的出现次数
        return classList
    if len(dataset[0])==1:#表示数据集中的属性只剩下一个了,无法继续向下划分
        return majorityCnt(classList)
    bestFeat=chooseBestFeature(dataset)#返回的是序号
    bestFeatlabel=labels[bestFeat]#根据序号在labels中找到属性
    myTree={bestFeatlabel:{}}#????嵌套字典，代表树
    del(labels[bestFeat])#在列表中delete bestfeat
    featvlaues=[example[bestFeat] for example in dataset]#列出所有bestfeat属性的值
    uniquevlas=set(featvlaues)#删除重复项
    for value in uniquevlas:#对于最佳属性的所有可能值
        sublabels=labels[:]
        myTree[bestFeatlabel][value]=createTree(spiltDataset(dataset,bestFeat,value),sublabels)
        #多维字典，类似多维数组，value为key,node
    return myTree
def storeTree(inputTree,filename):
    import pickle
    fw=open(filename,'wb')
    pickle.dump(inputTree,fw)
    fw.close()
def getTree(filename):
    import pickle
    fr=open(filename)
    return pickle.load(fr)
if __name__ == '__main__':
    myDat,labels=createDataset()
    #print(myDat)
    #print(calcShannonEnt(myDat))
    #print(spiltDataset(myDat,0,0))
    #print(chooseBestFeature(myDat))
    #storeTree(createTree(myDat,labels),'classifierTree.txt')
    storeTree(createTree(myDat,labels),'ss.txt')
