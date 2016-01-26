#!/usr/bin/python3
import numpy,operator
def createDataset():
	group=numpy.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=['A','A','B','B']
	return group,labels
def clssify0(inx,dataset,labels,k):
	datasize=dataset.shape[0]
	diffmat=tile(inx,(datasize,1))-dataset
	sqdiffmat=diffmat*2
	sqdistances=sqdiffmat.sum(axis=1)
	distances=sqdistances**0.5
	
	pass