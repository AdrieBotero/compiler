__author__ = 'andreasbotero'

from StateMachines.IDMachine import id_machine
from StateMachines.INTMachine import int_machine
from StateMachines.LONGREALMachine import long_real_machine
from StateMachines.REALMachine import real_machine
from StateMachines.RELOPMachine import relop_machine
from StateMachines.WhiteSpaceMachine import white_space_machine

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


def read_lines():
    file_name = open('read_it', 'r')
    file_write_to = open("write_it.txt", "w")
    print file_name
    # set limit for character in line
    char_limit = 72
    # counter for line numbers
    counter = 1
    # parse file
    for line in file_name:
        char = len(line)
        file_write_to.writelines("{0}\t{1}".format(counter, line))
        # Check line characters
        # if characters limits is bigger than 72 then it will display error
        if char > char_limit:
            file_write_to.writelines("character limit exceeded\n")
            print "character limit exceeded"
            # pass data to machines of machines
            # print machines_of_machines(char)
        counter += 1
    file_write_to.close()
    file_name.close()
    # print file_name.readline()


def machines_of_machines(file_to_analyze):
    token_file = open('write_it.txt', "w")
    list_file = open('list_file', 'w')
    # write properties of the data into file
    table_template = "{0:8}|{1:16}|{2:16}|{3:7}\n"  # Columns for table
    token_file.write(table_template.format('Line No.', 'Lexeme', 'Token-Type', 'Attribute'))
    # token_file.write('{Line No.\tLexeme\tToken-Type\tAttribute\n')
    line_number = 0
    errors = []
    for line in file_to_analyze:
        line_number += 1
        l = line
        fp = 0
        list_file.writelines("{0}\t\t{1}".format(line_number, l))  # write lines to list file
        # we are going to run the through the machines
        while fp < len(l):
            while True:
                success, temp_fp, token = id_machine(l, fp)  # get status, pointer and token of id machine
                t = token
                try:
                    temp_list = list(t)
                except TypeError:
                    pass
                current_word = temp_list[1]
                current_errors = temp_list[2]

                # list_file.writelines("LEXERR: {0}: {1}\n".format(','.join(line_errors), current_word))
                # check if current word is a reserve word
                if current_word in open('reserved_words').read():
                    # set temp variable for
                    temp_list[0] = "14 REV"
                    token = tuple(temp_list)

                if success:
                    # write to the token file
                    if current_errors:
                        list_file.writelines("LEXERR: {0}: {1}\n".format(','.join(current_errors), current_word))
                    token_file.writelines(table_template.format(line_number, token[1], token[0], ','.join(current_errors)))
                    fp = temp_fp
                    for i in token:
                        print i
                    break
                success, temp_fp = white_space_machine(l, fp)
                if success:
                    fp = temp_fp
                    break
                success, temp_fp, token = long_real_machine(l, fp)
                t = token
                try:
                    temp_list = list(t)
                except TypeError:
                    pass
                current_word = temp_list[1]
                current_errors = temp_list[2]
                if success:
                    if current_errors:
                        list_file.writelines("LEXERR: {0}: {1}\n".format(','.join(current_errors), current_word))
                    token_file.writelines(table_template.format(line_number, token[1], token[0], ','.join(current_errors)))
                    fp = temp_fp
                    for i in token:
                        print i
                    break
                success, temp_fp, token = real_machine(l, fp)
                t = token
                try:
                    temp_list = list(t)
                except TypeError:
                    pass
                current_word = temp_list[1]
                current_errors = temp_list[2]
                if success:
                    if current_errors:
                        list_file.writelines("LEXERR: {0}: {1}\n".format(','.join(current_errors), current_word))
                    token_file.writelines(table_template.format(line_number, token[1], token[0], ','.join(current_errors)))
                    fp = temp_fp
                    for i in token:
                        print i
                    break
                success, temp_fp, token = int_machine(l, fp)
                t = token
                try:
                    temp_list = list(t)
                except TypeError:
                    pass
                current_word = temp_list[1]
                current_errors = temp_list[2]
                if success:
                    if current_errors:
                        list_file.writelines("LEXERR: {0}: {1}\n".format(','.join(current_errors), current_word))
                    token_file.writelines(table_template.format(line_number, token[1], token[0], ','.join(current_errors)))
                    fp = temp_fp
                    for i in token:
                        print i
                    break
                success, temp_fp, token = relop_machine(l, fp)
                if success:
                    fp = temp_fp
                    for i in token:
                        print i
                    break
    token_file.close()  # close token file.
    list_file.close()  # close list file
