# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:54:36 2015

@author: DFW
"""
Gids = []
Name = {}
Count = {}
for line in open('../Result0923/Gid2Type.txt'):
    line = line.strip().split('\t')
    Type = line[1].strip()
    Name[Type.upper()] = Name.get(Type.upper(), Type)
    Count[Name[Type.upper()]] = Count.get(Name[Type.upper()], 0) + 1
    Gids.append((line[0].strip(), Name[Type.upper()]))

Count = sorted(Count.items(), key=lambda x:x[1], reverse=True)
#f = open('../Result0923/BarcodeSequenceCount.txt', 'w')
#for i in Count:
#    f.write(i[0]+'\t'+str(i[1])+'\n')
#f.close()

result = Count[0:15]
result.append(('other_'+str(len(Count)-15), sum([i[1] for i in Count[15:]])))
print result
import matplotlib.pyplot as plt
x = [i[0] for i in result]
y = [i[1] for i in result]
plt.bar(range(len(x)), y, width=0.6, color='lime')
plt.xticks([i+0.3 for i in range(len(x))], x, rotation=-90, fontsize=13)
for i in range(len(y)):
    plt.annotate(str(y[i]), (range(len(x))[i]+0.05*(5-len(str(y[i]))), y[i]+200))
plt.show()







