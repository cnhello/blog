#-*-coding:utf-8-*-
import os
import cgi



def th(txt):
	txt = txt.replace('\n','')
	txt = txt.replace('\r','')
	txt = txt.replace('\n\r','')
	txt = txt.replace('\r\n','')
	return txt

def toTxt(fileName,txt):
	f = open('blog/'+fileName, 'w')
	f.write(txt+"\n")
	f.close()

def rh(fileName):
	fileHandle = open (fileName)
	html = fileHandle.read()
	fileHandle.close()
	return html


def readFile(fileName):

	Name = 'data\\'+fileName

	fileHandle = open (Name)

	lines= fileHandle.readlines()

	fileHandle.close()

	lineNum = 0

	pre = 0

	post = ''

	for line in lines:

		if line=='' or line == '\n' or line == '\r':
			continue

		if lineNum < 3:

			if lineNum==0:
				time = th(line)
				lineNum = lineNum + 1

			elif lineNum==1:
				title = th(line)
				lineNum = lineNum + 1

			elif lineNum==2:
				tags = line
				lineNum = lineNum + 1
				
		else:

			if th(line)=='<pre>' and pre==0:

				pre = 1

				post = post + '<pre>' +'\n'

				lineNum = lineNum + 1

			elif th(line)!='</pre>' and pre==1:

				post = post + cgi.escape(line)

				lineNum = lineNum + 1

			elif th(line)=='</pre>' and pre==1:

				pre = 0

				post = post + '</pre>' + '\n'

				lineNum = lineNum + 1

			elif line[0:3]=='<h1' or line[0:3]=='<h2' or line[0:3]=='<h3' or line[0:4]=='<img':

				post = post + '\n' + line

			else:

				line = th(line)

				post = post + '<p>' + line + '</p>' + '\n'

				lineNum = lineNum + 1

	
	fileHandle = open('post.tmp')
	html = fileHandle.read()
	fileHandle.close()

	#print title

	html = html.replace('{title}',title)
	html = html.replace('{h1}',title)
	html = html.replace('{content}',post)

	toTxt(fileName+'.html',html)

	return '<a href="' + fileName +'.html">' + title + '</a><span>2014.08.01</span>'


fs = os.listdir('data')

lilist = ''

for x in fs:
	
	try:
	
		t = readFile(x)
		
	except:
	
		print x

	lilist = lilist + '<li>' + t + '</li>'

	print t

fileHandle = open('home.tmp')
html = fileHandle.read()
fileHandle.close()

html = html.replace('{title}','正在输入_永不停歇的叨叨')
html = html.replace('{h1}','正在输入')
html = html.replace('{list}',lilist)

toTxt('index.html',html)
