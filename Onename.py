#By: Justin Chase (Onename.io/juju)
#Description: Simple and Small API for interacting with OneName.io json data
import json
import urllib2
 
#Pre: Given the (u/) USERNAME
#Post: Returns the entire json object using opendig
def getOpenDigJson(USERNAME):
	from opendig import ons_resolver #sudo pip install opendig - https://github.com/opennamesystem/opendig
	try:
		data=ons_resolver(USERNAME)
	except ValueError:
		return "No data found to return"
	else:
		return data
 
#Pre: Given the (u/) USERNAME
#Post: Returns the entire json object
def getOneNameJson(USERNAME):
	URL='https://onename.io/' + str(USERNAME) + '.json'
	try:
		data=json.load(urllib2.urlopen(URL))
	except urllib2.HTTPError:
		return str("HTTPException")
	else:
		return data
 
#Pre: Given the (u/) USERNAME
#Post: Returns .json URL
def getOneNameJsonURL(USERNAME):
	URL='https://onename.io/' + str(USERNAME) + '.json'
#	print URL
	return str(URL)
 
#Pre: Given the (u/) USERNAME
#Post: Returns the entire .json file
def getOneNameURL(USERNAME):
	URL="https://onename.io/" + str(USERNAME)
#	print URL
	return str(URL)
 
#Pre: Given the profile data
#Post: Returns the bitcoin address
def getBitcoin(JSONTOPARSE):
	try:
		BITCOIN=JSONTOPARSE["bitcoin"]["address"]
	except KeyError:
		return "No Bitcoin Address found"
	else:
	#	print BITCOIN
		return str(BITCOIN)
 
#Pre: Given the profile data
#Post: Returns the name formatted
def getRealName(JSONTOPARSE):
	try:
		REALNAME=JSONTOPARSE["name"]["formatted"]
	except KeyError:
		return "No Name found"
	else:
	#	print REALNAME
		return str(REALNAME)
 
#Pre: Given the profile data
#Post: Returns the PGP Keyserver URL
def getPGPURL(JSONTOPARSE):
	try:
		PGPURL=JSONTOPARSE["pgp"]["url"]
	except KeyError:
		return "No PGP key found"
	else:
#		print PGPURL
		return str(PGPURL)
 
#Pre: Given the profile data
#Post: Returns the PGP Fingerprint
def getPGPFingerPrint(JSONTOPARSE):
	try:
		FINGERPRINT=JSONTOPARSE["pgp"]["fingerprint"]
	except KeyError:
		return "No PGP key found"
	else:
	#	print FINGERPRINT
		return str(FINGERPRINT)
 
#Pre: Given the profile data
#Post: Returns the BIO
def getBio(JSONTOPARSE):
	try:
		BIO=JSONTOPARSE["bio"]
	except KeyError:
		return "No Bio found"
	else:
	#	print BIO
		return str(BIO)
 
#Pre: Given the profile data
#Post: Returns the website URL
def getWebsite(JSONTOPARSE):
	try:
		WEBSITE=JSONTOPARSE["website"]
	except KeyError:
		return "No website found."
	else:
	#	print WEBSITE
		return str(WEBSITE)
 
#Pre: Given the profile data
#Post: Returns the Location formatted
def getLocation(JSONTOPARSE):
	try:
		LOCATION=JSONTOPARSE["location"]["formatted"]
	except KeyError:
		return "No Location found"
	else:
	#	print LOCATION
		return str(LOCATION)
 
#Pre: Given the profile data
#Post: Returns the GITHUB
def getGithub(JSONTOPARSE):
	try:
		GITHUB=JSONTOPARSE["github"]["username"]
	except KeyError:
		return "No Github found"
	else:
	#	print GITHUB
		return str(GITHUB)
 
