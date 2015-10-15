# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:18:43 2015

@author: DFW
"""
import pandas as pd
import numpy as np
import os
###
Gid2Taxid = {}
Taxid2Gid = {}
for line in open('../Result0923/Gid2Taxid.txt'):
    line = line.strip().split('\t')
    Gid2Taxid[line[0]] = line[1]
    Taxid2Gid[line[1]] = Taxid2Gid.get(line[1], set())
    Taxid2Gid[line[1]].add(line[0])
print len(Gid2Taxid), len(Taxid2Gid)
###
Gid2Type = {}
for line in open('../Result0923/Gid2Type.txt'):
    line = line.strip().split('\t')
    Gid2Type[line[0]] = line[1]
print len(Gid2Type)

###
barcodeTypes = ['ITS', 'rbcL', 'matK', 'trnL-trnF', 'psbA-trnH',
                'trnL', 'ITS2', 'ndhF', 'trnH-psbA', 'rpoC1']
###
genuspath = '../Result0923/Sepcies/'
genusfiles = os.listdir(genuspath)
#print genusfiles
##
print genusfiles[0]
genus = pd.read_excel(genuspath+genusfiles[0], 0, header=0)
print genus
SpeciesCount = {} ### {type => set(taxid)}
SeqCount = {} ### {taxid => {type => set(gid)}}
for i in genus.index:
    Taxid = str(genus.loc[i, 'ID'])
    print i, Taxid, len(Taxid2Gid.get(Taxid, set()))
    SeqCount[Taxid] = {}
    for gid in Taxid2Gid.get(Taxid, set()):
        SeqCount[Taxid][Gid2Type[gid]] = SeqCount[Taxid].get(Gid2Type[gid], set())
        SeqCount[Taxid][Gid2Type[gid]].add(gid)
        SpeciesCount[Gid2Type[gid]] = SpeciesCount.get(Gid2Type[gid], set())
        SpeciesCount[Gid2Type[gid]].add(Taxid)
        if Gid2Type[gid] in barcodeTypes:
            print '', gid, Gid2Type[gid]

print SeqCount
print SpeciesCount
###


































