__author__ = 'andreasbotero'

error_list = {
    0: "NULL",
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


def long_real_machine(line, forward_p):
    # work on this next time
    back_pointer = forward_p
    current_char = line[forward_p]  # get current character
    string_to_return = ""
    counter_xx = 0  # this will keep characters count
    counter_yy = 0  # yy counter
    counter_zz = 0  # zz counter
    error = []  # error array
    # check for zeros
    # if current char is zero then we
    if current_char is '0' and line[forward_p + 1].isdigit():  # if current char is a 0 and the next char is a digit
        key = '12'
        error_string = error_list.get(12)
        error.append(key + " " + error_string)
    if current_char.isdigit():
        while current_char.isdigit():  # while we have a digit
            counter_xx += 1  # we increment the counter for xx
            string_to_return += current_char  # we add current char to the string
            forward_p += 1
            current_char = line[forward_p]  # get next character
            if counter_xx > 5 and ('11 ' + error_list.get(11)) not in error: # check for limit of xx
                key = '11'
                error_string = error_list.get(11)
                error.append(key + " " + error_string)  # if true then add error to array
            if current_char is '0' and line[forward_p + 1] is '0':
                error.append(error_list.get(13))
            if current_char == '.' and line[forward_p + 1].isdigit():  # checking for dot and next character
                forward_p += 1
                string_to_return += current_char  # we get next character
                current_char = line[forward_p]
                while current_char.isdigit():
                    string_to_return += current_char
                    counter_yy += 1
                    forward_p += 1
                    if counter_yy > 5 and ('14 ' + error_list.get(14)) not in error:
                        key = '14'
                        error_string = error_list.get(14)
                        error.append(key + " " + error_string)
                    if current_char is '0' and line[forward_p+1] is '0':
                        error.append(error_list.get(17))
                    try:
                        current_char = line[forward_p]
                    except IndexError:
                        break

                if current_char == 'E':
                    string_to_return += current_char
                    forward_p += 1
                    current_char = line[forward_p]
                    if current_char == '+' or current_char == '-':
                        string_to_return += current_char
                        forward_p += 1
                        current_char = line[forward_p]
                    if current_char.isdigit():
                        #  add char to place holder
                        # string_to_return += current_char
                        # counter_zz += 1
                        # forward_p += 1
                        # current_char = line[forward_p]
                        while current_char.isdigit():
                            string_to_return += current_char
                            counter_zz += 1
                            if current_char is '+' or current_char is '-':
                                counter_zz -= 1
                            forward_p += 1
                            if counter_zz > 2 and ('9 ' + error_list.get(9)) not in error_list:  # fix this if
                                key = '9'
                                error_string = error_list.get(9)
                                error.append(key + " " + error_string)
                            try:
                                current_char = line[forward_p]
                            except IndexError:
                                break
                        if not error:
                            error.append("0 " + error_list.get(0))
                        return True, forward_p, ('12 LONG_REAL', string_to_return, error)
                    else:
                        return False, None, None
    return False, None, None