#Pre: Given the profile data
#Post: Returns the GITHUB URL
def getGithubURL(JSONTOPARSE):
	try:
		GITHUB=JSONTOPARSE["github"]["username"]
	except KeyError:
		return "No Github found"
	else:
	#	print GITHUB
		return "https://github.com/"+ str(GITHUB)
 
#Pre: Given the profile data
#Post: Returns the twitter @handle
def getTwitter(JSONTOPARSE):
	try:
		TWITTER=JSONTOPARSE["twitter"]["username"]
	except KeyError:
		return "No Twitter found"
	else:
	#	print TWITTER
		return str(TWITTER)
 
#Pre: Given the profile data
#Post: Returns the whole twitter URL
def getTwitterURL(JSONTOPARSE):
	try:
		TWITTER=JSONTOPARSE["twitter"]["username"]
	except KeyError:
		return "No Twitter found"
	else:
	#	print TWITTER
		return "http://twitter/" + str(TWITTER)
 
#Pre: Given the profile data
#Post: Returns the Cover URL
def getCover(JSONTOPARSE):
	try:
		COVER=JSONTOPARSE["cover"]["url"]
	except KeyError:
		return "No Cover image found"
	else:
		return str(COVER)
 
#Pre: Given the profile data
#Post: Returns the Avatar URL
def getAvatar(JSONTOPARSE):
	try:
		AVATAR=JSONTOPARSE["avatar"]["url"]
	except KeyError:
		return "No Avatar image found"
	else:
		#	print AVATAR
		return str(AVATAR)
 
#Pre: Given the profile data
#Post: Returns the Graph URL
def getGraph(JSONTOPARSE):
	try:
		GRAPH=JSONTOPARSE["graph"]["url"]
	except KeyError:
		return "No Graph image found"
	else:
	#	print GRAPH
		return str(GRAPH)
 
#Pre: Given the profile data
#Post: Returns the version
def getVersion(JSONTOPARSE):
	try:
		VERSION=JSONTOPARSE["v"]
	except KeyError:
		return "No Version found"
	else:
	#	print VERSION
		return str(VERSION)
 
#Pre: Given the usernames (u/) in a text file
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
	o.close()
	f.close()

#Pre: Given the Output file path and name and the Json to write
#Post: Writes out the JSON data to the given Output file path
def writeOutJson(OUTPUTFILEPATH, JSONTOWRITE):
	with open(OUTPUTFILEPATH, 'w') as outfile:
		json.dump(JSONTOWRITE, outfile)

#Pre: Given the usernames (u/) in a text file
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
	o.close()
	f.close()
 
#Pre: Given the username (u/)
#Post: Prints all associated information related to that user using the onename.io .json files
def listAllJson(USERNAME):
	data=getOneNameJson(USERNAME)
	if(data!="HTTPException"):
		print "OneNameJsonUrl: " + getOneNameJsonURL(USERNAME)
		print "OneName: " + USERNAME
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
	else:
		print USERNAME + " not found or this is reserved."

#Pre: Given the Profile data prints it out
#Post: Prints all associated information related to that user using the Profile data passed in as parameter
def listAllJsonData(data):
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
	print "Version: " + getVersion(data)
 
#Pre: Given the username (u/)
#Post: Prints all associated information related to that user using the onename.io .json files
def listAllOpendigJson(USERNAME):
	data=getOpenDigJson(USERNAME)
#	print data
	print "OneNameJsonUrl: " + getOneNameJsonURL(USERNAME)
	print "OneName: " + USERNAME
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
	
