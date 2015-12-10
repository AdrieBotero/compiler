__author__ = 'andreasbotero'


class Node:
    def __init__(self, i, w_type):
        self.i = i
        self.w_type = w_type
        self.next_node = None
        self.previous_node = None

    def __str__(self):
        return "testing nodes" + \
               self.i + self.w_type + str(id(self.next_node))

    def set_data(self, d):
        self.data = d

    def get_data(self):
        return self.data

    def set_type(self, t):
        self.w_type = t

    def get_type(self):
        return self.w_type

    def set_next_node(self, n):
        self.next_node = n

    def get_next_node(self):
        return self.next_node

    def set_previous_node(self):
        self.previous_node

    def get_previous_node(self):
        return self.previous_node
