import socket
import sys
import ssl
import re
from threading import local



class SmartClient():

    def __init__(self, domain = sys.argv[1], port=80, path = '/',retry_connect=7, headers=[200,404,503,505], password_protected = False):
        self.domain = domain
        self.port = port
        self.retry_connect = retry_connect
        self.s = None
        self.path=path
        self.headers = headers
        self.password_protected=password_protected

    def connectWith80(self):
        numArgs = len(sys.argv)
        if numArgs > 2:
            print("too many arguements given")
            exit(0)
        if "www" not in self.domain:
            self.domain = 'www.' + self.domain
        print(self.domain)
        
        location = self.domain
        localA = location.split("/")
        if len(localA) > 1:
            self.path = self.path+localA[1]
            self.location = localA[1]

        self.port = 80       
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.domain, self.port))
         #   print("CONNECTED THROUGH PORT 80")
        except:
            print("something went wrong. The web server doesn't exist")
            exit(0)
        message = "GET "+self.path+" HTTP/1.0\r\nHost:"+self.domain+"\r\n\r\n"
        self.s.sendall(message.encode())
        data = self.s.recv(10000)
        code = re.search(r"^(HTTP/1.[0|1])\s(\d+)", data.decode()).group(2)
        httpVersion = re.search(r"^(HTTP/1.[0|1])\s(\d+)", data.decode()).group(1)
        if int(code) in self.headers:
            http2bool = self.upgradeToHttp2()
            if(http2bool == True):
                print("Supports http2: Yes")
            else:
                print("Supports http2: no")
            self.getCookies(data.decode("utf-8"))     
        else:
            self.connectWith443()

    def connectWith443(self):
        version = "1.1"
        self.port = 443
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Error creating socket. Exiting.")
            sys.exit()
        
        try:
            self.s.connect((self.domain,self.port))
        except:
            print("something went wrong, can't connect from port 443")
            sys.exit()
        
        try:
            self.s = ssl.wrap_socket(self.s)
        except ssl.SSLError:
            raise Exception

        #r = (f"HEAD {path} HTTP/{version}\r\nHost: {self.domain}\r\n\r\n").encode()
        message = "GET "+self.path+" HTTP/1.0\r\nHost:"+self.domain+"\r\n\r\n"
        self.s.sendall(message.encode())
        response = ""
        while True:
            try:
                data = self.s.recv(4096).decode()
                if not data:
                    break
                response += data
            except socket.timeout:
                break
        #print(response)
        code = re.search(r"^(HTTP/1.[0|1])\s(\d+)", response).group(2)
        httpVersion = re.search(r"^(HTTP/1.[0|1])\s(\d+)", response).group(1)
        if int(code) in self.headers:
            http2bool = self.upgradeToHttp2()
            if(http2bool == True):
                print("Supports http2: Yes")
            else:
                print("Supports http2: no")
            self.getCookies(response) 
        else:
            #print("welp this is strange......... Cannot connect from both ports")
            print("Supports http2: Yes")
            self.getCookies(response) 
            sys.exit()
    
    def upgradeToHttp2(self): #found this
        context = ssl.create_default_context()
        context.set_alpn_protocols(['h2', 'spdy/3', 'http/1.1']) 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s = context.wrap_socket(self.s, server_hostname=self.domain)
        #print(self.domain)
        self.s.connect((self.domain, 443))
        #print("retrying connection")
        if self.s.selected_alpn_protocol() == "h2":
            return True
        else:
            return False
    
        
    
    def getCookies(self, response):
        printString = ""
        tempStr = ""
        cookieList = []
        tempCookiestoPrint = []
        i = 0
        responseList = response.split('\n')
        for x in range(0, len(responseList)):
            if 'Set-Cookie' in responseList[x]:
                i += 1
                cookie = responseList[x]
                cookieList.append(cookie)

        for x in range(0, len(cookieList)):
            cookieString = cookieList[x].split(";")
            for y in range(0, len(cookieString)):
                cookieString1 = cookieString[y].split(":")
                if('Set-Cookie' in cookieString1):
                    printString = ""
                    cookieString2 = cookieString1[1].split("=")
                    cookieName = cookieString2[0]
                    printString += "cookie name:" + cookieName
                else:
                    cookieString2 = cookieString1[0].split("=")
                    if(' expires' in cookieString2):
                        printString += ', expires time: '+ cookieString2[1] + ":" + cookieString1[1] + ":" + cookieString1[2] + '; '
                    if(' domain' in cookieString2):
                        printString += "domain name: " + cookieString2[1]
                   

            print(printString)
                              

        if(self.password_protected == False):
            print("Password protected: no")
        else:
            print("Password protected: Yes")         
        return


SmartClient1 = SmartClient()
SmartClient1.connectWith80()


  