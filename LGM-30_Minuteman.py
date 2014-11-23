#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import urllib

index = 0
linkList = []
linkFile = open("../Montreal40k/m40k-members-links.txt", 'r')
for line in linkFile:
	linkList.append(line)

nameFile = open('../Montreal40k/m40k-members-names.txt', 'r');
for line in nameFile:
	name = line;
	name = name.replace('\n', '');
	nameU = name.replace(' ', '_');
	dossier = open('../Montreal40k/dossiers/'+nameU+'.html', 'w');
	dossierContents = '''
<html>
<head>
<title>'''+name+'''</title>

</head>
<body style="padding: 30px">

<h1>Your new employee, <a href="'''+linkList[index]+'''">'''+name+'''</a></h1>

<p>The applicant, '''+name+''', who you just googled as part of your hiring process is a member of a Facebook group run by, and willing associate of, a Neo Nazi who uses the name "MajorTom11" who has a verified history of collaboration with a German Neo Nazi software developer in Bavaria who has a long history of vicious cyberbullying of many Autistic people.  We figure that the purpose of your Google search was to be warned about any such activities by '''+name+'''.</p>

</body>\n
</html>\n
''';
	dossier.write(dossierContents);
	dossier.close();
	index = index + 1
