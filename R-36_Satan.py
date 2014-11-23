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



</body>\n
</html>\n
''';
	dossier.write(dossierContents);
	dossier.close();
	index = index + 1
