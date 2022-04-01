
class Node:
    def __init__(self,char,info,lock = 0):
        self.char = char
        self.info = info
        self.lock = lock
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

    def update_info(self,info):
        self.info = info

    def lock(self):
        if self.lock ==0:
            self.lock = 1

    def unlock(self):
        self.lock = 0

    def is_locked(self):
        return self.lock


class BaseTrie:
    def __init__(self):
        self.head = Node('.','home')

    def add_node(self,key,info):
        current  = self.head
        for k in key[:-1]:
            child = current.get_child(k)
            if child == None:
                child = Node(k,'Unused')
                current.add_child(child)
            current = child

        destination = current.get_child(key[-1])
        if destination == None:
            child = Node(key[-1],info)
            current.add_child(child)
        else:
            destination.update_info(info)

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
