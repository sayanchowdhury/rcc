import os
import sys
import urllib
import httplib

#Change the SERVER_URL according to Server IP.
#By default, configured to localhost:8000
SERVER_URL = '127.0.0.1:8000'

def readsource(filepath):
    f=open(filepath)
    data=""
    filename=""
    data=f.read()
    f.close()
    filename = os.path.basename(filepath)
    return data, filename

def post(text,filename):
    data = urllib.urlencode({'filename': filename, 'text':text})
    h = httplib.HTTPConnection(SERVER_URL)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    h.request('POST', '/compile/', data, headers)
    r = h.getresponse()
    print r.read()

def main():
    path = sys.argv[1]
    text,filename = readsource(path)
    post(text, filename)

if __name__ == '__main__':
    main()
