#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs
from aparser import Hantei

ha = Hantei()

class Cutmorph:
    def cut(self,sent):
        #sent = raw_input("カットしたい文字列を入力：").decode("utf-8")
        numarray = [-1]
        for x in range(len(sent)-1):
            if ha.hantei(sent[x]) != ha.hantei(sent[x+1]):
                numarray.append(x)
        numarray.append(len(sent))
        array = []
        for y in range(len(numarray)-1):
            before = int (numarray[y]) + 1
            last = int (numarray[y+1] ) + 1
            array.append(sent[before:last])
        return array

cu = Cutmorph()
filename = raw_input("作成したい形態素の連鎖辞書の元ファイルを入力：")
f = open(filename)

fout = codecs.open("markov_dict_"+filename,"w","utf-8")
mchain = []
for line in f:
    line = line.strip().decode("utf-8")
    array =  cu.cut(line)
    for x in range(len(array)-1):
        #print array[x]+":"+array[x+1]
        mchain.append(array[x]+":"+array[x+1])
    #for a in array:
    #    print a
    #    fout.write(a+"\n")

#comb = [(a,array.count(a)) for a in array] #律速部分
comb = [(m,mchain.count(m)) for m in mchain] #律速部分

#print comb

rmved = []
for c in comb:
    if not c in rmved:
        rmved.append(c)
rmved = sorted(rmved,key=lambda x:int(x[1]),reverse=True)

for r in rmved:
    print r[0],r[1]
    fout.write(r[0]+":"+str(r[1])+"\n")

f.close()
fout.close()
