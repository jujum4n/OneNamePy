OneNamePy
=========

###Description: 
  Simple Python API, to preform RESTAPI Calls for the JSON data on Onename.io

---
###Example Usage:
```python
import OneNamePy
print "OneNameJsonUrl: " + getOneNameJsonURL("juju")
print "OneName.io URL: " + getOneNameURL("juju")
data=getOneNameJson("juju")
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
```
---
