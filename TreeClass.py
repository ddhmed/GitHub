# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 18:50:50 2015

@author: DFW
"""
import random as rd
import pandas as pd
import re
class TaxonTerm:
    ID = None
    Name = None
    Rank = None
    Parent = None
    Childs = set()
    seqs = []
    def __init__(self, ID, Name, Rank):
        self.ID = ID
        self.Name = Name
        self.Rank = Rank
    def checkID(self, ID):
        if self.ID == ID:
            return True
        else:
            return False
    def checkName(self, Name):
        if self.Name == Name:
            return True
        else:
            return False
    def checkRank(self, Rank):
        if self.Rank == Rank:
            return True
        else:
            return False
    def getMessage(self):
        return self.ID+'|'+self.Name+'|'+self.Rank
    def getChildCount(self):
        return len(self.Childs)
    def getBorthers(self):
        if self.Name != 'ROOT':
            return self.Parent.Childs
        else:
            return None
    def getBorthersCount(self):
        if self.Name != 'ROOT':
            return len(self.Parent.Childs)
        else:
            return 0
def ToxRanks():
    ### 界   门   纲   目   科   '族'  属   种
    qzs = ['super', '', 'sub', 'infra']
    RankTerms = ['kingdom', 'phylum', 'class', 'order', 'family', 'tribe', 'genus','species']
    ranks = []
    for rt in RankTerms:
        for qz in qzs:
            ranks.append(qz+rt)
    return ranks

def printTree(Root, sep = '-', rank = 'species'):
    if Root.Rank in rank.split('|'):
        print sep+Root.getMessage()
        return True
    print sep+Root.getMessage()
    for Node in Root.Childs:
        printTree(Node, sep+'-', rank)

def printTree2(Root, sep = '-'):
    if len(Root.Childs) == 0:
        print sep+Root.getMessage()
        return True
    print sep+Root.getMessage()
    for Node in Root.Childs:
        printTree2(Node, sep+'-')

def printTreeMin(Root, sep = '-', rank = 'species'):
    Ranks = ToxRanks()
    Ranks = Ranks[:Ranks.index(rank)+1]
    if Root.Rank in Ranks:
        print sep+Root.getMessage()
        sep += '-'
    if Root.Rank == rank:
        return True
    for Node in Root.Childs:
        printTreeMin(Node, sep, rank)

def defineColors():
    #50 colors
    colors = []
    colors.append('#ff7f7f')
    colors.append('#ff7fbf')
    colors.append('#ff7fff')
    colors.append('#bf7fff')
    colors.append('#7f7fff')
    colors.append('#7fbfff')
    colors.append('#7fffff')
    colors.append('#7fffbf')
    colors.append('#7fff7f')
    colors.append('#bfff7f')
    colors.append('#ffff7f')
    colors.append('#ffbf7f')
    colors.append('#ffa8a8')
    colors.append('#ffa8d3')
    colors.append('#ffa8ff')
    colors.append('#d3a8ff')
    colors.append('#a8a8ff')
    colors.append('#a8d3ff')
    colors.append('#a8ffff')
    colors.append('#a8ffd3')
    colors.append('#a8ffa8')
    colors.append('#d3ffa8')
    colors.append('#ffffa8')
    colors.append('#ffd3a8')
    colors.append('#ffe5e5')
    colors.append('#ffe5f2')
    colors.append('#ffe5ff')
    colors.append('#f4eaff')
    colors.append('#eaeaff')
    colors.append('#eaf4ff')
    colors.append('#eaffff')
    colors.append('#eafff4')
    colors.append('#eaffea')
    colors.append('#f4ffea')
    colors.append('#ffffea')
    colors.append('#fff4ea')
    colors.append('#ffbcbc')
    colors.append('#ffbcdd')
    colors.append('#ffbcff')
    colors.append('#ddbcff')
    colors.append('#bcbcff')
    colors.append('#bcddff')
    colors.append('#bcffff')
    colors.append('#bcffdd')
    colors.append('#bcffbc')
    colors.append('#ddffbc')
    colors.append('#ffffbc')
    colors.append('#ffddbc')
    colors.append('#ff9393')
    colors.append('#ff93c9')
    return colors

def getTree(Root, rank = 'genus'):
    if Root.Rank == rank:
        return Root.ID
    else:
        cids = [getTree(child, rank) for child in Root.Childs]
        if len(cids) != 0:
            return '('+','.join(cids)+')'+Root.ID
        else:
            return Root.ID

def getTreeMin(Root, rank = 'genus'):
    Ranks = ToxRanks()
    NRanks = Ranks[Ranks.index(rank)+1:]
    #print NRanks
    if Root.Rank in NRanks:
        return ''
    else:
        cids = [getTreeMin(child, rank) for child in Root.Childs]
        cids = [i for i in cids if i != '']
        if len(cids) != 0:
            if Root.Rank == 'no rank':
                return ','.join(cids)
            return '('+','.join(cids)+')'+Root.ID
        else:
            if Root.Rank == 'no rank':
                return ''
            return Root.ID

def getNodesByRank(Nodes, rank = 'class'):
    IDs = []
    for node in Nodes.values():
        if node.Rank in rank.split('|'):
            IDs.append(node.ID)
    return IDs
def getNodesByRanks(Root, nodes = set(), ranks = 'class'):
    if Root.Rank in ranks.split('|'):
        nodes.add(Root.ID)
        return nodes
    for child in Root.Childs:
        nodes.update(getNodesByRanks(child, nodes, ranks))
    return nodes


def getLeafs(Node):
    if len(Node.Childs) == 0:
        return [Node.ID]
    IDs = []
    for child in Node.Childs:
        IDs.extend(getLeafs(child))
    return IDs

def getSpecies(Node):
    if Node.Rank == 'species':
        return [Node.ID]
    IDs = []
    for child in Node.Childs:
        IDs.extend(getSpecies(child))
    return IDs

def getAllNodeofGenus(Node, IDs):
    if Node.Rank in ['forma', 'varietas', 'subspecies', 'species']:
        IDs.add(Node.ID)
    if len(Node.Childs) == 0:
        return IDs
    for child in Node.Childs:
        IDs.update(getAllNodeofGenus(child, IDs))
    return IDs

#def getColorFile(Nodes, RootID, treeleafs, cutoff, path, colorranks = 'class|subclass', colortype= 'range'):
#    IDs = getNodesByRanks(Nodes[RootID], nodes = set(), ranks = colorranks)
#    IDs = list(IDs)
#    print len(IDs)
#    #IDs = getNodesByRank(Nodes, rank = colorrank)
#    Data = {}
#    colors = defineColors()
#    colori = 0
#    f = open(path, 'w')
#    for i in range(len(IDs)):
#        ClassID = IDs[i]
#        color = colors[colori]
#        nodes0 = getLeafs(Nodes[ClassID], leafs = set())
#        nodes = [j for j in nodes0 if j in treeleafs]
#        print ClassID, Nodes[ClassID].Name, len(nodes0), len(nodes)
#        if len(nodes) >= cutoff:
#            Data[IDs[i]] = (color, nodes)
#            colori += 1
#            for node in nodes:
#                f.write(node+'\t'+colortype+'\t'+color+'\t'+Nodes[ClassID].Name.replace(' ', '_')+'\n')
#    print len(Data)
#    f.close()
#    return True

def getColorFile(Tree, RootID, newick, path, cutoff, colorranks = 'class|subclass', colortype= 'range'):
    #IDs = ['3041', '35493']
    IDs = getNodesByRanks(Tree[RootID], nodes = set(), ranks = colorranks)
    newickIDs = re.findall(r'\d+', newick)
    colors = defineColors()[0:len(IDs)]
    colors = rd.sample(colors, len(colors))
    colori = 0
    f = open(path, 'w')
    for ID in IDs:
        if ID not in newickIDs:
            continue
        try:
            loc = newick.index(')'+ID+',')
        except:
            try:
                loc = newick.index(')'+ID+')')
            except:
                continue
        i = loc-1
        left = 0
        right = 1
        while(left != right):
            if newick[i] == '(':
                left += 1
            if newick[i] == ')':
                right += 1
            i = i-1
        color = colors[colori]
        nodes = re.findall(r'(\d+)', newick[i+1 : loc])
        noleafs = re.findall(r'\)(\d+)[,\)]', newick[i+1 : loc])
        leafs = set(nodes) - set(noleafs)
        if len(leafs) >= cutoff:
            colori += 1
            for node in leafs:
                f.write(node+'\t'+colortype+'\t'+color+'\t'+Tree[ID].ID+'\n')
        print ID, loc, len(leafs)
    f.close()
    return True

def getNuclearCount(Nodes):
    Counts = {}
    for node in Nodes.values():
        if len(node.seqs) != 0:
            Counts[node.ID] = len(node.seqs)
    return Counts

def getSubTree(Tree, RootID, Nodes):
    Nodes = getNuclearCount(Nodes)
    subTree = {}
    c = 0
    for ID in Nodes.keys():
        print len(Nodes), c
        c += 1
        if ID not in Tree.keys():
            print '###############', ID
            continue
        Node = Tree[ID]
        subTree[ID] = TaxonTerm(Node.ID, Node.Name, Node.Rank)
        subTree[ID].Childs = set()
        subTree[ID].seqs = [Nodes[ID]]
        Node = Node.Parent
        newNode = subTree[ID]
        while(Node.ID != RootID and Node.ID != '1'):
            #print len(Nodes), c, Node.ID, Node.Rank
            if not subTree.has_key(Node.ID):
                subTree[Node.ID] = TaxonTerm(Node.ID, Node.Name, Node.Rank)
                subTree[Node.ID].Childs = set()
                subTree[Node.ID].seqs = [0]
            subTree[Node.ID].Childs.add(newNode)
            newNode.Parent = subTree[Node.ID]
            
            newNode = subTree[Node.ID]
            Node = Node.Parent
    return subTree

def getDataFile(Tree, path, rank = 'genus'):
    f = open(path, 'w')
    IDs = getNodesByRank(Tree, rank = rank)
    for ID in IDs:
        #print ID
        nodes = getLeafs(Tree[ID])
        #print nodes
        count = 0
        for node in nodes:
            count += Tree[node].seqs[0]
        f.write(ID+','+str(count)+'\n')
    f.close()
    return True

def getDataFileOfSeq(Tree, subTree, path, rank = 'genus'):
    f = open(path, 'w')
    f.write('LABELS,seq_species,noseq_species\n')
    f.write('COLORS,#ff0000,#00ff00\n')
    IDs = getNodesByRank(subTree, rank = rank)
    for ID in IDs:
        #print ID
        nodes = getSpecies(subTree[ID])
        AllSpecies = getSpecies(Tree[ID])
        #print nodes
        f.write(ID+','+str(len(nodes))+','+str(len(AllSpecies)-len(nodes))+'\n')
    f.close()
    return True

def getDataFileOfHerb(Tree, path, rank = 'genus'):
    data = pd.read_excel('../Data/Book_All Species.xls', 0, index_col = 0, head = True)
    herbs = [str(int(i)) for i in list(data.ID) if str(i).upper()!='NAN']
    f = open(path, 'w')
    IDs = getNodesByRank(Tree, rank = rank)
    for ID in IDs:
        nodes = getLeafs(Tree[ID])
        #print ID, Tree[ID].Name
        #print nodes
        if len(set(herbs)&set(nodes)) != 0 and len(nodes) != 0:
            f.write(ID+','+str(len(set(herbs)&set(nodes)))+'\n')
    f.close()
    return True
def getDataFileOfHerbPercent(Tree, path, rank = 'genus'):
    data = pd.read_excel('../Data/Book_All Species.xls', 0, index_col = 0, head = True)
    herbs = [str(int(i)) for i in list(data.ID) if str(i).upper()!='NAN']
    f = open(path, 'w')
    IDs = getNodesByRank(Tree, rank = rank)
    for ID in IDs:
        nodes = getLeafs(Tree[ID])
        if len(set(herbs)&set(nodes)) != 0 and len(nodes) != 0:
            f.write(ID+','+str(len(set(herbs)&set(nodes))/float(len(nodes)))+'\n')
    f.close()
    return True

def getSubTreeOfHerb(Tree, RootID):
    data = pd.read_excel('../Data/Book_All Species.xls', 0, index_col = 0, head = True)
    herbs = [str(int(i)) for i in list(data.ID) if str(i).upper()!='NAN']
    subTree = {}
    c = 0
    for ID in herbs:
        print len(herbs), c
        c += 1
        if ID not in Tree.keys():
            print '###############', ID
            continue
        Node = Tree[ID]
        subTree[ID] = TaxonTerm(Node.ID, Node.Name, Node.Rank)
        subTree[ID].Childs = set()
        subTree[ID].seqs = [1]
        Node = Node.Parent
        newNode = subTree[ID]
        while(Node.ID != RootID):
            if not subTree.has_key(Node.ID):
                subTree[Node.ID] = TaxonTerm(Node.ID, Node.Name, Node.Rank)
                subTree[Node.ID].Childs = set()
                subTree[Node.ID].seqs = [0]
            subTree[Node.ID].Childs.add(newNode)
            newNode.Parent = subTree[Node.ID]
            
            newNode = subTree[Node.ID]
            Node = Node.Parent
    return subTree
##########         

def getRankPathes(Nodes):
    Pathes = set()
    IDs = getNodesByRank(Nodes, rank = 'species|subspecies')
    print len(IDs)
    for ID in IDs:
        node = Nodes[ID]
        path = node.Rank
        while(node.Parent != None):
            node = node.Parent
            if node.Rank != 'no rank':
                path = node.Rank+'|'+path
        Pathes.add(path)
    print len(Pathes)
    for i in Pathes:
        print i
       



