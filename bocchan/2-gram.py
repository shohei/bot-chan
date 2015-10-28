#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

filename = raw_input("input the file name:")
fin = codecs.open(filename,"r","utf-8")
fout = codecs.open("2-gram_"+filename,"w","utf-8")
#sent = u"日本語で書いた日本語の文を解析します。"
arr = []
for line in fin:
    for i in range(len(line)-1):
        arr.append(line[i]+line[i+1])

comb = [(a,arr.count(a)) for a in arr] #ここが律速
rmv = []
for c in comb:
    if not c in rmv:
        rmv.append(c) #重複を削除(if notを使うのがミソ)
rmv = sorted(rmv,key=lambda x:int(x[1]),reverse=True)

for r in rmv:
    print r[0],r[1]
    fout.write(r[0]+str(r[1])+"\n")
    
fin.close()
fout.close()
