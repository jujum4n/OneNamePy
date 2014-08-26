#By: Justin Chase (Onename.io/juju)
#Description: Simple and Small API for interacting with OneName.io json data
import json
import urllib2

#Pre:Given the onename.io USERNAME
#Post: Returns the entire json object using opendig
def getOpenDigJson(USERNAME):
	from opendig import ons_resolver #sudo pip install opendig - https://github.com/opennamesystem/opendig
	data=ons_resolver(USERNAME)
	return data

#Pre:Given the onename.io USERNAME
#Post: Returns the entire json object
def getOneNameJson(USERNAME):
	URL='https://onename.io/' + str(USERNAME) + '.json'
	data=json.load(urllib2.urlopen(URL))
#	print data
	return data

#Pre:Given the onename.io USERNAME
#Post: Returns .json URL
def getOneNameJsonURL(USERNAME):
	URL='https://onename.io/' + str(USERNAME) + '.json'
#	print URL
	return URL

#Pre:Given the onename.io USERNAME
#Post: Returns the entire .json file
def getOneNameURL(USERNAME):
	URL="https://onename.io/" + USERNAME
#	print URL
	return URL

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the bitcoin address
def getBitcoin(JSONTOPARSE):
	BITCOIN=JSONTOPARSE["bitcoin"]["address"]
#	print BITCOIN
	return BITCOIN

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the name formatted
def getRealName(JSONTOPARSE):
	REALNAME=JSONTOPARSE["name"]["formatted"]
#	print REALNAME
	return REALNAME

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the PGP Keyserver URL
def getPGPURL(JSONTOPARSE):
	PGPURL=JSONTOPARSE["pgp"]["url"]
#	print PGPURL
	return PGPURL

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the PGP Fingerprint
def getPGPFingerPrint(JSONTOPARSE):
	FINGERPRINT=JSONTOPARSE["pgp"]["fingerprint"]
#	print FINGERPRINT
	return FINGERPRINT

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the BIO
def getBio(JSONTOPARSE):
	BIO=JSONTOPARSE["bio"]
#	print BIO
	return BIO

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the website URL
def getWebsite(JSONTOPARSE):
	WEBSITE=JSONTOPARSE["website"]
#	print WEBSITE
	return WEBSITE

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the Location formatted
def getLocation(JSONTOPARSE):
	LOCATION=JSONTOPARSE["location"]["formatted"]
#	print LOCATION
	return LOCATION

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the GITHUB
def getGithub(JSONTOPARSE):
	GITHUB=JSONTOPARSE["github"]["username"]
#	print GITHUB
	return GITHUB

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the GITHUB URL
def getGithubURL(JSONTOPARSE):
	GITHUB=JSONTOPARSE["github"]["username"]
#	print GITHUB
	return "https://github.com/"+GITHUB

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the twitter @handle
def getTwitter(JSONTOPARSE):
	TWITTER=JSONTOPARSE["twitter"]["username"]
#	print TWITTER
	return TWITTER

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the whole twitter URL
def getTwitterURL(JSONTOPARSE):
	TWITTER=JSONTOPARSE["twitter"]["username"]
#	print TWITTER
	return "http://twitter/" + TWITTER

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the Cover URL
def getCover(JSONTOPARSE):
	COVER=JSONTOPARSE["cover"]["url"]
#	print COVER
	return COVER

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the Avatar URL
def getAvatar(JSONTOPARSE):
	AVATAR=JSONTOPARSE["avatar"]["url"]
#	print AVATAR
	return AVATAR

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the Graph URL
def getGraph(JSONTOPARSE):
	GRAPH=JSONTOPARSE["graph"]["url"]
#	print GRAPH
	return GRAPH

#Pre:Given the onename.io/USERNAME.json
#Post: Returns the version
def getVersion(JSONTOPARSE):
	VERSION=JSONTOPARSE["v"]
#	print VERSION
	return VERSION

