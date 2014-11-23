#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import urllib

index = 0
linkList = []
linkFile = open("../Lexicanum/lex-members-links.txt", 'r')
for line in linkFile:
	linkList.append(line)

nameFile = open('../Lexicanum/lex-members-names.txt', 'r');
for line in nameFile:
	name = line;
	name = name.replace('\n', '');
	nameU = name.replace(' ', '_');
	dossier = open('../Lexicanum/dossiers/'+nameU+'.html', 'w');
	dossierContents = '''
<html>
<head>
<title>'''+name+'''</title>

</head>
<body style="padding: 30px">

<h1>Your new employee, <a href="'''+linkList[index]+'''">'''+name+'''</a></h1>

<p>The applicant, '''+name+''', who you just googled as part of your hiring process is a member of a Neo Nazi Facebook group 
and is an accessory to many appalling pro Nazi actions by the website Lexicanum.  We figure that the purpose of your 
Google search (or any other preferred search engine that you use) was for your company to be warned if your applicant was 
part of any sort of socially unacceptable behavior or morally objectional activities.  We can tell you with confidence that 
'''+name+''' is not someone that you would want to have working for your company.  We are also inclined to keep a list of any 
companies that have employed '''+name+''', so that any Neo Nazis who are looking for work will be able to easily find companies 
who are sympathetic to and are willing to hire them.</p>

<p>We assure you that all information contained in this document about '''+name+''' is true and accurate.  '''+name+''' has been a willing accessory to the vile Neo Nazi actions by Inquisitor S. against many severely disabled Autistic people all over Virginia.  The real life identity of Inquisitor S. was uncovered by investigators only two days after his first attack against Autistic people in Virginia.  Based on comments made by Inquisitor S., it is very likely that they were involved with vicious cyberbullying of Autisitic people for years earlier.</p>

</body>\n
</html>\n
''';
	dossier.write(dossierContents);
	dossier.close();
	index = index + 1
