#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

kanj = re.compile(ur'^[一-龥]*$')
hira = re.compile(ur'^[あ-ん]*$')
kata = re.compile(ur'^[ァ-ン]*$')

class Hantei:
    def hantei(self,moji):
        if (kanj.search(moji)!=None):
            return "kanji"
        elif(hira.search(moji)!=None):
            return "hiragana"
        elif(kata.search(moji)!=None):
            return "katakana"

