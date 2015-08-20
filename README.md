#VoiceIt Python wrapper
A Wrapper for using the VoiceIt Rest API.
##Installation
First make sure you have the [Requests](http://www.python-requests.org/en/latest/user/install/#install) library installed. Install from PyPi using pip, a package manager for Python.
```
pip install Requests
```
##Setup
Then simply download the [VoiceIt Python Library](https://github.com/voiceittech/voiceit-python/archive/master.zip) which includes all
dependencies.

##Usage
Then initialize a VoiceIt Object like this with your own developer id
```python
from VoiceIt import *
myVoiceIt = VoiceIt("123456")
```

Finally use all other API Calls as documented on the [VoiceIt API Documentation](https://siv.voiceprintportal.com/getstarted.jsp#apidocs) page.
