#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import urllib

index = 0
linkList = []
linkFile = open("../example/ex-members-links.txt", 'r')
for line in linkFile:
	linkList.append(line)

nameFile = open('../example/ex-members-names.txt', 'r');
for line in nameFile:
	name = line;
	name = name.replace('\n', '');
	nameU = name.replace(' ', '_');
	dossier = open('../example/dossiers/'+nameU+'.html', 'w');
	dossierContents = '''
<html>
<head>
<title>'''+name+'''</title>

</head>
<body style="padding: 30px">

<h1>Personal biography, <a href="'''+linkList[index]+'''">'''+name+'''</a></h1>

<p>My name is '''+name+''' and I am a proud pedophile.  I am sexually aroused by seeing all children, both children and images, between four and nine.  My orientation for sexual activity with children is not different in any way from people who are gay and attracted to people of the same sex as them.  Being a pedophile entitles me to the same rights as people who are gay.</p>

</body>\n
</html>\n
''';
	dossier.write(dossierContents);
	dossier.close();
	index = index + 1
