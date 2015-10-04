__author__ = 'andreasbotero'


token = {
    1: ('MULOP', 'Multiplication'),
    2: ('MULOP', 'Division'),
    3: ('MULOP', 'div'),
    4: ('MULOP', 'or'),
    5: ('MULOP', 'mod'),
    6: ('MULOP', 'and')

}


def mulup(line, forward_p):

    current_char = line[forward_p]
    word = ""
    if current_char is '*':
        forward_p += 1
        return True, forward_p, token[1]
    if current_char is '/':
        forward_p += 1
        return True, forward_p, token[2]
    if current_char.isalpha():
        while current_char.isalpha():
            forward_p += 1
            word += current_char
        if word is 'div':
            return True, forward_p, token[2]
        if word is 'mod':
            return True, forward_p, token[5]
        if word is 'and':
            return True, forward_p, token[6]
