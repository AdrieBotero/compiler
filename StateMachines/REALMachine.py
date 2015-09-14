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


def real_machine(line, forward_p):
    error = []  # on here we are going to store every error we get
    xx_counter = 0  # counter for xx
    yy_counter = 0  # counter for yy
    my_string = ""
    current_char = line[forward_p]  # current didigit
    # check for leading zero
    if current_char == '0' and line[forward_p + 1].isdigit():
        error.append(error_list.get(7))

    # check if first character is a digit
    if current_char.isdigit():
        while current_char.isdigit():
            # add char to string
            my_string += current_char
            # add one to xx counter
            xx_counter += 1
            forward_p += 1
            current_char = line[forward_p]
            if xx_counter > 5 and error_list.get(5) not in error:  # here we are checking if xx counter goes over limit
                error.append(error_list.get(5))  # if it does then we add error to the error array
            if current_char is '.':
                forward_p += 1  # increase pointer
                my_string += current_char  # add current character to the string
                # get next character
                # get the next character in the line
                current_char = line[forward_p]
                while current_char.isdigit():
                    # add 1 to the yy counter
                    yy_counter += 1
                    # add current char to the string
                    my_string += current_char
                    # increment pointer
                    forward_p += 1
                    if yy_counter > 5 and error_list.get(6) not in error:
                        error.append(error_list.get(6))  # if true then add error to array
                    try:
                        current_char = line[forward_p]
                    except IndexError:
                        break

                return True, forward_p, ('REAL', my_string, error)
        return False, None, None
    else:
        return False, None, None
