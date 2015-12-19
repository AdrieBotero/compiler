__author__ = 'andreasbotero'

# Cases to handle:
    #   (
    #   )
    #   .
    #   ..
    #   :=
    #   ;
    # ,
token = {
    1: ('CATCHALL', 'OPEN-PAR', '('),
    2: ('CATCHALL', 'CLOSE-PAR', ')'),
    3: ('CATCHALL', 'DOT', '.'),
    4: ('CATCHALL', 'D-DOT', '..'),
    5: ('CATHCALL', 'SINGOP', ':='),
    6: ('CATCHALL', 'TERMINATE', ';'),
    7: ('CATCHALL', 'COMMA', ','),
    8: ('Unrecog Symbol', '99 LEXERR'),
    9: ('CATCHALL', 'colon', ':'),
    10: ('CATCHALL', 'OPEN-BRA', '['),
    11: ('CATCHALL', 'CLOSE-BRA', ']')
}


def catch_all_machine(line, pointer):
    current_char = line[pointer]
    length = len(line)
    if current_char == '(':
        pointer += 1
        return True, pointer, token[1]
    elif current_char == ')':
        pointer += 1
        return True, pointer, token[2]
    elif current_char == '.':
        try:
            if line[pointer+1] == '.':
                pointer += 2
                return True, pointer, token[4]
            else:
                pointer += 1
                return True, pointer, token[3]
        except IndexError:
            pointer += 1
            return True, pointer, token[3]
    elif current_char == ':' and line[pointer + 1] == '=':
        pointer += 2
        return True, pointer, token[5]
    elif current_char == ':' and line[pointer + 1] != '=':
        pointer += 1
        return True, pointer, token[9]
    elif current_char == ';':
        pointer += 1
        return True, pointer, token[6]
    elif current_char == ',':
        pointer += 1
        return True, pointer, token[7]
    elif current_char == '[':
        pointer += 1
        return True, pointer, token[10]
    elif current_char == ']':
        pointer += 1
        return True, pointer, token[11]
    else:
        pointer += 1
        temp_list = list(token[8])
        temp_list.append(current_char)
        new_token = tuple(temp_list)
        return True, pointer, new_token
