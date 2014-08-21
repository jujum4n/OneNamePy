#By: Justin Chase (Onename.io/juju)
#Description: Simple and Small API for interacting with OneName.io json data

import json
import urllib2

#Pre:Given the onename.io USERNAME
#Post: Returns the entire .json file
def getOneNameJson(USERNAME):
	data=json.load(urllib2.urlopen("https://onename.io/" + USERNAME + ".json"))
#	print data
	return data

#Pre:Given the onename.io USERNAME
#Post: Returns .json URL
def getOneNameJsonURL(USERNAME):
	URL="https://onename.io/" + str(USERNAME) + ".json"
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

###########################
#For Testing Purposes
#data=getOneNameJson("juju")
#print "OneNameJsonUrl: " + getOneNameJsonURL("juju")
#print "Bitcoin Address: " + getBitcoin(data)
#print "Real Name: " + getRealName(data)
#print "PGP Fingerprint: " + getPGPFingerPrint(data)
#print "PGP Keyserver URL: " + getPGPURL(data)
#print "Cover image URL: " + getCover(data)
#print "Avatar image URL: " + getAvatar(data)
#print "Graph image URL: " + getGraph(data)
#print "Twitter: " + getTwitter(data)
#print "Twitter URL: " + getTwitterURL(data)
#print "Github: " + getGithub(data)
#print "Github URL: " + getGithubURL(data)
#print "Location: " + getLocation(data)
#print "Website: " + getWebsite(data)
#print "Bio: " + getBio(data)
#print "OneName.io URL: " + getOneNameURL("juju")
#print "Version: " + getVersion(data)
###########################
