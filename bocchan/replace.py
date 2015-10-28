#! /usr/bin/python
# -*- coding:utf-8 -*-

import re
import codecs

filename = raw_input("input file name: ")

fin = codecs.open(filename,"r","utf-8") #utf-8で読み込む
fout = codecs.open("trimmed_"+filename,"w","utf-8")
rmlist = codecs.open("rmlist.txt","w","utf-8")
           
for line in fin:  
    chara = re.findall(u"《[^《》]*》",line) #基本的にutf-8で操作
    for c in chara:
        print c
        rmlist.write(c)
        line = re.sub(c,"",line)    
    fout.write(line)
