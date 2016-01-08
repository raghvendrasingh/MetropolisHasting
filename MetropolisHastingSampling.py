import numpy as np
import math
import matplotlib.pyplot as plt

def plotSamples1(samples):
	x = []
	y = []
	for i in xrange(0,len(samples)):
	    x.append(samples[i][0])
	    y.append(samples[i][1])
	n = list(xrange(len(samples))) 
	fig, ax = plt.subplots()   
	ax.scatter(x,y,s=0.2)
	ax.axis('equal')
	for i, txt in enumerate(n):
		ax.annotate(txt,(x[i],y[i]))
	plt.show()

def plotSamples(samples):
	x = []
	y = []
	for i in xrange(0,len(samples)):
	    x.append(samples[i][0])
	    y.append(samples[i][1])
	plt.scatter(x,y,s=0.1)
	plt.axis('equal')
	plt.show()	


def targetFunction(x):
    a = math.exp(-5*abs(x[0]*x[0]+x[1]*x[1]-1))
    return a

def getSamples(target, N, x, cov, burnin=0):
       samples = [x]
       for i in xrange(2,burnin+N):
          proposalSampleTemp = np.random.multivariate_normal(x, cov, 1)
          proposalSample = []
          for sample in proposalSampleTemp:
       	    for j in xrange(0,sample.size):
               proposalSample.append(sample[j]) 
          
          randomNumber = np.random.rand(1,1)[0][0]
          if randomNumber <= min(1, target(proposalSample)/target(x)):
       	     x = proposalSample
          samples.append(x)
       
       return samples[(burnin+1):(N+burnin)]   	  



mean = [0,0]
cov = [[.01, 0], [0, .01]]

samples = getSamples(targetFunction, 20000, mean, cov,10000)

plotSamples(samples)
