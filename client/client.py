import os
import sys
import urllib
import httplib


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

    h = httplib.HTTPConnection('192.168.1.102:8000')

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
    
    
