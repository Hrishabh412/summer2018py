#!/usr/bin/python2

import time
import webbrowser

print"press 1 for for string search"
print"press 2 for for image search"
print"press 3 for URL name"
print"press 4 for time and date"
print"press 5 for default browser"
print"press 6 for all network ip"
print"press 7 to get domain and owner name"

x=raw_input()

if x=='1':
   search_data=raw_input("enter a string")
   new_data=search_data.strip()
   new_data.split()
   for i in new_data:
      webbrowser.open_new_tab("http://www.google.com/search?q="+i)
elif x=="2":

   search_data=raw_input("enter a string")
   new_data=search_data.strip()
   new_data.split()
   for i in new_data:
      webbrowser.open_new_tab('https://www.google.com/search?q=%s& client=ubuntu&hs=dBh&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiO38XTp4jbAhVEe7wKHUqXB7cQ_AUoA3oECAAQBQ&biw=1535&bih=802='+i)
     
elif x=='3':
   print time.ctime()

