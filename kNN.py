#!/usr/bin/python3
import numpy
import matplotlib.pyplot as plt
from os import listdir
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
def classify0(inx,dataset,labels,k):
	datasize=dataset.shape[0]
	#print(datasize)
	diffmat=numpy.tile(inx,(datasize,1))-dataset
	#print(diffmat,'\n')
	sqdiffmat=diffmat**2
	#print(sqdiffmat,'\n')
	sqdistances=sqdiffmat.sum(axis=1)
	#clom is axis==0,row is axis=1
	#print(sqdistances)
	distances=sqdistances**0.5
	sortddistnces=distances.argsort()
	classCount={}
	for i in range(k):
		vote=labels[sortddistnces[i]]
		classCount[vote]=classCount.get(vote,0)+1
	sortclasscount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	#sort classcount'interitems
	#print(sortclasscount)
	return sortclasscount[0][0]
	pass
def autonorm(dataset):
	minvalues=dataset.min(0)
	#min(axis=n),0 is the cloumns
	maxvalues=dataset.max(0)
	ranges=maxvalues-minvalues
	#print(ranges)
	#normaldataset=numpy.zeros(numpy.shape(dataset))
	#init the dataset
	m=dataset.shape[0]
	normaldataset=dataset-numpy.tile(minvalues,(m,1))
	normaldataset=normaldataset/numpy.tile(ranges,(m,1))
	#correspond element divides
	return normaldataset,ranges,minvalues
	pass
def testclassfiy0():
	horatio=0.10
	datingdatamat,datinglabels=file2matrix("datingTestSet2.txt")
	normmat,ranges,minvalues=autonorm(datingdatamat)
	m=normmat.shape[0]
	numtestvecs=int(m*horatio)
	errorcount = 0
	for i in range(numtestvecs):
		classifieresult=classify0(normmat[i,:],normmat[numtestvecs:m,:],datinglabels[numtestvecs:m],3)
		#print("the classify0 came back with :%d,the real answer is :%d" %(classifieresult,datinglabels[i]))
		if classifieresult!=datinglabels[i]:
			errorcount+=1
			pass
	print("the total error rate is %f" %(errorcount/float(numtestvecs)))	
	pass
def image2vector(filename):
	returnvec=numpy.zeros((1,1024))
	files=open(filename)
	for i in range(32):
		lines=files.readline()
		#read a sigle line from files
		for j in range(32):
			returnvec[0,32*i+j]=int(lines[j])
	return returnvec
	pass
def handwritingclasstest():
	hwlabels=[]
	trainingfilelist=listdir("trainingDigits")
	m=len(trainingfilelist)
	trainmat=numpy.zeros((m,1024))
	for i in range(m):
		filename=trainingfilelist[i]
		classnumber=int(filename.split('_')[0])
		hwlabels.append(classnumber)
		trainmat[i,:]=image2vector("trainingDigits/%s" % filename)
	testfilelsit=listdir("testDigits")
	errorcount=0
	n=len(testfilelsit)
	for i in range(n):
		testfilename=testfilelsit[i]
		classnumber=int(testfilename.split('_')[0])
		vectorundertest=image2vector("testDigits/%s" %testfilename)
		classifieresult=classify0(vectorundertest,trainmat,hwlabels,3)
		if classifieresult!=classnumber:
			errorcount+=1.0
			pass
	print("the total error rate is :%f" %(errorcount/float(n)))
	pass
if __name__ == '__main__':
	#
	#a,b=createDataset()
	#c=clssify0([1,0.5],a,b,3)
	#print(c)
	datamat,datalab=file2matrix("datingTestSet2.txt")
	datamat,ranges,minvalues=autonorm(datamat)
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(datamat[:,0],datamat[:,1],50,15.0*numpy.array(datalab))
	plt.show()
	testclassfiy0()
	handwritingclasstest()
	#print(datalab)
