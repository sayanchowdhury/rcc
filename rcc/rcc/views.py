from django.http import HttpResponse
from retask.task import Task
from retask.queue import Queue

import json

def compile(request):
    """
    Enqueue the task to Queue
    """
    filename = request.POST.get('filename', False)
    text = request.POST.get('text', False)

    if filename is False:
        return HttpResponse(json.dumps({'error':'Invalid filename'}))

    if text is False:
        return HttpResponse(json.dumps({'error':'Empty file'}))

    try:
        queue = Queue('test')
        queue.connect()
        task = Task({'filename':filename, 'text':text})
        job = queue.enqueue(task)
    except:
        return HttpResponse(json.dumps({'error':'Error creating Job'}))

    return HttpResponse(json.dumps({'status':'Job Created'}))
