from math import log
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
if __name__ == '__main__':
    myDat,labels=createDataset()
    print(myDat)
    print(calcShannonEnt(myDat))
    print(spiltDataset(myDat,0,0))
    print(chooseBestFeature(myDat))