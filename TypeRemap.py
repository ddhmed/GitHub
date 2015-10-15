# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:46:57 2015

@author: DFW
"""
#import pandas as pd
#import re
#'''
#pattern: 
#trnL,trnF
#trnL-trnF
#trnT-trnL,trnL,trnL-trnF
#trnL, trnL-trnF, and trnF
#trnL and trnL-trnF
#=> trnL
#'''
#def barcodesplit(barcode):
#    #print barcode, '\n'
#    barcode = barcode.strip()
#    seps = [',', 'and', ',']
#    barcode = barcode.replace('partial ', 'partial-')
#    p = re.compile(r',[\w -/]*?\(([\w-]+?)\)[\w -]*?and')
#    barcode =  p.sub(r', \1 ,', barcode)
#    p = re.compile(r'^[\w -/]*?\(([\w-]+?)\)[\w -]*?and')
#    barcode =  p.sub(r', \1 ,', barcode)
#    #print barcode, '\n'
#    p = re.compile(r',[\w -/]*?\(([\w-]+?)\)[\w -]*?,')
#    barcode =  p.sub(r', \1 ,', barcode)
#    p = re.compile(r'^[\w -/]*?\(([\w-]+?)\)[\w -]*?,')
#    barcode =  p.sub(r', \1 ,', barcode)
#    p = re.compile(r'and [\w -/]*?\(([\w-]+?)\)[\w -]*?,')
#    barcode =  p.sub(r', \1 ,', barcode)
#    
#    p = re.compile(r'and [\w -/]*?\(([\w-]+?)\)[\w -]*?$')
#    barcode =  p.sub(r', \1 ,', barcode)
#    p = re.compile(r',[\w -/]*?\(([\w-]+?)\)[\w -]*?$')
#    barcode =  p.sub(r', \1 ,', barcode)
#    p = re.compile(r'^[\w -/]*?\(([\w-]+?)\)[\w -]*?$')
#    barcode =  p.sub(r', \1 ,', barcode)
#    #print barcode, '\n'
#    p = re.compile(r' ?- ?')
#    barcode =  p.sub(r'-', barcode)
#    #print barcode, '\n'
#    p = re.compile(r'and ([\w-]+)[\w -]*?, partial-sequence[^ \w]')
#    barcode =  p.sub(r', partial-\1,', barcode)
#    p = re.compile(r', ?([\w-]+)[\w -]*?, partial-sequence[^ \w]')
#    barcode =  p.sub(r', partial-\1,', barcode)
#    p = re.compile(r'and ([\w-]+)[\w -]*?, partial-sequence$')
#    barcode =  p.sub(r', partial-\1,', barcode)
#    p = re.compile(r', ?([\w-]+)[\w -]*?, partial-sequence$')
#    barcode =  p.sub(r', partial-\1,', barcode)
#    p = re.compile(r', *partial-sequence *([\w-]+) *,')
#    barcode =  p.sub(r', partial-\1,', barcode)
#    #print barcode, '\n'
#    barcodes = [barcode]
#    for s in seps:
#        barcodes_new = set()
#        for i in barcodes:
#            barcodes_new.update([maprole(j.strip()) for j in i.split(s)])
#        barcodes = barcodes_new
#    if '' in barcodes:
#        barcodes.remove('')
#    return barcodes
#
#def maprole(barcode):
#    match = re.search(r'chloroplast (partial-\w*?) gene', barcode)
#    if match:
#        return match.group(1)
#    match = re.search(r'chloroplast ([\w-]*?) gene for', barcode)
#    if match:
#        return match.group(1)
#    if 'photosystem II protein D1 (psbA) gene' in barcode:
#        return 'psbA'
#    barcode = barcode.replace('between', '').replace('region', '').replace(' for ', ' ').replace('pseudogene', '').replace('genes', '').replace('gene', '').replace('protein', '').replace('intergenic spacer', '').strip()
#    if barcode in 'ribulose-1,5-bisphosphate carboxylase/oxygenase large subunit':
#        return 'rbcL'
#    if 'ribulose-1' in barcode or '5-bisphosphate carboxylase' in barcode:
#        return 'rbcL'
#    if 'maturase K' in barcode and 'matK' in barcode:
#        return 'matK'
#    if barcode.upper()=='MATK' or barcode.upper()=='MARK_LIKE':
#        return 'matK'
#    if barcode == 'PsaA-like':
#        return 'PsaA'
#    if barcode == 'maturase K' or barcode=='maturase K-like' or barcode=='maturase':
#        return 'matK'
#    if len(barcode)==4 and 'ITS' in barcode.upper():
#        return barcode.upper()
#    if 'ITS'==barcode.upper():
#        return barcode.upper()
#    if len(barcode)in [5, 6, 7]:
#        if '('==barcode[0] and barcode[-1] == ')':
#            return barcode[1:-1]
#        if barcode[-1] == ')':
#            return barcode[0:-1]
#        if barcode[0] == '(':
#            return barcode[1:]
#        return barcode[1:]
#    return barcode
#
#typemap = pd.read_excel(u'../20151009补充/BarcodeSequenceCount-Jin.xlsx', 0, header=0, index_col=0)
##print typemap.index
#mapdic = {}
##print barcodesplit('tRNA-His (trnH) gene, partial sequence, trnH-psbA intergenic spacer, complete sequence, and PsbA (psbA) gene, partial sequence  trnH ,gene psbA ,gene, partial-sequence')
#codes = set()
#for i in range(len(typemap.index)):
#    mapt = str(typemap.iloc[i, 0]).strip()
#    i = str(typemap.index[i]).strip()
#    if mapt == 'nan':
#        mapt = i
#    mapt = mapt.replace(u'，', ',').replace(u'；', ',').replace(u';', ',')
#    #print barcodesplit(mapt),mapt
#    codes.update(barcodesplit(mapt))
#    mapdic[i] = barcodesplit(mapt)
##print '##########################'
##codes = sorted(codes)
##for i in codes:
##    print i
#
#def split2(barcodes):
#    seps = [',', 'and', '-']
#    for s in seps:
#        barcodes_new = set()
#        for i in barcodes:
#            i = i.replace('partial-', 'partial=')
#            barcodes_new.update([j.strip() for j in i.split(s)])
#        barcodes = barcodes_new
#    if '' in barcodes:
#        barcodes.remove('')
#    barcodes_new = set()
#    for i in barcodes:
#        barcodes_new.add(i.replace('partial=', 'partial-'))
#    return barcodes_new
#
#f = open('../Result0923/Gid2Type_remap2.txt', 'w')
#for line in open('../Result0923/Gid2Type.txt'):
#    line = line.strip().split('\t')
#    if ',' in line[1]:
#        map2 = [maprole(i) for i in line[1].split(',')]
#    else:
#        map2 = [maprole(line[1].strip())]
#    mapc = mapdic.get(line[1].strip(), map2)
#    mapc = split2(mapc)
#    f.write(line[0]+'\t'+'&'.join(mapc)+'\n')
#f.close()
#print 'Done!'

data = []
for line in open('../Result0923/Gid2Type_remap2.txt'):
    data.extend(line.strip().split('\t')[1].split('&'))
data = [(i, data.count(i)) for i in set(data)]
print len(data)
Count = sorted(data, key=lambda x:x[1], reverse=True)

f = open('../Result0923/BarcodeSequenceCount_remap2.txt', 'w')
for i in Count:
    f.write(i[0]+'\t'+str(i[1])+'\n')
f.close()

result = Count[0:20]
result.append(('other_'+str(len(Count)-15), sum([i[1] for i in Count[15:]])))
print result
import matplotlib.pyplot as plt
x = [i[0] for i in result]
y = [i[1] for i in result]
plt.bar(range(len(x)), y, width=0.6, color='lime')
plt.xticks([i+0.3 for i in range(len(x))], x, rotation=-90, fontsize=13)
for i in range(len(y)):
    plt.annotate(str(y[i]), (range(len(x))[i]+0.05*(5-len(str(y[i]))), y[i]+200))
plt.xlim([0,21])
plt.show()









