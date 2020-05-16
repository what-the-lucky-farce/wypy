# whippy

Hello out there.
Not sure what I am going to do with this yet.

Here's some [music for coding](https://open.spotify.com/playlist/537xEagDmV3lfECrwvYCXt?si=RqUlUiCyS5Cfn9pIs4EgFw) wypy.



# Homepage of WyPy as of May 15, 2020

The rest of this page was stolen from
http://infomesh.net/2003/wypy/.



## WyPy: A Minimal Python Wiki


**Update**: on 3rd February 2004, a new **11 line** version of wypy was released.

### Introduction

WyPy is a wiki implemented in just *11 lines* of Python code (source: [wy.py.txt](http://infomesh.net/2003/wypy/wy.py.txt)), including shebang. It was written as a contender for the [ShortestWikiContest](http://c2.com/cgi/wiki?ShortestWikiContest), and implements all of the [basic Wiki principles](http://c2.com/cgi/wiki?WikiPrinciples). It is released under GPL 2. There is a [working example](http://sbp.f2o.org/2003/wypy) for you to try.

### Installation and Use

Download the [source code](http://infomesh.net/2003/wypy/wy.py.txt), and save it as wypy.py in a CGI executable directory of your Web server. Make sure that there is a writable folder named "w" under the root of the CGI service—the raw WikiFiles will be dumped there. Runs as a normal Python CGI.

### Text Formatting

-   WikiNames are replaced with wypy internal links.
-   "`\n{{`" starts an unordered list.
-   "`\n* [text]`" is a list item in an unordered list.
-   "`\n}}`" ends an unordered list.
-   "`---`" creates an `<hr>` element.
-   http: and ftp: URIs are replaced with links to those URIs
-   All HTML is replaced with its quoted equivalent (i.e. is forbidden).

### Notes

Previous versions:

-   [18 lines](http://infomesh.net/2003/wypy/wypy.py.txt)
-   [23 lines](http://infomesh.net/2003/wypy/wypy.txt)

WyPy is pronounced "whippy". It is capitalized irregularly, as "WyPy"; it appears as "wypy" elsewhere in text, unless used in a wiki. For more information about wikis, try [c2.com:WikiWiki](http://c2.com/cgi/wiki?WikiWiki). Many thanks to Aaron Swartz and anonymous contributors on the original wypy wiki for helping to trim those lines down from 23 to 18!

### Feedback

Please [contact the author](http://infomesh.net/sbp/#sbp).

[Sean B. Palmer](http://purl.org/net/sbp/ "A Homepage Of Sean B. Palmer")


