import hashlib
import urllib2
import json
import requests


class VoiceIt:
    developerId = ""
    urlUsers = 'https://siv.voiceprintportal.com/sivservice/api/users'
    urlEnrollments = 'https://siv.voiceprintportal.com/sivservice/api/enrollments'
    urlAuthentication = 'https://siv.voiceprintportal.com/sivservice/api/authentications'

    def getSHA256(self, strData):
        return hashlib.sha256(strData).hexdigest()

    def __init__(self, devId):
        print("Constructor for VoiceIt Called")
        self.developerId = devId
        print("Parameters Initialized")

    def createUser(self, mail, passwd, firstName, lastName, phone1="", phone2="", phone3=""):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'application/json', "VsitEmail": email, "VsitPassword": password, "VsitDeveloperId": self.developerId,
                   "VsitFirstName": firstName, "VsitLastName": lastName, "VsitPhone1": phone1, "VsitPhone2": phone2, "VsitPhone3": phone3}
        response = ""
        try:
            response = requests.post(self.urlUsers, headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def deleteUser(self, mail, passwd):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'application/json', "VsitEmail": email,
                   "VsitPassword": password, "VsitDeveloperId": self.developerId}
        response = ""
        try:
            response = requests.delete(self.urlUsers, headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def getUser(self, mail, passwd):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'application/json', "VsitEmail": email,
                   "VsitPassword": password, "VsitDeveloperId": self.developerId}
        response = ""
        try:
            response = requests.get(self.urlUsers, headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def setUser(self, mail, passwd, firstName, lastName, phone1="", phone2="", phone3=""):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'application/json', "VsitEmail": email, "VsitPassword": password, "VsitDeveloperId": self.developerId,
                   "VsitFirstName": firstName, "VsitLastName": lastName, "VsitPhone1": phone1, "VsitPhone2": phone2, "VsitPhone3": phone3}
        response = ""
        try:
            response = requests.put(self.urlUsers, headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def createEnrollment(self, mail, passwd, pathToEnrollmentWav, contentLanguage=""):
        email = mail
        password = self.getSHA256(passwd)
        wavData = open(pathToEnrollmentWav, 'rb').read()
        headers = {'Content-Type': 'audio/wav', "VsitEmail": email,
                   "VsitPassword": password, "VsitDeveloperId": self.developerId, "ContentLanguage":contentLanguage}
        response = ""
        try:
            response = requests.post(
                self.urlEnrollments, headers=headers, data=wavData)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def createEnrollmentByWavURL(self, mail, passwd, urlToEnrollmentWav, contentLanguage=""):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'audio/wav', "VsitEmail": email, "VsitPassword": password,
                   "VsitDeveloperId": self.developerId, "VsitwavURL": urlToEnrollmentWav, "ContentLanguage":contentLanguage}
        response = ""
        try:
            response = requests.post(
                self.urlEnrollments + "/bywavurl", headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def getEnrollments(self, mail, passwd):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'application/json', "VsitEmail": email,
                   "VsitPassword": password, "VsitDeveloperId": self.developerId}
        response = ""
        try:
            response = requests.get(self.urlEnrollments, headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def deleteEnrollment(self, mail, passwd, enrollmentId):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'application/json', "VsitEmail": email,
                   "VsitPassword": password, "VsitDeveloperId": self.developerId}
        response = ""
        try:
            response = requests.delete(
                self.urlEnrollments + "/" + enrollmentId, headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def authentication(self, mail, passwd, pathToAuthenticationWav, accuracy, accuracyPasses, accuracyPassIncrement, confidence, contentLanguage=""):
        email = mail
        password = self.getSHA256(passwd)
        wavData = open(pathToAuthenticationWav, 'rb').read()
        headers = {'Content-Type': 'audio/wav', "VsitEmail": email, "VsitPassword": password, "VsitDeveloperId": self.developerId,
                   "VsitAccuracy": accuracy, "VsitAccuracyPasses": accuracyPasses, "VsitAccuracyPassIncrement": accuracyPassIncrement, "VsitConfidence": confidence, "ContentLanguage":contentLanguage}
        response = ""
        try:
            response = requests.post(
                self.urlAuthentication, headers=headers, data=wavData)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()

    def authenticationByWavURL(self, mail, passwd, urlToAuthenticationWav, accuracy, accuracyPasses, accuracyPassIncrement, confidence, contentLanguage=""):
        email = mail
        password = self.getSHA256(passwd)
        headers = {'Content-Type': 'audio/wav', "VsitEmail": email, "VsitPassword": password, "VsitDeveloperId": self.developerId, "VsitwavURL": urlToAuthenticationWav,
                   "VsitAccuracy": accuracy, "VsitAccuracyPasses": accuracyPasses, "VsitAccuracyPassIncrement": accuracyPassIncrement, "VsitConfidence": confidence, "ContentLanguage":contentLanguage}
        response = ""
        try:
            response = requests.post(
                self.urlAuthentication + "/bywavurl", headers=headers)
            return response.text
        except requests.exceptions.HTTPError, e:
            return e.read()
