from mechanize import Browser
import re
from pyquery import PyQuery
import os

def geturl(line):
	htmlset = line.split("\"")
	return htmlset[1]

""" Enter your current details here """

user_id = ""							#Enter user id 
user_password = ""						#Enter password

""" Enter album details here """

album_name = ""							# give a name to the album
album_link = ""							# replace by link to album 


br = Browser()
br.set_handle_robots(False)

br.open("http://facebook.com")

""" logging in """

br.select_form(nr=0)							
br["email"] = user_id
br["pass"] = user_password

br.submit()

""" In case new browser notifications have been turned on """

try:
	br.form = list(br.forms())[0]
	formid1 = br.form.attrs['title']

	if formid1 == "Remember Browser":		
		br.submit()

	elif formid1 == "Review Recent Login":
		rbr.submit()

		br.form = list(br.forms())[0]
		br.submit(name='submit[This is Okay]')

		br.form = list(br.forms())[0]
		br.submit()

		br.form = list(br.forms())[0]
		br.submit()
	else:
		pass

except:
	pass    	#In case new browser notifications have been turned off


""" At this moment, successfully reached the news feed """	

try:
	response = br.open(album_link)
except:
	print "Wrong userid or password"

html = br.response().read()

bigset = []

for i in html.split('href'):
	if 'photo.php' in i:
		bigset.append(i)

urlset = []

bigset = bigset[2:]

for i in bigset:
	urlset.append(geturl(i))

for i in urlset:
	br.open(i)
	urlhtml = PyQuery(br.response().read())
	urlset[urlset.index(i)] = urlhtml("#fbPhotoImage").attr('src')

count = 1

album_name.replace('/','_')
album_name = album_name + "/"

try:
	os.makedirs(album_name)
except:
	pass

for i in urlset:
	filename = album_name+"image"+str(count)
	imgdata = br.open(i).read()
	imgfile = open(filename,'w')
	imgfile.write(imgdata)
	imgfile.close()
	os.rename(filename,filename+str(".jpg"))
	print "image"+str(count)," downloaded"
	count+=1
