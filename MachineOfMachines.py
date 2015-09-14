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


def machines_of_machines(file_to_analyze):
    line_number = 0
    for line in file_to_analyze:
        line_number += 1
        l = line
        fp = 0
        # we are going to run the through the machines
        while fp < len(l):
            while True:
                success, temp_fp, token = id_machine(l, fp)  # get status, pointer and token of id machine
                if success:
                    fp = temp_fp
                    for i in token:
                        print i
                    break
                success, temp_fp = white_space_machine(l, fp)
                if success:
                    fp = temp_fp
                    break
                success, temp_fp, token = long_real_machine(l, fp)
                if success:
                    fp = temp_fp
                    for i in token:
                        print i
                    break
                success, temp_fp, token = real_machine(l, fp)
                if success:
                    fp = temp_fp
                    for i in token:
                        print i
                    break
                success, temp_fp, token = int_machine(l, fp)
                if success:
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
            print machines_of_machines(char, 0)
        counter += 1
    file_write_to.close()
    file_name.close()
    # print file_name.readline()