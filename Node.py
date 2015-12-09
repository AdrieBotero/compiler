__author__ = 'andreasbotero'


class Node:
    def __init__(self, data, w_type, next_node, previous_node):
        self.data = data
        self.w_type = w_type
        self.next_node = next_node
        self.previous_node = previous_node

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
