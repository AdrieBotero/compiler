__author__ = 'andreasbotero'


class Node:
    def __init__(self, data, w_type):
        self.data = data
        self.w_type = w_type
        self.parent = None
        self.right_sibling = None
        self.left_child = None
        self.previous_node = None

    def __str__(self):
        return "testing nodes " + \
               self.data + " " + self.w_type + " " + str(id(self.left_child))

    def set_data(self, d):
        self.data = d

    def get_data(self):
        return self.data

    def set_type(self, t):
        self.w_type = t

    def get_type(self):
        return self.w_type

    def set_previous_node(self):
        return self.previous_node

    def get_previous_node(self):
        return self.previous_node
