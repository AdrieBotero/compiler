__author__ = 'andreasbotero'

error_list = {
    0: "NULL",
    1: "Buffer size too long",
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
    17: "LONGREAL yy with trailer of zeros",
    18: "ID too long"
}


# open file  and load it into a datastructure


def id_machine(string_line, forward_p):
    error = []
    # open file of reserve words

    word = ""
    current_character = string_line[forward_p]  # get current character
    if not current_character.isalpha():
        # Return fail
        return False, None, None

    while current_character.isalpha() | current_character.isdigit():
        # store get next character and store is in character variable
        # character limit
        word += current_character
        if len(word) > 10 and error_list.get(18) not in error:  # check if character limit is more than 10
            key = '18'
            error_string = error_list.get(18)
            error.append(key+" "+error_string)
        # add characters
        forward_p += 1  # then we increment pointer to get next character
        try:
            current_character = string_line[forward_p]  # get next character in the string
        except IndexError:
            break
    # if len(string_line) > 72 and error_list.get(1) not in error:
    #     error.append(error_list.get(1))
    if not error:
        error.append("0 " + error_list.get(0))
    return True, forward_p, ('10 ID', word, error)  # return data back to check next character

