# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:47:19 2015

@author: DFW
"""
import os
import re
import pandas as pd
import numpy as np
ID2Gid = {}
AllIDs = set()

####### read all GI id
path = u'../Data/seq/核糖体序列/'
fs = os.listdir(path)
for f in fs:
    if '.txt' not in f:
        continue
    text = ''.join(open(path+f, 'r').readlines())
    GIs = re.findall(r'>gi\|(\d+)\|[\w\W]+?\|([\w\W]+?)\|', text)
    for Gid, ID in GIs:
        AllIDs.add(Gid.strip())
        AllIDs.add(ID.strip().split('.')[0].strip())
        ID2Gid[ID.strip().split('.')[0].strip()] = Gid.strip()
    
path = u'../Data/seq/叶绿体/'
fs = os.listdir(path)
for f in fs:
    if '.txt' not in f:
        continue
    text = ''.join(open(path+f, 'r').readlines())
    GIs = re.findall(r'>gi\|(\d+)\|[\w\W]+?\|([\w\W]+?)\|', text)
    for Gid, ID in GIs:
        AllIDs.add(Gid.strip())
        AllIDs.add(ID.strip().split('.')[0].strip())
        ID2Gid[ID.strip().split('.')[0].strip()] = Gid.strip()

path = u'../Data/seq/叶绿体/不是目录中的属/'
fs = os.listdir(path)
for f in fs:
    if '.txt' not in f:
        continue
    text = ''.join(open(path+f, 'r').readlines())
    GIs = re.findall(r'>gi\|(\d+)\|[\w\W]+?\|([\w\W]+?)\|', text)
    for Gid, ID in GIs:
        AllIDs.add(Gid.strip())
        AllIDs.add(ID.strip().split('.')[0].strip())
        ID2Gid[ID.strip().split('.')[0].strip()] = Gid.strip()


print len(ID2Gid)
print len(AllIDs)
#'165971911'
#print ID2Gid.values().index('165971911')


NoMatchIDs = set()
NoMatchindexs = []
ID2Type = {}
Types = pd.read_excel('../Data/Types.xlsx', 0, header=None)
for i in Types.index:
    Type = str(Types.loc[i, 1]).strip()
    RawID = str(Types.loc[i, 3]).strip()
    #Name = str(Types.loc[i, 2]).strip()
    ID = RawID
    #print i, str(RawID)
    if RawID[0] == '|':
        RawID = RawID[1:]
    if '|' in ID:
        ID = RawID.split('|')[1].strip()
    ID = ID.split('.')[0].strip()
    search = re.search(r'([\w\W][\w\W][\w\W]\d+)', ID)
    if search:
        ID = search.group(1)
    if ID in ID2Gid.keys():
        ID2Type[ID2Gid[ID]] = Type
    elif ID in ID2Gid.values():
        ID2Type[ID] = Type
    else:
        #print i, ID
        NoMatchindexs.append(i)
        NoMatchIDs.add(ID)
print len(ID2Type), len(NoMatchIDs)

Types = pd.read_excel(u'../20151009补充/NoMatchTerms 10.8补充.xls', 0, header=None, index_col=0)
NoMatchindexs_new = []
for i in NoMatchindexs:
    Type = str(Types.loc[i, 2]).strip()
    RawID = str(Types.loc[i, 5]).strip()
    #Name = str(Types.loc[i, 2]).strip()
    ID = RawID
    #print i, str(RawID)
    if RawID[0] == '|':
        RawID = RawID[1:]
    if '|' in ID:
        ID = RawID.split('|')[1].strip()
    ID = ID.split('.')[0].strip()
    search = re.search(r'([\w\W][\w\W][\w\W]\d+)', ID)
    if search:
        ID = search.group(1)
    print '###############'
    print Type, ID
    if ID in ID2Gid.keys():
        if ID2Type.has_key(ID2Gid[ID]):
            print 'Has ID...'
        ID2Type[ID2Gid[ID]] = Type
    elif ID in ID2Gid.values():
        if ID2Type.has_key(ID):
            print 'Has ID...'
        ID2Type[ID] = Type
    else:
        print i, ID
        NoMatchindexs_new.append(i)
        NoMatchIDs.add(ID)

print len(ID2Type), len(NoMatchIDs)
NoMatchData = Types.loc[NoMatchindexs_new, :]
NoMatchData.to_excel('../Result0923/NoMatchTerms_turn2.xls')

f = open('../Result0923/Gid2Type_turn2.txt', 'w')
for Gid, Type in ID2Type.items():
    f.write(Gid+'\t'+Type+'\n')
f.close()

print 'Done!'












