import iofile, numpy as np, pickle
from sklearn import svm
# import matplotlib.pyplot as plt

def processingData(mode='train'):
	mentah = iofile.readPickle('browsing-session-'+mode+'-pickle.txt')
	data = []
	target = []
	i = 0
	for line in mentah:
		i += 1
		obj = [line['details'], line['duration'], line['page_per_time']]
		c = 1 if line['class'] == 'buy' else 0
		target.append(c)
		data.append(obj)
	return data, target


data, target = processingData()
X = np.array(data)
y = np.array(target)

print X.shape
svc = svm.SVC(kernel='linear', C=0.1).fit(X,y)
svc = iofile.readPickle('svc-pickle.pkl')
print "save done"
# Z = svc.predict(X)
# print y
# print Z
# print "Number of mislabeled points : %d" % (y != Z).sum()
# print svc
# print Z