#Pre:Given the onename.io/USERNAME in a text file
#Post: Returns the version associated Bitcoin address and username in a csv format
def getAllBTCAddrsOpenDig(FILEPATHNAME,OUTPUTFILEPATH):
	f = open(FILEPATHNAME, 'r')
	o = open(OUTPUTFILEPATH, 'w')
	for line in f:
		data=getOpenDigJson(line.rstrip('\r\n'))
		if (str(data)!="""{'status': 404, 'message': 'ERROR: Not found'}"""):
			BTCADDR=getBitcoin(data)
			print line.rstrip('\r\n')+","+str(BTCADDR)+"\n"
			o.write(line.rstrip('\r\n')+","+str(BTCADDR)+"\n")

#Pre:Given the onename.io/USERNAME in a text file
#Post: Returns the version associated Bitcoin address and username in a csv format
def getAllBTCAddrs(FILEPATHNAME,OUTPUTFILEPATH):
	f = open(FILEPATHNAME, 'r')
	o = open(OUTPUTFILEPATH, 'w')
	for line in f:
		data=getOneNameJson(line.rstrip('\r\n'))
		if (str(data)!="""{'status': 404, 'message': 'ERROR: Not found'}"""):
			BTCADDR=getBitcoin(data)
			print line.rstrip('\r\n')+","+str(BTCADDR)+"\n"
			o.write(line.rstrip('\r\n')+","+str(BTCADDR)+"\n")

#Pre:Given the onename.io/USERNAME
#Post: Prints all associated information related to that user using the onename.io .json files
def listAllJson(USERNAME):
	data=getOneNameJson(USERNAME)
	print "OneNameJsonUrl: " + getOneNameJsonURL(USERNAME)
	print "Bitcoin Name: " + USERNAME
	print "Bitcoin Address: " + getBitcoin(data)
	print "Real Name: " + getRealName(data)
	print "PGP Fingerprint: " + getPGPFingerPrint(data)
	print "PGP Keyserver URL: " + getPGPURL(data)
	print "Cover image URL: " + getCover(data)
	print "Avatar image URL: " + getAvatar(data)
	print "Graph image URL: " + getGraph(data)
	print "Twitter: " + getTwitter(data)
	print "Twitter URL: " + getTwitterURL(data)
	print "Github: " + getGithub(data)
	print "Github URL: " + getGithubURL(data)
	print "Location: " + getLocation(data)
	print "Website: " + getWebsite(data)
	print "Bio: " + getBio(data)
	print "OneName.io URL: " + getOneNameURL(USERNAME)
	print "Version: " + getVersion(data)

#Pre:Given the onename.io/USERNAME
#Post: Prints all associated information related to that user using the onename.io .json files
def listAllOpendigJson(USERNAME):
	data=getOpenDigJson(USERNAME)
	print "OneNameJsonUrl: " + getOneNameJsonURL(USERNAME)
	print "Bitcoin Name: " + USERNAME
	print "Bitcoin Address: " + getBitcoin(data)
	print "Real Name: " + getRealName(data)
	print "PGP Fingerprint: " + getPGPFingerPrint(data)
	print "PGP Keyserver URL: " + getPGPURL(data)
	print "Cover image URL: " + getCover(data)
	print "Avatar image URL: " + getAvatar(data)
	print "Graph image URL: " + getGraph(data)
	print "Twitter: " + getTwitter(data)
	print "Twitter URL: " + getTwitterURL(data)
	print "Github: " + getGithub(data)
	print "Github URL: " + getGithubURL(data)
	print "Location: " + getLocation(data)
	print "Website: " + getWebsite(data)
	print "Bio: " + getBio(data)
	print "OneName.io URL: " + getOneNameURL(USERNAME)
	print "Version: " + getVersion(data)

###########################
#For Testing Purposes
#getAllBTCAddrs("newlist", "output.csv")
#NAME="juju"
#listAllJson(NAME)
#listAllOpendigJson(NAME)
###########################
