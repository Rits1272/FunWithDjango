from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')


"""
QUE IMPLEMENTATION
"""
class Queue():

    def __init__(self):
        self.head = ''
        self.tail = ''
        self.arr = []

    def add(self, item):
        if len(self.arr) == 0:
            self.arr.append(item)
            self.head = 0
            self.tail = 0
        else:
            self.arr.append(item)
            self.tail+=1

    def delete(self):
        self.arr[self.head] = ''
        self.head += 1
        if len(self.arr) > 1:
            self.tail -= 1

    def clear(self):
        self.arr = []
        self.head = ''
        self.tail = ''

que = Queue()

def QueMethod(request):

    if request.method == 'GET':
        if request.GET.get('add-btn'):
            que.add(request.GET.get('add-btn'))
        elif request.GET.get('del-btn'):
            que.delete()
        elif request.GET.get('clear-btn'):
            que.clear()

    return render(request,'basic_app/queue.html',{'arr' : que.arr,
                                                 'head':que.head,
                                                 'tail':que.tail})

"""
STACK IMPLEMENTATION
"""

class Stack():

    def __init__(self):
        self.front = ''
        self.arr = []

    def add(self, item):
        if len(self.arr) == 0:
            self.arr.append(item)
            self.front = 0
        else:
            self.arr.append(item)
            self.front+=1

    def delete(self):
        self.arr.pop()
        if len(self.arr) ==  0:
            self.front = -1

    def clear(self):
        self.arr = []
        self.front = ''

stack = Stack()

def StackMethod(request):

    if request.method == 'GET':
        if request.GET.get('add-btn'):
            stack.add(request.GET.get('add-btn'))
        elif request.GET.get('del-btn'):
            stack.delete()
        elif request.GET.get('clear-btn'):
            stack.clear()

    return render(request,'basic_app/stack.html',{'arr' : stack.arr,
                                                 'front':stack.front,
                                                 })

"""
CIRCULAR QUE
"""
class CircularQueue():

    def __init__(self):
        self.size = 5
        self.head = ''
        self.tail = ''
        self.arr = []
        self.message = ''

    def add(self, item):
        if len(self.arr) == 0:
            self.arr.append(item)
            self.head = 0
            self.tail = 0

        elif self.tail < (self.size - 1) and self.arr[self.tail] != '' and len(self.arr) < self.size:
            self.arr.append(item)
            self.tail+=1

            if self.tail == (self.size-1):
                self.tail = 0

        else:
            if self.arr[self.tail] == '':
                self.arr[self.tail] = item
                self.tail += 1

            else:
                self.message = "Circular Que is Full"

    def delete(self):
        self.arr[self.head] = ''
        self.head += 1
        if self.head > (self.size-1):
            self.head = 0

    def clear(self):
        self.arr = []
        self.head = ''
        self.tail = ''
        self.message = ''

Cque = CircularQueue()

def CQueMethod(request):

    if request.method == 'GET':
        if request.GET.get('add-btn'):
            Cque.add(request.GET.get('add-btn'))
        elif request.GET.get('del-btn'):
            Cque.delete()
        elif request.GET.get('clear-btn'):
            Cque.clear()

    return render(request,'basic_app/cque.html',{'arr' : Cque.arr,
                                                 'head':Cque.head,
                                                 'tail':Cque.tail,
                                                 'message':Cque.message,
                                                 'size':Cque.size,}
                                                 )
