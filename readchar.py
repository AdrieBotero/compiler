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
    11: "Unrecognized Symbol"
}

tokens = {
    1: ('RELOP', 'LE'),
    2: ('RELOP', 'NE'),
    3: ('RELOP', 'LT'),
    4: ('RELOP', 'EQ'),
    5: ('RELOP', 'GE'),
    6: ('RELOP', 'GT'),
}

# global pointers

# forward_p = 0
# back_p = 0


def main():
    # **Error Array**

    # read_lines()

    #machines_of_machines("var 123 2.34E+5", 0)
    #long_real_machine("2.34E+5", 0)

    print int_machine("12d", 0)


def get_next_token():
    return 0

def real_machine(line, forward_p):
    error = []  # on here we are going to store every error we get
    xx_counter = 0  # counter for xx
    yy_counter = 0  # counter for yy

    current_char = line[forward_p] # current didigit

    # check if first character is a digit
    

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
        print current_character + " is a letter or digit"
        # add characters
        forward_p += 1  # then we increment pointer to get next character
        try:
            current_character = string_line[forward_p]  # get next character in the string
        except IndexError:
            break
    print word
    return True, forward_p, ('ID', word)  # return data back to check next character


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
        if current_char is '0' and line[forward_p+1].isdigit():
            error.append(error_list.get(3))
        while current_char.isdigit():
            # add 1 to char_max to counter
            char_max += 1
            # add character to string
            my_string += current_char
            # check the max of character
            if char_max > 10 and error_list.get(2) not in error:
                error.append(error_list.get(2))  # if number are over max then we append error
            # get next character
            forward_p += 1
            try:
                current_char = line[forward_p]
            except IndexError:
                break

        return True, forward_p, ('INT', my_string, error)
    else:  # else we need to return an error with what kind of things
        return False, forward_p


def machines_of_machines(line, forward_p):
    l = line
    fp = forward_p
    bp = 0
    # we are going to run the through the machines
    while forward_p < len(l):
        while True:
            success, temp_fp, token = id_machine(l, fp)  # get status, pointer and token of id machine
            if success:
                bp = temp_fp
                fp = temp_fp
                for i in token:
                    print i
                break
            success, temp_fp = white_space_machine(l, fp)
            if success:
                bp = temp_fp
                fp = temp_fp
                for i in token:
                    print i
                break
            success, temp_fp = long_real_machine(l, fp)
            if success:
                bp = temp_fp
                fp = temp_fp
                for i in token:
                    print i
                break


def white_space_machine(line, forward_p):
    # check if white space tab or new line exist in current character
    current_character = line[forward_p]  # get current character
    if current_character is not ' ' or current_character is not '\t' or current_character is not '\n':
        return False, None
    while current_character is ' ' or current_character is '\t' or current_character is '\n':
        # increment forward pointer
        forward_p += 1
        current_character = line[forward_p]
    return True, forward_p


def long_real_machine(line, forward_p):
    # work on this next time
    print line
    current_char = line[forward_p]  # get current character
    print current_char
    string_to_return = ""
    counter_xx = 0  # this will keep characters count
    counter_yy = 0  # yy counter
    counter_zz = 0  # zz counter
    error = []  # error array
    # check for zeros
    # if current char is zero then we
    if current_char is 0 and line[forward_p + 1].isdigit():  # if current char is a 0 and the next char is a digit
        return False
    while current_char.isdigit():  # while we have a digit
        counter_xx += 1  # we increment the counter for xx
        string_to_return += current_char  # we add current char to the string
        forward_p += 1
        current_char = line[forward_p]  # get next character
        print "checking current character " + current_char
    if current_char == '.' and line[forward_p + 1].isdigit():  # checking for dot and next character
        forward_p += 1
        string_to_return += current_char  # we get next character
        print "string return is " + string_to_return
        current_char = line[forward_p]
        print "next char is " + current_char
        while current_char.isdigit():
            string_to_return += current_char
            counter_yy += 1
            forward_p += 1
            current_char = line[forward_p]
            print string_to_return
        print "next character " + current_char
        if current_char is 'E' and line[forward_p + 1].isdigit() or current_char is 'E' and \
                line[forward_p + 1] == '+' or current_char is 'E' and line[forward_p + 1] == '-':
            #  add char to place holder
            string_to_return += current_char
            counter_zz += 1
            forward_p += 1
            current_char = line[forward_p]
            print 'after E ' + current_char
            while current_char.isdigit() or current_char == '+' or current_char == '-':
                string_to_return += current_char
                print "string return " + string_to_return
                counter_zz += 1
                forward_p += 1
                try:
                    current_char = line[forward_p]
                except IndexError:
                    break
            return True, forward_p, ('LONG_REAL', string_to_return)
        else:
            back_p = forward_p
            print "forward_point" + str(back_p)
    else:
        return False, None


def relop_machine(line, forward_p, back_p):
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
            return tokens[1], forward_p  # return ('RELOP', 'LE')
        elif character == ">":
            return tokens[2], forward_p  # return ('RELOP', 'NE')
        else:
            return tokens[3], forward_p - 1  # return ('RELOP', 'LT')
    if character == "=":
        return tokens[4]  # return ('RELOP', 'EQ')
    if character == ">":
        forward_p += 1
        character = l[forward_p]
        if character == "=":
            return tokens[5]  # return ('RELOP', 'GE')
        else:
            return tokens[6], forward_p  # return ('RELOP', 'GT')


def read_lines():
    file_name = open('read_it', 'r')
    file_write_to = open("write_it.txt", "w")
    # print file_name.read(10)
    print file_name
    # set limit for character in line
    char_limit = 72
    # counter for line numbers
    counter = 1
    # parse file
    for line in file_name:
        char = len(line)

        print line
        file_write_to.writelines("{0}\t{1}".format(counter, line))
        # Check line characters
        # if characters limits is bigger than 72 then it will display error
        if char > char_limit:
            file_write_to.writelines("character limit exceeded\n")
            print "character limit exceeded"
        counter += 1
    file_write_to.close()
    file_name.close()
    # print file_name.readline()


if __name__ == "__main__":
    main()
