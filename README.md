OneNamePy
=========

###Description: 
  * Simple Python API, to preform RESTAPI Calls for the JSON data on Onename.io.
  * Last updated for Onename.io Version: 0.2 - 8/20/2014

---
###Example Usage: 
   * Most Objects are as dict or JSON, URL calls return as str, if you need it as a string you can use Ex: str(getBitcoin(data))
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
###Output:
```
OneNameJsonUrl: https://onename.io/juju.json
Bitcoin Address: 1jujuGykhtsMigKzZY7UDcfL2pWgKCK8u
Real Name: Justin Chase
PGP Fingerprint: 49E530348A9D9C2FB9F51C245C12E062A840EB1F
PGP Keyserver URL: http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x5C12E062A
840EB1F
Cover image URL: https://s3.amazonaws.com/dx3/juju
Avatar image URL: https://s3.amazonaws.com/kd4/juju
Graph image URL: https://s3.amazonaws.com/grph/juju
Twitter: @jujum4n
Twitter URL: http://twitter/@jujum4n
Github: jujum4n
Github URL: https://github.com/jujum4n
Location: California
Website: http://jujuman.org
Bio: Stay Digital
OneName.io URL: https://onename.io/juju
Version: 0.2
```
---
###Donate:
  1jujuGykhtsMigKzZY7UDcfL2pWgKCK8u

