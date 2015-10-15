# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:51:57 2015

@author: DFW
"""
import os
import re

NuclearID = set()
PlastidID = set()
####### read all GI id
path = u'../Data/seq/核糖体序列/'
fs = os.listdir(path)
for f in fs:
    if '.txt' not in f:
        continue
    text = ''.join(open(path+f, 'r').readlines())
    GIs = re.findall(r'>gi\|(\d+)\|', text)
    NuclearID.update(GIs)

path = u'../Data/seq/叶绿体/'
fs = os.listdir(path)
for f in fs:
    if '.txt' not in f:
        continue
    text = ''.join(open(path+f, 'r').readlines())
    GIs = re.findall(r'>gi\|(\d+)\|', text)
    PlastidID.update(GIs)

print len(NuclearID)
print len(PlastidID)

AllID = NuclearID | PlastidID
print len(AllID), len(NuclearID)+len(PlastidID)

### GI 2 TaxID
#IDMapping = {}
#
#f = open('../../gi_taxid_nucl/gi_taxid_nucl.dmp', 'r')
#line = f.readline()
#i = 0
#while(line):
#    i += 1
#    if i == 10:
#        pass
#    line = line.strip().split('\t')
#    NID = line[0]
#    TaxID = line[1]
#    if NID in AllID:
#        IDMapping[NID] = TaxID
#    #print NID, TaxID
#    line = f.readline()
#f.close()
#
#print len(IDMapping)


f = open('../../gi_taxid_nucl/gi_taxid_nucl.dmp', 'r')
line = f.readline()
i = 0
while(line):
    i += 1
    line = f.readline()
f.close()
print i






