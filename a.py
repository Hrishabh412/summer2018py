#!/usr/bin/python2

import time
import webbrowser

print"button1"
print"button2"
print"button3"
print"button4"
print"button5"
print"button6"
print"button7"

x=raw_input()

if x=='1':
   a=raw_input("enter a string")
   b=a.split()
   for i in b:
      webbrowser.open_new_tab("http://www.google.com/search?btng=1&q=%s" %i)
elif x=="2":
   print("image search")
elif x=='3':
   print time.ctime()

