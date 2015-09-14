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


def id_machine(string_line, forward_p):
    word = ""
    current_character = string_line[forward_p]  # get current character
    if not current_character.isalpha():
        # Return fail
        return False, None, None

    while current_character.isalpha() | current_character.isdigit():
        # store get next character and store is in character variable
        # check if character is a letter

        word += current_character
        # add characters
        forward_p += 1  # then we increment pointer to get next character
        try:
            current_character = string_line[forward_p]  # get next character in the string
        except IndexError:
            break
    return True, forward_p, ('ID', word)  # return data back to check next character
