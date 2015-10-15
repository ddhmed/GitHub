# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:25:20 2015

@author: DFW
"""
import pandas as pd
import numpy as np
import TreeClass as tc
TaxonTerm = tc.TaxonTerm

### name
ID2Name = {}
for line in open('../Data/names.dmp'):
    line = [i.strip() for i in line.split('|')]
    if not ID2Name.has_key(line[0]):
        ID2Name[line[0]] = line[1]
### Tree
TTree = {}
for line in open('../Data/nodes.dmp'):
    line = [i.strip() for i in line.split('|')][0:3]
    Node = TaxonTerm(line[0], '', line[2])
    Node.Parent = line[1]
    Node.Childs = set()
    Node.seqs = []
    TTree[line[0]] = Node
for ID, Node in TTree.items():
    Node.Parent = TTree[Node.Parent]
    Node.Parent.Childs.add(Node)
#print len(TTree)

### genus Data
Data = pd.read_excel('../Data/ZYName.xlsx', 0, index_col = 0)
for i in Data.index:
    print i, Data.loc[i, 'Name']
    IDs = set()
    IDs = tc.getAllNodeofGenus(TTree[str(Data.loc[i, 'Tid'])], IDs)
    out = []
    for ID in IDs:
        out.append([ID, ID2Name[ID], TTree[ID].Rank])
    #print out
    out = pd.DataFrame(np.array(out), columns=['ID', 'Name', 'Rank'])
    out.to_excel('../Result0923/Sepcies/'+str(i)+'_'+str(Data.loc[i, 'Tid'])+'_'+str(Data.loc[i, 'TName'])+'.xls')

print 'Done!'


























