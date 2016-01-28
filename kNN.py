#!/usr/bin/python3
import numpy
import matplotlib
import matplotlib.pyplot as plt
import operator
def file2matrix(filename):
	#infiles everyline have four element ,last one is leble
	files=open(filename)
	lines=files.readlines()
	numberofline=len(lines)
	returnMat=numpy.zeros((numberofline,3))
	# rows and cloms
	classlabvector=[]
	index=0
	for line in lines:
		line=line.strip()
		#removed whitespace
		listformline=line.split('\t')
		# split line by '\t'
		returnMat[index:]=listformline[0:3]
		#write data into everyrows of matrix
		classlabvector.append(int(listformline[-1]))
		#list[-1] to get the last element
		index+=1
	return returnMat,classlabvector
	pass
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
def autonorm(dataset):
	minvalues=dataset.min(0)
	#min(axis=n),0 is the cloumns
	maxvalues=dataset.max(0)
	ranges=maxvalues-minvalues
	print(ranges)
	#normaldataset=numpy.zeros(numpy.shape(dataset))
	#init the dataset
	m=dataset.shape[0]
	normaldataset=dataset-numpy.tile(minvalues,(m,1))
	normaldataset=normaldataset/numpy.tile(ranges,(m,1))
	#correspond element divides
	return normaldataset
	pass
if __name__ == '__main__':
	a,b=createDataset()
	c=clssify0([1,0.5],a,b,3)
	print(c)
	datamat,datalab=file2matrix("datingTestSet2.txt")
	datamat=autonorm(datamat)
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(datamat[:,0],datamat[:,1],50,15.0*numpy.array(datalab))
	plt.show()
	#print(datalab)
