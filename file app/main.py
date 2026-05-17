#A simple file sharing app
#importing te necessary modules
#for http web server

import http.server

#provide access to BSD socket imterface
import socket

#frameowork for network servers
import socketserver

#display web based doc to users
import webbrowser

#to generate qrcode
import pyqrcode
from pyqrcode import QRCode

#converting QR CODE TO PNG
import png

#accessing os control
import os

#assigning the appropriate system control
PORT = 8010
#to find name of computer user
os.environ['USERPROFILE']

#changng the directory to access the files desktop wit help of os model
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive')
os.chdir(desktop)

#creating http request
Handler = http.server.SimpleHTTPRequestHandler
#returns host name of the system under which pthon interpreter is executed
hostname = socket.gethostname()

#finding ip address of the pc
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))

IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

#converting the ip address imto a form of  qrcode with help of qrcode

url = pyqrcode.create(link)
#saves qrcode inform of svg

url.svg("myqr.svg",scale=8)

#opens the qr code img in the browser

webbrowser.open('myqr.svg')

#creating http request and serving folder in port 8010
#and qrcode generated
#continous stream of data btw client server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port,PORT")
    print("Type this in your browser",IP)
    print("or Use the QRCode")
    httpd.serve_forever()

    #why tcp 8010 it uses a defined user protocol depending on the application