#Pre: Given Profile v02 Information creates a Profile
#Post: Returns a Profile with the given Information, if something is not given NoneType is passed in
def format_profile_v02(name=None, location=None, bio=None, website=None, avatar_url=None, cover_url=None, twitter_username=None,twitter_proof=None, facebook_username=None,facebook_proof=None, linkedin_username=None,linkedin_proof=None, github_username=None, github_proof=None, bitcoin_address=None, pgp_fingerprint=None, pgp_url=None):
	profile ={
		"avatar": 
		{
			"url": ""
		},
		"website": "", 
		"bio": "", 
		"cover": 
		{
			"url": ""
		}, 
		"twitter": 
		{
			"proof": 
			{
				"url": ""
			}, 
			"username": ""
		},
		"facebook": 
		{
			"proof": 
			{
				"url": ""
			}, 
			"username": ""
		},
		"linkedin": 
		{
			"proof": 
			{
				"url": ""
			}, 
			"username": ""
		}, 
		"graph": 
		{
			"url": ""
		}, 
		"pgp": 
		{
			"fingerprint": "",
			"url": ""
		}, 
		"v": "0.2", 
		"location": 
		{
			"formatted": ""
		}, 
		"github": 
		{
			"proof": 
			{
				"url": ""
			}, 
			"username": ""
		}, 
		"name": 
		{
			"formatted": ""
		}, 
		"bitcoin": 
		{
			"address": ""
		}
	}
	profile['v'] = '0.2'
	profile['name']['formatted'] = name
	profile['location']['formatted'] = location
	profile['bio'] = bio
	profile['website'] = website
	profile['avatar'] = {"url": avatar_url}
	profile['cover'] = {"url": cover_url}
	profile['bitcoin'] = {"address": bitcoin_address}
	profile['twitter'] = {"username": twitter_username}
	profile['twitter']['proof']={"url": twitter_proof}
	profile['facebook'] = {"username": facebook_username}
	profile['facebook']['proof']={"url": facebook_proof}
	profile['linkedin'] = {"username": linkedin_username}
	profile['linkedin']['proof']={"url": linkedin_proof}
	profile['github'] = {"username": github_username}
	profile['github']['proof']={"url": github_proof}
	profile['pgp']['fingerprint'] = pgp_fingerprint
	profile['pgp']['url'] = pgp_url
	return profile
 
#Pre: Given Profile v02 Information from Input (Taken from OpenSpecs)
#Post: Returns a profile with v02 no validation for Username ownership
def format_profile_from_user_input_v02():
	profile = {}
	input_items = [
		{'name': 'name', 'prompt': 'Name: '},
		{'name': 'location', 'prompt': 'Location: '},
		{'name': 'bio', 'prompt': 'Bio: '},
		{'name': 'website', 'prompt': 'Website: '},
		{'name': 'twitter_username', 'prompt': 'Twitter username: '},
		{'name': 'github_username', 'prompt': 'Github username: '},
		{'name': 'avatar_url', 'prompt': 'Avatar url: '},
		{'name': 'cover_url', 'prompt': 'Cover url: '},
		{'name': 'bitcoin_address', 'prompt': 'Bitcoin address: '},
		{'name': 'pgp_fingerprint', 'prompt': 'PGP Key Fingerprint: '},
		{'name': 'pgp_url', 'prompt': 'URL of hosted PGP Public Key: '},
	]
	for input_item in input_items:
		profile[input_item['name']] = raw_input(input_item['prompt'])
	return profile

#Pre: Testing Function
#Post: Testing Function
#def testt():
	#getAllBTCAddrs("newlist", "output.csv")
	#NAME='juju'
	#profile=getOneNameJson(NAME)
	#print type(profile)
	#print profile["bitcoin"]["address"]
	#listAllJson(NAME)
	#listAllOpendigJson(NAME)
	#profile=format_profile_from_user_input_v02()
	#print profile
	#profile=format_profile_v02(name='FirstName LastName', location='Location', bio=None, website=None, avatar_url=None, cover_url=None, twitter_username=None,twitter_proof=None, facebook_username=None,facebook_proof=None, linkedin_username=None,linkedin_proof=None, github_username=None, github_proof=None, bitcoin_address=None, pgp_fingerprint=None, pgp_url=None)
	#print profile
	#listAllJsonData(profile)
	#writeOutJson(NAME + '.json', profile)
#testt()
