__author__ = 'andreasbotero'

token = {
    1: ('ADDOP', 'Add'),

}


def addop(line, forward_point):
    current_char = line[forward_point]
    word = ""
    if current_char is '+' or current_char is '-':
        forward_point += 1
        return True, forward_point, token[1]
    elif current_char.isalpha():
        while current_char.isalpha():
            forward_point += 1
            word += current_char
        if word is 'or' or word is 'and':
            return True, forward_point, token[1]
        return False, forward_point, None