import csv
import numpy as np
import scipy
import scipy.cluster


reader = csv.reader(open("red_data2.csv","rb"),delimiter=",")
x = list(reader)
result = np.array(x).astype('float')
np.shape(result)
dude = scipy.cluster.vq.kmeans(result,10)
print dude




