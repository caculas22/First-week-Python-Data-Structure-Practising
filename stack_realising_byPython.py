# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:50:57 2019

@author: caculas22
"""
class Stack(object):
    def __init__(self,limit=10):#默认的栈上限为10,初始化属性
        self.stack=[]          #以列表存放
        self.limit=limit       #栈容量极限
    def is_empty(self):        #判断栈是否为空
        return bool(self.stack)
    def top(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def push(self,data):
        if len(self.stack)<self.limit:
            self.stack.append(data)
        else:
            print('Stack Overflow Error')
            pass
    def pop(self):
        if self.stack:
            self.stack=self.stack[0:len(self.stack)-1]
        else:
            raise IndexError('Pop From an empty stack')
            
            