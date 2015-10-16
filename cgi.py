#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
#from subprocess import call
import os
import time

print "Content-type: text/html\n\n"
print "<head>"
print "<title>fotograf basiliyor...</title>"
print "</head>"
print "<body>"
print "<h3>Istediginiz fotograf/lar basiliyor...</h3>"
print "</body>"

form = cgi.FieldStorage()
number = form.getvalue('number')
file = form.getvalue('file')


print number
print "adet"
print file
print "yaziliyor"

os.system('lp -d yazici -n%d %s' %(int(number), file))
