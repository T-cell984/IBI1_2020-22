import numpy as np
a=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
#a describes gene lengths
b=np.array([51,1142,42,216,25,650,32533,57,1,523])
#b is the number of exons in each gene
c=a/b
#c is the average exon length across all 10 genes
c=sorted(c)
c.sort()
print(c)

import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(c)
plt.show()
#get the boxplot that shows the distribution of average exon length
