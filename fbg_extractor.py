#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

fb_members_file = "members.html"
link_list_file = "rw-members-links.txt"
name_list_file = "rw-members-names.txt"

file = open(fb_members_file, 'r')
fContents = file.read()
file.close()

html = BeautifulSoup(fContents)

nClass = html.findAll("div", attrs={"class" : "fsl fwb fcb"})
nLink = []
nLinkL = []
nLinkT = []
for div in nClass:
	nLink.append(div.findAll('a'))
	for link in div.findAll('a'):
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

