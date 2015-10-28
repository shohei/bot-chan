#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs
import random

#fin = codecs.open("2gram.txt","r","utf-8")
fin = codecs.open("markov_dict_trimmed_bocchan.txt","r","utf-8")
fout = codecs.open("out_markov.txt","w","utf-8")
filearray = []
for line in fin:
    filearray.append(line)
fin_2gram = codecs.open("2gram.txt","r","utf-8")
bigram_array = []
for line in fin_2gram:
    bigram_array.append(line)
#print "bigram_array",bigram_array

def conversation(message):
    def calcarr(ch):
        arr = [] #arrは開始文字を先頭に含む2-gramのリスト。重複あり。
	for line in filearray:
	    lsplt = line.split(":")
	    if (lsplt[0] == ch.decode("utf-8")):
		num = int(lsplt[2]) #
	        for x in range(num):
	            arr.append(lsplt[1])
	#print arr
        return arr

    def nextstr(array):
	return array[random.randint(0,len(array)-1)] #後続する形態素を乱数を使って返す

    def calcarr_bigram(ch):
	arr = [] #arrは開始文字を先頭に含む2-gramのリスト。重複あり。
	for line in bigram_array:
	    if (line[0] == ch.decode("utf-8")):
		num = int(str(line[2:]))
	        for x in range(num):
		    arr.append(line[1:2])
	return arr

    message = message.decode("utf-8")
    number = random.randint(0,len(message)-1)
    startch = message[number].encode("utf-8")
    
    sent = [startch]
    #会話文の先頭の文字
    next_array = calcarr(startch)
    if (next_array == []):
	print "###2-gramコード起動(開始文字）(デバッグ用です)##"
	next_array = calcarr_bigram(startch)
	#print "next_array",next_array
    #n = nextstr(calcarr(startch))
    n = nextstr(next_array)
    sent.append(n) #会話文の次の言葉（形態素）を付加
    n = n.encode('utf-8')

    while (n != "。"): #終端記号にならない限り繰り返す
        nextarray = calcarr(n)	
	if (nextarray == []):
	    print "###空配列なので2gramコード起動(中の人の都合です)###"
	    nextarray = calcarr_bigram(n)
	    #print "計算された配列",nextarray
	#print "計算された2-gramリスト",nextarray
	n = nextstr(nextarray)
	n = n.encode('utf-8')
	#print "確率的にとる次の文字",n
	sent.append(n)
	if(len(sent) >=20):
	    break
    return sent

message = "null" #初期化
print "人工知能と会話しましょう。"
print "やめる場合は　bye　と入力してください。"
while(1):
    message = raw_input("あなた：")
    print "人工知能:",
    if message == "bye":
        print "bye!"
	break
    sent = conversation(message)
    for s in sent:
        print s,
    print 
    

fin.close()
fout.close()
