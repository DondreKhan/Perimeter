#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

fb_members_file = "../Lexicanum/lexicanum-fb.html"
link_list_file = "../Lexicanum/lex-members-links.txt"
name_list_file = "../Lexicanum/lex-members-names.txt"

file = open(fb_members_file, 'r')
fContents = file.read()
file.close()

html = BeautifulSoup(fContents)

nClass = html.findAll("li", attrs={"class" : "UFIRow UFIComment display UFIComponent"})
nLink = []
nLinkL = []
nLinkT = []
for li in nClass:
	nLink.append(li.findAll('a'))
	for link in li.findAll('a', attrs={"class" : " UFICommentActorName"}):
		nLinkL.append(link.get("href"))
		nLinkT.append(link.get_text())

linkFile = open(link_list_file, 'a')
for i in nLinkL:
	linkFile.write(i.encode('utf8')+'\n')
linkFile.close()

nameFile = open(name_list_file, 'a')
for i in nLinkT:
	nameFile.write(i.encode('utf8')+'\n')
nameFile.close()

