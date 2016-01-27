#!/usr/bin/python3
import numpy,operator
def createDataset():
	group=numpy.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=['B','B','A','A']
	return group,labels
def clssify0(inx,dataset,labels,k):
	datasize=dataset.shape[0]
	#print(datasize)
	diffmat=numpy.tile(inx,(datasize,1))-dataset
	print(diffmat,'\n')
	sqdiffmat=diffmat**2
	print(sqdiffmat,'\n')
	sqdistances=sqdiffmat.sum(axis=1)
	#clom is axis==0,row is axis=1
	print(sqdistances)
	distances=sqdistances**0.5
	sortddistnces=distances.argsort()
	classCount={}
	for i in range(k):
		vote=labels[sortddistnces[i]]
		classCount[vote]=classCount.get(vote,0)+1
	sortclasscount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	#sort classcount'interitems
	print(sortclasscount)
	return sortclasscount[0][0]
	pass

if __name__ == '__main__':
	a,b=createDataset()
	c=clssify0([1,0.5],a,b,3)
	print(c)