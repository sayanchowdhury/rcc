import os
import sys
import json
import requests

#Change the SERVER_URL according to Server IP.
#By default, configured to localhost:8000
SERVER_URL = 'http://127.0.0.1:8000'

def readsource(filepath):
    f=open(filepath)
    data=""
    filename=""
    data=f.read()
    f.close()
    filename = os.path.basename(filepath)
    return data, filename

def post(text,filename):
    payload = {'filename': filename, 'text':text}
    headers = { "Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/plain"}
    resp = requests.post(SERVER_URL + '/compile/', data=payload, headers=headers)
    print resp.json()['output']

def main():
    path = sys.argv[1]
    text,filename = readsource(path)
    post(text, filename)

if __name__ == '__main__':
    main()
