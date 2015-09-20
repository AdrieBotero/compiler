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
    17: "LONGREAL yy with trailer of zeros",
    18: "INT with trailing of zeros"
}


def int_machine(line, forward_p):
    error = []  # append everything that is wrong with line
    char_max = 0  # counter for characters
    my_string = ""
    # get current character
    current_char = line[forward_p]
    # check if current char is a digit
    if current_char.isdigit():
        # if current char is a digit then we continue
        # check for leading zero
        if current_char is '0' and line[forward_p + 1].isdigit():
            error.append(error_list.get(3))
        while current_char.isdigit():
            # add 1 to char_max to counter
            char_max += 1
            # add character to string
            my_string += current_char
            # check the max of character
            if char_max > 10 and error_list.get(2) not in error:
                # get key of dic.
                error.append(error_list.get(2))  # if number are over max then we append error
            # get next character
            if current_char is '0' and line[forward_p + 1] is '0' and error_list.get(18) not in error:
                error.append(error_list.get(18))
            forward_p += 1
            try:
                current_char = line[forward_p]
            except IndexError:
                break

        return True, forward_p, ('11 INT', my_string, error)
    else:  # else we need to return an error with what kind of things
        return False, forward_p, None
