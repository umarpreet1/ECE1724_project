import threading

class Node:
    def __init__(self,char,lock = 0):
        self.char = char
        self.lock_obj = threading.Lock()
        self.children = [None]*27

    def add_child(self,child):
        if child.char !='.':
            index = ord(child.char) - ord('a')
            self.children[index] = child
        else:
            self.children[-1] = child

    def get_child(self,char):
        if char !='.':
            index = ord(char) - ord('a')
            return self.children[index]
        else:
            return self.children[-1]

    def lock(self):
        self.lock_obj.acquire()

    def unlock(self):
        self.lock_obj.release()

    def is_locked(self):
        return self.lock_obj.locked()


class BaseTrie:
    def __init__(self):
        self.head = Node('.')

    def get_lock(self,key):
        current  = self.head
        for k in key[:-1]:
            child = current.get_child(k)
            if child == None:
                child = Node(k)
                current.add_child(child)
            current = child

        destination = current.get_child(key[-1])
        if destination == None:
            child = Node(key[-1])
            current.add_child(child)
            return child
        else:
            return destination

    def get_node(self,key):
        current = self.head
        for k in key[:-1]:
            child = current.get_child(k)
            if child == None:
                return ''
            current = child

        destination = current.get_child(key[-1])
        if destination == None:
            return ''
        else:
            return destination.info
