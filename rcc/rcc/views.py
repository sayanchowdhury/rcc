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
        return HttpResponse(json.dumps({'error':'Invalid filename'}),
                            content_type="application/json")

    if text is False:
        return HttpResponse(json.dumps({'error':'Empty file'}),
                            content_type="application/json")

    try:
        queue = Queue('rcc')
        queue.connect()
        task = Task({'filename':filename, 'text':text})
        job = queue.enqueue(task)
    except:
        return HttpResponse(json.dumps({'error':'Error creating Job'}),
                            content_type="application/json")

    while True:
        if job.result is None:
            continue
        break

    return HttpResponse(json.dumps({'status' : 'Job Created',
                                    'output' : job.result}),
                        content_type="application/json")
