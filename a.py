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
   for j in new_data:
      webbrowser.open_new_tab('https://www.google.com/search?q=%s& client=ubuntu&hs=dBh&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiO38XTp4jbAhVEe7wKHUqXB7cQ_AUoA3oECAAQBQ&biw=1535&bih=802='+i)
     
elif x=='3':
   print time.ctime()

elif x=='4':
   webbrowser.open_new_tab('http://')

elif x=='5':
   a=raw_input("Enter any statement    ")
   webbrowser.open_new_tab('https://who.is/whois/%s' %a)
   
elif choice=="6" :
	a=raw_input("Enter any word    ")
	url = ("http://www.google.com/search?q=%s"%a)
	response = requests.get(url)
	# parse html
	page = str(BeautifulSoup(response.content))


 	def getURL(page):
    
    		start_link = page.find("a href")
    		if start_link == -1:
        		return None, 0
    		start_quote = page.find('"', start_link)
    		end_quote = page.find('"', start_quote + 1)
    		url = page[start_quote + 1: end_quote]
    		return url, end_quote

	while True:
    		url, n = getURL(page)
    		page = page[n:]
    		if url:
        		print url
    		else:
                 break  
else :
   print "Wrong Input"

