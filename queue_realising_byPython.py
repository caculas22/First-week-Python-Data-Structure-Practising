# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:50:54 2019

@author: caculas22
"""

class Queue(object):
    def __init__(self,limit=10):
        self.queue=[]          #初始化为空队列
        self.head=None         #队列头
        self.tail=None         #队列尾
        self.limit=limit       #队列容量
    def is_empty(self):
        return bool(self.queue)
    def enqueue(self,data):
        if not bool(self.queue):
            self.head=0
            self.tail=0
            self.queue.append(data)
        else:
            if len(self.queue)>=self.limit:
                print('Queue Overflow Error')
            else:
                self.tail+=1
                self.queue.append(data)
    def dequeue(self):
        if not bool(self.queue):
            raise IndexError('Dequeue from an empty queue')
        else:
            self.queue=self.queue[self.head+1:self.tail]
            self.head+=1
            