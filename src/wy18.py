#!/usr/bin/python
import sys,re,os,cgi;q,x,h,w=cgi.escape,os.path.exists,'<a href=','wypy?p='
load,t=lambda n:(x('w/'+n) and open('w/'+n).read()) or '','</textarea></form>'
f,i=cgi.FormContent(),'put type';y=f.get('p',[''])[0];y=('WyPy',y)[y.isalpha()]
fs,do,main=lambda s:reduce(lambda s,r:re.sub('(?m)'+r[0],r[1],s),(('\r',''),(
'(^|[^A-Za-z0-9?])(([A-Z][a-z]+){2,})',lambda m:(m.group(1)+'%s'+h+w+m.group(2
)+'%s>%s</a>')%((m.group(2),'&amp;q=e','?'),('','',m.group(2)))[x('w/'+m.group
(2))]),('^\{\{$','\n<ul>'),('^\* ','<li>'),('^}}$','</ul>'),('^---$','<hr>'),(
'\n\n','<p>'),('(ht|f)tp:[^<>"\s]+',h+'"\g<0>">\g<0></a>')),q(s)),lambda m,n:{
'get':'<h1>WyPy:%s%s%s&amp;q=f>%s</a></h1>(%s%s%s&amp;q=e>edit</a>)<p>%s'%(h,w,
n,n,h,w,n,fs(load(n)) or n),'edit':'<form action=%s%s method=POST><h1>%s <in'\
'%s=hidden name=p value=%s><in%s=submit></h1><textarea name=t cols=79 rows=17'\
'>%s'%(w,n,fs(n),i,n,i,q(load(n)))+t,'find':('<h1>Links: %s</h1>'%fs(n))+fs(
'{{\n* %s\n}}'%'\n* '.join([d for d in os.listdir('w/') if load(d).count(n)]))
}.get(m),lambda f=f:`(os.getenv("REQUEST_METHOD")!="POST") or open('w/'+y,'w'
).write(f['t'][0])`+`sys.stdout.write("Content-type: text/html; charset=utf-8"\
"\r\n\r\n<title>%s</title>"%y+do({'e':'edit','f':'find'}.get(f.get('q',[None])
[0],'get'),y))`;(__name__=="__main__") and main()