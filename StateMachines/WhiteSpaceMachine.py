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


def white_space_machine(line, forward_p):
    # check if white space tab or new line exist in current character
    current_character = line[forward_p]  # get current character
    if current_character == ' ' or current_character == '\t' or current_character == '\n':
        while current_character == ' ' or current_character == '\t' or current_character == '\n':
            # increment forward pointer
            forward_p += 1
            try:
                current_character = line[forward_p]
            except IndexError:
                break
        return True, forward_p
    else:
        return False, None
