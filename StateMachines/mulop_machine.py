__author__ = 'andreasbotero'


token = {
    1: ('MULOP', 'Multiplication', '*'),
    2: ('MULOP', 'Division', '/'),
    3: ('MULOP', 'DIV', 'div'),
    4: ('MULOP', 'OR', 'or'),
    5: ('MULOP', 'MOD', 'mod'),
    6: ('MULOP', 'AND', 'and')

}


def mulop(line, forward_p):

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
            word += current_char
            forward_p += 1
            try:
                current_char = line[forward_p]
            except IndexError:
                break
        if word == 'div':
            return True, forward_p, token[3]
        if word == 'mod':
            return True, forward_p, token[5]
        if word == 'and':
            return True, forward_p, token[6]
    return False, None, None