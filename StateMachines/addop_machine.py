__author__ = 'andreasbotero'

token = {
    1: ('ADDOP', 'Add', '+'),
    2: ('ADDOP', 'sub', '-'),
    3: ('ADDOP', 'or', 'or')

}


def addop(line, forward_point):
    current_char = line[forward_point]
    word = ""
    if current_char == '+':
        forward_point += 1
        return True, forward_point, token[1]
    if current_char == '-':
        forward_point += 1
        return True, forward_point, token[2]
    if current_char.isalpha():
        while current_char.isalpha():
            word += current_char
            forward_point += 1
            try:
                current_char = line[forward_point]
            except IndexError:
                break
        if word == 'or':
            return True, forward_point, token[3]
    return False, None, None
