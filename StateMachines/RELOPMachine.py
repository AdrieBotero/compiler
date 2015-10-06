__author__ = 'andreasbotero'

error_list = {
    1: "ID too long",
    2: "INT to long",
    3: "INT with leading zeros",
    4: "INT too long with leading zeros",
    5: "REAL xx too long",
    6: "REAL yy too long ",
    7: "REAL xx with leading zeros",
    8: "REAL yy with trailer",
    9: "LONGREAL zz too long",
    10: "LONGREAL zz with leading zero",
    11: "LONGREAL xx too Long",
    12: "LONGREAL xx with leading zero",
    13: "LONGREAL xx with trailer of zeros",
    14: "LONGREAL yy too long",
    15: "LONGREAL yy with leading zero",
    16: "Unrecognized Symbol",
    17: "LONGREAL yy with trailer of zeros"
}

tokens = {
    1: ('RELOP', 'LE', '<='),
    2: ('RELOP', 'NE', '<>'),
    3: ('RELOP', 'LT', '<'),
    4: ('RELOP', 'EQ', '='),
    5: ('RELOP', 'GE', '>='),
    6: ('RELOP', 'GT', '>'),
}


def relop_machine(line, forward_p):
    # current_char = line[forward_p]
    # if current_char is '<' and line[forward_p+1] is '=':
    #     forward_p += 1
    #     return True, forward_p, tokens[1]

    # store line
    l = line
    # get first char
    character = l[forward_p]
    if character == "<":
        # increment pointer
        forward_p += 1
        # get next character
        character = l[forward_p]
        if character == "=":
            forward_p += 1
            return True, forward_p, tokens[1]  # return ('RELOP', 'LE')
        elif character == ">":
            forward_p += 1
            return True, forward_p, tokens[2]  # return ('RELOP', 'NE')
        else:
            return True, forward_p, tokens[3],  # return ('RELOP', 'LT')
    elif character == "=":
        forward_p += 1
        return True, forward_p, tokens[4]  # return ('RELOP', 'EQ')
    elif character == ">":
        forward_p += 1
        character = l[forward_p]
        if character == "=":
            forward_p +=1
            return True, forward_p, tokens[5]  # return ('RELOP', 'GE')
        else:
            return True, forward_p, tokens[6]  # return ('RELOP', 'GT')
    else:
        return False, None, None
