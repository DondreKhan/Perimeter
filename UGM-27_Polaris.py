#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import urllib

index = 0
linkList = []
linkFile = open("rw-members-links.txt", 'r')
for line in linkFile:
	linkList.append(line)

nameFile = open('rw-members-names.txt', 'r');
for line in nameFile:
	name = line;
	name = name.replace('\n', '');
	nameU = name.replace(' ', '_');
	dossier = open('dossiers/'+nameU+'.html', 'w');
	dossierContents = '''
<html>
<head>
<title>'''+name+'''</title>

</head>
<body style="padding: 30px">

<h1>Your new employee, <a href="'''+linkList[index]+'''">'''+name+'''</a></h1>

<p>The applicant, '''+name+''', who you just googled as part of your hiring process is a member of a Neo Nazi Facebook group 
and is an accessory to many appalling pro Nazi actions on the website Rational Wiki.  We figure that the purpose of your 
Google search (or any other preferred search engine that you use) was for your company to be warned if your applicant was 
part of any sort of socially unacceptable behavior or morally objectional activities.  We can tell you with confidence that 
'''+name+''' is not someone that you would want to have working for your company.  We are also inclined to keep a list of any 
companies that have employed '''+name+''', so that any Neo Nazis who are looking for work will be able to easily find companies 
who are sympathetic to and are willing to hire them.</p>

<p>Given the nature of the activities in which your new employee has been engaged in, it is very likely that '''+name+''' is sexually aroused by rape and has violent, uncontrollable rape fantasies.  More specifically due to the nature of the harassment for which '''+name+''' is an accessory, '''+name+''' is very likely sexually aroused by the genocidal rape committed by Nazis against millions of women in the Soviet Union.  That's right; your new employee '''+name+''' jacks off to the horrible rapes that the Nazis committed.</p>

<h2>Neo Nazi Facebook group membership</h2>

<p>'''+name+''' has been engaged with the Neo Nazi Facebook group <a href="https://www.facebook.com/groups/114421575256439/">RationalWiki</a>
which is a discussion group for the shamelessly unabashed pro Nazi website RationalWiki.org.  We can prove beyond any doubt that Rational Wiki is in fact a Neo Nazi website.  Members of it, including members of the board of trustees, have engaged in willful and persistent spewing of vile Nazi apologetics, even in the face of overwhelming evididence.  Your new employee '''+name+''' has been an accessory to these activities.</p>

<h2>Evidence against '''+name+'''</h2>

<img src="../images/Nazi-rape-graphical.png" width="500px"/>
<p>Essentially everything you need to know about '''+name+''' in a nutshell, a willing particpant in these events.</p>

<img src="../images/german-brutality-ussr-ww2-pictures.jpg" height="350px"/>
<br/>
<h4>Your new employee, '''+name+''' is sexually turned on by this.</h4>

<p>As you can see, '''+name+''' is incapable of any sort of compassion towards rape victims.  Quite simply, '''+name+''' does not care at all about rape victims.

<p>Here we offer you extremely damning evidence that '''+name+''' is in fact guilt of all charges and accusations that we have so far made.  '''+name+''' has been a willing accessory to all of the apalling Nazi apologetic behavior committed by Rational Wiki.</p>

<h3>Quotes</h3>

<p>This is a very limited selection of the worst comments that were made by Rational Wikis, who all engaged in this harassment and incitement of the idea that Soviet women deserved to be raped by Germans.</p>

<p>"RAPE RAPE NAZI RAPE" -Hipocrite</p>
<p>"Hi, Andy Schlafly's an Asshole who needs to get raped so he can see how great gay sex really is." -Jimmy Wales</p>
<p>"And rape!" -Hipocrite</p>
<p>"BOLDING EVERY TIME HE SAYS RAPE BECAUSE IT'S NOT OBSESSIVE AT ALL!" *bolded every use of the word rape on the page* -Hipocrite</p>
<p>"Notice:  This article has <b>too much rape</b>.  Please edit it such that it includes a reasonable amount of rape." -Hipocrite</p>
<p>"NAZI RAPE NAZI RAPE RAPE NAZI!" -Hipocrite</p>
<p>"...NAZI RAPE. It's basically a joke at this point" -Hipocrite</p>
<p>"Also, nazirape nazirape nazirape woo woo woo." -Nutty Roux</p>
<p>"It's been my experience that, in addition to Nazis, ableists, racists, and ageists." -Nutty Roux</p>
<p>"Woo!  Nazirape!" -PowderSmokeAndLeather</p>

<h3>Transcript</h3>

<p>This is a transcript from a Rational Wiki talk page where many users spewed vile Nazi apologetics in the face of evidence provided by a World War II historian.  Among other activities, they claimed the historical context for the war crimes (they focused only on rape, even though the author included non rape crimes) committed agianst Germans were somehow victim blaming against the Germans.  It was repeatedly stated to them that mainstream historians consider historical context necessary and that its absense is victim blaming to the victims of German genocide.  It was also stated that the arguments used by Rational Wiki users against historical context echoed the same arguments of Nazi apologist historians.  The mainstream historian Richard Bessel described Germans in <u>Germany 1945</u> as (paraphrase) "experiencing the same sorts of attrocities that they had committed against the same peoples earlier in the war."  '''+name+''' was a willing participant in this Nazi apologetic activity.</p>

<p>Rational Wiki users' arguments can be summarized as:</p>
<li>Caiming that historical context is victim blaming - Repeatedly established as Nazi apologetic and victim blaming to victims of Nazi genocide</li>
<li>Inciting the idea that the article author is somehow aroused by rape - Clear psychological projection as a defense mechanism on the part of Rational Wiki users who somehow got hung up on mentions of rape even though the author mentioned crimes other than rape</li>
<li>Personal attacks against the author</li>
<li>Repeating old Nazi apologetic myths</li>

<iframe src="../transcripts/ArticleTranscript.txt" width="700px" height="600px"></iframe>

<h3>Screenshots</h3>

<img src="../images/RW-justifies-rape.png" width="700px"/>
<p>Rational Wiki members believe that rape is morally justified against people who they disagree with.</p>
<img src="../images/Hipocrite-and-rape.png" width="700px"/>
<img src="../images/Hipocrite-makes-rape-a-joke.png" width="700px"/>
<img src="../images/Hipocrite-makes-rape-a-joke-2.png" width="700px"/>
<img src="../images/Hipocrite-Nazi-rape.png" width="700px"/>
<img src="../images/Hipocrite-Nazi-rape-rev.png" width="700px"/>
<img src="../images/Hipocrite-says-rape-is-a-joke.png" width="700px"/>
<img src="../images/Mikal-is-a-pedophile.png" width="700px"/>
<p>Rational Wiki users are also pedophiles as well.  Not only do they have inappropriate interests in little girls, but they make bizzare defenses for them, such as attempts to claim that having sex with a 12 year old girl is somehow not pedophilia.</p>
<img src="../images/Nutty-Roux-Nazirape.png" width="700px"/>
<img src="../images/Nutty-Roux-says-Nazis-are-a-joke.png" width="700px"/>
<img src="../images/Nutty-roux-says-Weaseloid-supports-rape.png" width="700px"/>
<img src="../images/PSAL-Woo-Nazirape.png" width="700px"/>
<img src="../images/Weaseloid-justifies-rape.png" width="700px"/>

</body>\n
</html>\n
''';
	dossier.write(dossierContents);
	dossier.close();
	index = index + 1
