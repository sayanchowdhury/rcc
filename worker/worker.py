#!/usr/bin/python
import tempfile
import os
import subprocess
import sys
from retask.queue import Queue, Job


def file_read(file_name):
    f=open(file_name)
    content=f.read()
    f.close()
    return content,file_name


def main():
    queue = Queue('test')
    queue.connect()
    while True:
        task = queue.wait()
        name = task.data['filename']
        print "Received", name
        content = task.data['text']
        destdir = writesource(name, content)
        temp_path = os.path.join(destdir, name)
        x = os.path.join(destdir, 'test')
        out, err = system('gcc ' + temp_path + ' -o ' + x)
        if err:
            queue.send(task, err, 120)
        else:
            out1, err1 = system(x)
            if err1:
                queue.send(task, err1, 120)
            else:
                queue.send(task, out1, 120)

def system(cmd):
    """
    Invoke a shell command. Primary replacement for os.system calls.
    """
    ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    out, err = ret.communicate()
    return out, err


def writesource(name, content):
    destdir = tempfile.mkdtemp(suffix='.' + str(os.getpid()), dir=None)
    temp_path=os.path.join(destdir,name)
    f=open(temp_path,'w')
    f.write(content)
    f.close()
    return destdir
    
if __name__== '__main__':
    main()
