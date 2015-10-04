__author__ = 'andreasbotero'

token = {
    1: ('ADDOP', 'Add'),
    2: ('ADDOP', 'sub'),
    3: ('ADDOP', 'and'),
    4: ('ADDOP', 'or')

}


def addop(line, forward_point):
    current_char = line[forward_point]
    word = ""
    if current_char is '+':
        forward_point += 1
        return True, forward_point, token[1]
    if current_char is '-':
        forward_point += 1
        return True, forward_point, token[2]
    elif current_char.isalpha():
        while current_char.isalpha():
            forward_point += 1
            word += current_char
        if word is 'or':
            return True, forward_point, token[4]
        if word is 'and':
            return True, forward_point, token[3]
        return False, forward_point, None
