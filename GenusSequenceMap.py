# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:35:19 2015

@author: DFW
"""
import pandas as pd
import numpy as np
import os

def getT2Gmap(path = '../Result0923/Gid2Taxid.txt'):
    Taxid2G = {}
    for line in open(path):
        line = line.strip().split('\t')
        Taxid2G[line[1]] = Taxid2G.get(line[1], set())
        Taxid2G[line[1]].add(line[0])
    print 'Taxid:', len(Taxid2G)
    return Taxid2G

def genusSeqMap(path, Taxid2G, opath):
    print path
    data = pd.read_excel(path,0 ,header=0, index_col=0)
    Seq = ['&'.join(Taxid2G.get(str(ID), [''])) for ID in data['ID']]
    data['Seq'] = Seq
    data.to_excel(opath+path.split('/')[-1])

def rawSeqMap(Taxid2G, path):
    files = os.listdir(path)
    for f in files:
        genusSeqMap(path+f, Taxid2G, opath = '../Result0923/Gid/')

def getType2Gid(path='../Result0923/Gid2Type_remap2.txt', cutoff=15):
    Type2G = {}
    for line in open(path):
        line = line.strip().split('\t')
        for Type in line[1].split('&'):
            Type2G[Type] = Type2G.get(Type, set())
            Type2G[Type].add(line[0])
    Type = sorted(Type2G.items(), key=lambda x:len(x[1]), reverse = True)
    print ' || '.join([i[0]+', '+str(len(i[1])) for i in Type[0:cutoff]])
    AllSeq = set()
    tops = []
    for t, s in Type[:cutoff]:
        AllSeq.update(s)
        tops.append((t, s))
    print 'Type:',len(Type2G), 'Top Seq:',len(AllSeq)
    return Type, AllSeq, tops

def genustopSeqMap(path, Taxid2G, tops, opath):
    print path
    result = {}
    data = pd.read_excel(path,0 ,header=0, index_col=0)
    for top in range(len(tops)):
        name = tops[top][0]
        Seq = ['&'.join([i for i in Taxid2G.get(str(ID), []) if i in tops[top][1]]) for ID in data['ID']]
        count = [len([i for i in Taxid2G.get(str(ID), []) if i in tops[top][1]]) for ID in data['ID']]
        data[name] = Seq
        data[name+'_count'] = count
        result[name] = [len(count), len(count)-count.count(0), min(count), max(count), sum(count)/float(len(count)), sum(count)/float(len(count)-count.count(0)) if len(count)-count.count(0)!=0 else 0, sum(np.array(count)>=2)]
    data.to_excel(opath+path.split('/')[-1])
    return result
    

def topSeqMap(Taxid2G, path, tops):
    files = os.listdir(path)
    result = []
    names = [i[0] for i in tops]
    for f in files:
        count = genustopSeqMap(path+f, Taxid2G, tops, opath = '../Result0923/topSeq/')
        row = [count.values()[0][0]]
        for name in names:
            row.append(count[name][1])
            row.append(round(count[name][5], 1))
            row.append(count[name][6])
        result.append(row)
    tnames = ['Species']
    for i in names:
        tnames.append(i+'_SNum')
        tnames.append(i+'_Avg')
        tnames.append(i+'_MT2')
    index = [i.split('.xls')[0] for i in files]
    result = pd.DataFrame(np.array(result), index=index, columns=tnames)
    return result

if __name__ == '__main__':
    print 'main...'
    Taxid2G = getT2Gmap()
    path = '../Result0923/Sepcies/'
    #rawSeqMap(Taxid2G, path)
    Types, topseqs, tops = getType2Gid(cutoff=7)
    #print Types[0]
    result = topSeqMap(Taxid2G, path, tops)
    print result
    result.to_excel('../Result0923/genusBarcodeCount.xls')
    




















