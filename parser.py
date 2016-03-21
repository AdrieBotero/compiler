__author__ = 'andreasbotero'
import sys

from GreenNode import GreenNode

from BlueNode import BlueNode

from Node import Node

tokens = []
nodes = []
synch_set = []
syntax_er = []
new_list_file = {}
# list_file = open('list_file', 'w')
lex_analysis_listing_file = open('list_file', 'r')
variable_types = {}
bo_flag = ''
bool_flag = []
memory_counter = 0
line_number = None

def add_tokens():
    with open('write_it.txt', 'r') as token_file:
        next(token_file)
        for line in token_file:
            tokens.append(line.replace(' ', '').split('|'))
    # for item in tokens:
    #     print item
    last_line = 0
    checking = new_list_file
    for line in lex_analysis_listing_file:
        if line[0].isdigit():
            new_list_file[int(line.split('\t')[0])] = [line]
            last_line = int(line.split('\t')[0])
        else:
            new_list_file[str(last_line)].append(line)


def get_line_number():
    token = tokens[0]
    return token[0]


def peek_token():
    token = tokens[0]
    # line_number = token[0]
    conversion = {
        '14REV': token[1],
        '10ID': 'id',
        'COMMA': token[1],
        'CLOSE-PAR': token[1],
        'TERMINATE': token[1],
        'OPEN-PAR': token[1],
        'colon': token[1],
        '11INT': 'integer',
        'SINGOP': 'assignop',
        'DOT': token[1],
        'ADDOP': 'addop',
        'MULOP': 'mulop',
        'RELOP': 'relop',
        'D-DOT': token[1],
        'EOF': '$',
        '13REAL': 'real',
        '99LEXERR': 'LEXERR',
        'OPEN-BRA': token[1],
        'CLOSE-BRA': token[1]
    }
    return conversion[token[2]]


def get_token():
    try:
        return tokens.pop(0)
    except IndexError:
        return False


def finish():
    print 'PARSE COMPLETE'
    write_new_listing_file()
    sys.exit(0)


def match(expect_token):
    global line_number
    if expect_token == 'num':
        expected_tokens = ['integer', 'real']
        peek = peek_token()
        if peek in expected_tokens:
            if peek != '$':
                get_token()
            else:
                finish()
        else:
            syntax_error(peek, expected_tokens)
    else:
        peek = peek_token()
        if peek == expect_token and peek != '$':
            get_token()
        elif peek == expect_token and peek == '$':
            finish()
        elif peek != expect_token:
            syntax_error(peek, expect_token)


# green_node = GreenNode("dummy", 'Sometype')
# print green_node
# green_node2 = GreenNode("dummy2", 'Sometype2')
# green_node3 = GreenNode("dummy3", 'Sometype3')
# green_node.next_node = green_node2
# green_node2.previous_node = green_node
# green_node2.next_node = green_node3
# green_node3.previous_node = green_node2
# while green_node is not None:
#     print green_node
#     green_node = green_node.get_next_node()


def parse():
    add_tokens()
    prg()
    # green_node_one = nodes[0]
    # node = green_node_one.right_sibling
    # green_node_two = nodes[1]
    # node_2 = green_node_two.right_sibling
    # for item in nodes:
    #     while item is not None:
    #         print item
    #         item = item.right_sibling
    match('$')
    write_new_listing_file()


def write_new_listing_file():
    new_file = open('final_listing_file.txt', 'w')
    for key in sorted(new_list_file):
        for line in new_list_file[key]:
            new_file.write(line + '\n')
    new_file.close()


def syntax_error(given_token, *expected):
    # line_number = get_line_number()
    global line_number
    # line_number = int(expected[-1])

    error = "Syntax Error: in line " + str(line_number) + " Expecting %s" % (expected,) + "received " + str(given_token)
    # syntax_er.append(error)
    new_list_file[int(line_number)].append(error)
    # print new_list_file
    print "Syntax Error: in line " + str(line_number) + " Expecting %s" % (expected,) + "received " + str(given_token)

    # get_token()
    if len(tokens) != 0:
        token = peek_token()
    else:
        finish()


# def handle_sync():
#     return synch_set


# green_node = GreenNode("dummy", 'Sometype')
# print green_node
# green_node2 = GreenNode("dummy2", 'Sometype2')
# green_node3 = GreenNode("dummy3", 'Sometype3')
# green_node.next_node = green_node2
# green_node2.previous_node = green_node
# green_node2.next_node = green_node3
# green_node3.previous_node = green_node2
# while green_node is not None:
#     print green_node
#     green_node = green_node.get_next_node()


def prg():
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == 'program':
        match('program')
        token = tokens[0]
        match('id')
        green_node = GreenNode(token[1], 'pname')
        green_node.previous_node = "root"
        nodes.insert(0, green_node)
        # print nodes
        match('(')
        idlist()
        match(')')
        match(';')
        prg_()
    else:
        del synch_set[:]
        synch_set.append('$')
        handle_sync()
        syntax_error(token, 'program')


def prg_():
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == 'begin':
        compstate()
        match('.')
    elif token == 'function':
        subprgdeclarations()
        compstate()
        match('.')
    elif token == 'var':
        declarations()
        prg__()
    else:
        del synch_set[:]
        synch_set.append('$')
        handle_sync()
        syntax_error(token, 'begin', 'function', 'var')


def prg__():
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == 'begin':
        compstate()
        match('.')
    elif token == 'function':
        subprgdeclarations()
        compstate()
        match('.')
    else:
        del synch_set[:]
        synch_set.append('$')
        handle_sync()
        syntax_error(token, 'begin', 'function')


def idlist():
    global line_number
    line_number = get_line_number()
    line = tokens[0]
    token = peek_token()
    if token == 'id':
        token = tokens[0]
        match('id')
        green_node = nodes[0]
        if green_node.right_sibling is None:
            green_node.right_sibling = BlueNode(token[1], "pname")
            nodes.insert(0, green_node.right_sibling)
        idlist_()
    else:
        del synch_set[:]
        synch_set.append(')')
        handle_sync()
        syntax_error(token, 'id')


def idlist_():
    global line_number
    line_number = get_line_number()
    line = tokens[0]
    token = peek_token()
    if token == ')':
        pass
    elif token == ',':
        match(',')
        token = tokens[0]
        match('id')
        green_node = nodes[0]
        while green_node.right_sibling is not None:
            green_node = green_node.right_sibling
        if green_node.right_sibling is None:
            green_node.right_sibling = BlueNode(token[1], "pname")
            nodes.insert(0, green_node.right_sibling)
        idlist_()
    else:
        del synch_set[:]
        synch_set.append(')')
        handle_sync()
        syntax_error(token, ')', ',')


def declarations():
    global line_number
    line_number = get_line_number()
    global synch_set
    line = tokens[0]

    token = peek_token()
    if token == 'var':
        match('var')
        token = tokens[0]
        match('id')
        match(':')
        the_type = type_()
        if type(the_type) is tuple:
            array_size = the_type[1]
            the_type = the_type[0]
        variable_types.update({token[1]: the_type})
        checking = nodes
        value_counter = 0
        if nodes:
            green_node = nodes[0]
            while green_node.right_sibling is not None:
                green_node = green_node.right_sibling
            if green_node.right_sibling is None:
                new_blue_node = BlueNode(token[1], the_type)
                memory_counter = 0
                new_blue_node.value = memory_counter
                if new_blue_node.w_type is 'integer':
                    memory_counter += 4
                elif new_blue_node.w_type is 'real':
                    memory_counter += 8
                elif new_blue_node.w_type == "a-real":
                    memory_counter += 8 * array_size
                elif new_blue_node.w_type == "a-integer":
                    memory_counter += 4 * array_size

                green_node.right_sibling = new_blue_node
                nodes.insert(0, green_node.right_sibling)
                write_to_memory_file('name', new_blue_node.data, new_blue_node.value)
        checking = nodes
        match(';')
        declarations_()
    else:
        # synch_set = ['function', 'begin']
        del synch_set[:]
        synch_set.append('var')
        synch_set.append('begin')
        synch_set.append('$')
        handle_sync()
        syntax_error(token, 'var', line_number)


def handle_sync():
    global synch_set
    line = tokens[0]
    checking = tokens
    token = peek_token()
    testing = synch_set
    while token not in synch_set:
        line = tokens[0]
        if tokens:
            get_token()
            token = peek_token()
        else:
            break


def declarations_():
    line = tokens[0]
    token = peek_token()
    array_size = 0
    global line_number
    line_number = get_line_number()
    global memory_counter
    if token == 'begin':
        pass
    elif token == 'function':
        pass
    elif token == 'var':
        match('var')
        token = tokens[0]
        match('id')
        match(':')
        the_type = type_()
        if type(the_type) is tuple:
            array_size = the_type[1]
            the_type = the_type[0]
        variable_types.update({token[1]: the_type})
        current_nodes = nodes
        if nodes:
            node = nodes[0]
            while node.right_sibling is not None:
                node = node.right_sibling
            if node.right_sibling is None:
                new_blue_node = BlueNode(token[1], the_type)
                new_blue_node.value = memory_counter
                if new_blue_node.w_type == 'integer':
                    memory_counter += 4
                elif new_blue_node.w_type == 'real':
                    memory_counter += 8
                elif new_blue_node.w_type == "a-real":
                    memory_counter += 8 * array_size
                elif new_blue_node.w_type == "a-integer":
                    memory_counter += 4 * array_size
                node.right_sibling = new_blue_node
                nodes.insert(0, node.right_sibling)
                write_to_memory_file('', new_blue_node.data, new_blue_node.value)
            testing = nodes
        match(';')
        declarations_()
    else:
        # synch_set = ['function', 'begin']
        del synch_set[:]
        synch_set.append('function')
        synch_set.append('begin')
        handle_sync()
        syntax_error(token, 'begin', 'function', 'var')


def type_():
    line = tokens[0]
    token = peek_token()
    test = peek_stack()
    global line_number
    line_number = get_line_number()
    if token == 'array':
        match('array')
        match('[')
        first_avalue = tokens[0][1]
        match('num')
        match('..')
        secon_value = tokens[0][1]
        match('num')
        match(']')
        match('of')
        current_type = standtype()
        array_size = (int(secon_value) - int(first_avalue)) + 1
        if current_type == "integer":
            return "a-integer", array_size
        else:
            return "a-real", array_size
    elif token == 'integer':
        current_type = standtype()
        if current_type == 'a-integer':
            return current_type
        else:
            return 'integer'
    elif token == 'real':
        current_type = standtype()
        if current_type == 'a-real':
            return current_type
        else:
            return 'real'

    else:
        del synch_set[:]
        synch_set.append(';')
        synch_set.append(')')
        handle_sync()
        syntax_error(token, 'array', 'integer', 'real')


def standtype():
    line = tokens[0]
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'integer':
        match('integer')
        return "integer"
    elif token == 'real':
        match('real')
        return "real"
    else:
        del synch_set[:]
        synch_set.append(';')
        synch_set.append(')')
        handle_sync()
        syntax_error(token, 'integer', 'real')


def subprgdeclarations():
    line = tokens[0]
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == 'function':
        subprgdeclaration()
        match(';')
        subprgdeclarations_()
    else:
        del synch_set[:]
        synch_set.append('begin')
        handle_sync()
        syntax_error(token, 'function')


def subprgdeclarations_():
    line = tokens[0]
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'begin':
        pass
    elif token == 'function':
        subprgdeclaration()
        match(';')
        subprgdeclarations_()
    else:
        del synch_set[:]
        synch_set.append('begin')
        handle_sync()
        syntax_error(token, 'begin', 'function')


def subprgdeclaration():
    line = tokens[0]
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'function':
        var_type = subprghead()
        subprgdeclaration_()
        return var_type
    else:
        del synch_set[:]
        synch_set.append(';')
        handle_sync()
        syntax_error(token, 'function')


def subprgdeclaration_():
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'begin':
        compstate()
    elif token == 'function':
        declarations()
        subprgdeclaration__()
    elif token == 'var':
        declarations()
        subprgdeclaration__()
    else:
        del synch_set[:]
        synch_set.append(';')
        handle_sync()
        syntax_error(token, 'begin', 'function', 'var')


def subprgdeclaration__():
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == 'begin':
        compstate()
    elif token == 'function':
        subprgdeclarations()
        compstate()
    else:
        del synch_set[:]
        synch_set.append(';')
        handle_sync()
        syntax_error(token, 'begin', 'function')


def subprghead():
    line = tokens[0]
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'function':
        match('function')
        line = tokens[0]
        match('id')
        # var_type = subprghead_()
        test = nodes
        node = nodes[0]

        green_node = GreenNode(line[1], "temptype")

        node.left_child = green_node
        nodes.insert(0, green_node)
        var_type = subprghead_()
        green_node.return_type = var_type
        variable_types.update({line[1]: var_type})
        return var_type
    else:
        # synch_set = ['function', 'begin', 'var']
        del synch_set[:]
        synch_set.append('function')
        synch_set.append('begin')
        synch_set.append('var')
        handle_sync()
        syntax_error(token, 'function')


def subprghead_():
    line = tokens[0]
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == '(':
        arguments()
        match(':')
        var_type = standtype()
        match(';')
        return var_type
    elif token == ':':
        match(':')
        var_type = standtype()
        match(';')
        return var_type
    else:
        my_set = ['function', 'begin', 'var']
        del synch_set[:]
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, '(', ':')


def arguments():
    line = tokens[0]
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == '(':
        match('(')
        paramlist()
        match(')')
    else:
        del synch_set[:]
        synch_set.append(':')
        handle_sync()
        syntax_error(token, '(')


def paramlist():
    line = tokens[0]
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'id':
        token = tokens[0]
        lexeme = token[1]
        match('id')
        match(':')
        my_type = type_()
        if type(my_type) is tuple:
            my_type = my_type[0]
        # token = tokens[0]
        variable_types.update({token[1]: my_type})
        check_nodes = nodes
        if nodes:
            node = nodes[0]
            while node.right_sibling is not None:
                node = node.right_sibling
            if node.right_sibling is None:
                node.right_sibling = BlueNode(token[1], my_type)
                nodes.insert(0, node.right_sibling)
        paramlist_()
    else:
        del synch_set[:]
        synch_set.append(')')
        handle_sync()
        syntax_error(token, 'id')


def paramlist_():
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == ')':
        pass
    elif token == ';':
        match(';')
        token = tokens[0]
        match('id')
        match(':')
        my_type = type_()
        if type(my_type) is tuple:
            my_type = my_type[0]
        variable_types.update({token[1]: my_type})
        if nodes:
            node = nodes[0]
            while node.right_sibling is not None:
                node = node.right_sibling
            if node.right_sibling is None:
                node.right_sibling = BlueNode(token[1], my_type)
                nodes.insert(0, node.right_sibling)
        paramlist_()
    else:
        del synch_set[:]
        synch_set.append(')')
        handle_sync()
        syntax_error(token, '(', ';')


def compstate():
    my_stack = nodes
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == 'begin':
        match('begin')
        compstate_()
    else:
        del synch_set[:]
        my_set = [';', 'end', '.']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, 'begin')


def check_scope(token, line):
    stack = nodes
    in_stack = any(i.data == token for i in stack)
    if not in_stack:
        print "Scope Error: Out of scope Line number " + line + " for " + token
        error = "Scope Error: Out of scope Line number " + line + " for " + token
        new_list_file[int(line_number)].append(error)


def write_to_memory_file(fun, v, a):
    memory_file = open('memory_file.', 'a')
    if fun is not None:
        memory_file.write(str(fun) + '\n')
    memory_file.write(str(v) + "      " + str(a) + '\n')


def set_function_name():
    green_node = nodes[0].__class__.__name__
    green_node_type = nodes[0].w_type
    if (green_node is 'GreenNode' and green_node_type is 'temptype') or (
                    green_node is 'GreenNode' and green_node_type is 'pname'):
        fun_name = nodes[0].data
        return fun_name


def update_memory_counter():
    global memory_counter
    if nodes[1].w_type is 'real':
        memory_counter += 8
        return memory_counter
    if nodes[1].w_type is 'integer':
        memory_counter += 4
        return memory_counter


def compstate_():
    global memory_counter
    global line_number
    line_number = get_line_number()
    line = tokens[0]

    token = peek_token()
    testing_node = nodes
    if token == 'begin':

        optionalstate()
        my_node = nodes
        match('end')
        if nodes[0].__class__.__name__ is 'GreenNode':
            # pop till next green node
            nodes.pop(0)
            while nodes[0].__class__.__name__ is 'BlueNode':
                nodes.pop(0)
        if nodes[0].__class__.__name__ is 'BlueNode':
            while nodes[0].__class__.__name__ is 'BlueNode':
                nodes.pop(0)
        check = nodes
    elif token == 'end':
        my_node = nodes
        match('end')
        if nodes[0].__class__.__name__ is 'GreenNode':
            # pop till next green node
            nodes.pop(0)
            while nodes[0].__class__.__name__ is 'BlueNode':
                nodes.pop(0)
        if nodes[0].__class__.__name__ is 'BlueNode':
            while nodes[0].__class__.__name__ is 'BlueNode':
                nodes.pop(0)
        check = nodes
    elif token == 'id':
        check_scope(line[1], line_number)
        my_node = nodes
        optionalstate()
        match('end')
        if nodes[0].__class__.__name__ is 'GreenNode':
            if nodes[1].__class__.__name__ is not 'GreenNode':

                # set func name
                # func = set_function_name()
                # # update_memory counter
                # if func is not None:
                #     memory_counter = 0
                #
                # a = memory_counter
                # # set variable
                # # setting variable but checking
                #
                # if nodes[0].__class__.__name__ is 'GreenNode':
                #     v = nodes[1].data
                # else:
                #     v = nodes[0].data
                #
                # # write everything to file.
                # write_to_memory_file(func, v, a)
                # update_memory_counter()
                # pop current node
                nodes.pop(0)
                while nodes[0].__class__.__name__ is 'BlueNode':
                    # write_to_memory_file(fun, v, a)
                    # set func name
                    # func = set_function_name()
                    # # update_memory counter
                    # if func is not None:
                    #     memory_counter = 0
                    # a = memory_counter
                    # # set variable
                    # # setting variable but checking
                    #
                    # if nodes[0].__class__.__name__ is 'GreenNode':
                    #     v = nodes[1].data
                    # else:
                    #     v = nodes[0].data
                    #
                    # # write everything to file.
                    # write_to_memory_file(func, v, a)
                    # update_memory_counter()
                    nodes.pop(0)
            elif nodes[1].__class__.__name__ is 'GreenNode':
                # write_to_memory_file(fun, v, a)
                nodes.pop(1)

        if nodes[0].__class__.__name__ is 'BlueNode':
            while nodes[0].__class__.__name__ is 'BlueNode':
                # write_to_memory_file(fun, v, a)
                # set func name
                # func = set_function_name()
                # # update_memory counter
                # if func is not None:
                #     memory_counter = 0
                # a = memory_counter
                # # set variable
                # # setting variable but checking
                # if nodes[0].__class__.__name__ is 'GreenNode':
                #     v = nodes[1].data
                # else:
                #     v = nodes[0].data
                # # write everything to file.
                # write_to_memory_file(func, v, a)
                # update_memory_counter()
                nodes.pop(0)
        check = nodes

    elif token == 'if':
        optionalstate()
        my_node = nodes
        match('end')
    elif token == 'while':
        optionalstate()
        my_node = nodes
        match('end')

    else:
        del synch_set[:]
        my_set = [';', 'end', '.', 'else']
        for i in my_set:
            synch_set.append(i)

        handle_sync()
        syntax_error(token, 'begin', 'end', 'id', 'if', 'while')


def optionalstate():
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'begin':
        statementlist()
    elif token == 'id':
        statementlist()
    elif token == 'if':
        statementlist()
    elif token == 'while':
        statementlist()
    else:
        del synch_set[:]
        synch_set.append('end')
        handle_sync()
        syntax_error(token, 'begin', 'id', 'if', 'while')


def statementlist():
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == 'begin':
        statement()
        statementlist_()
    elif token == 'id':
        statement()
        statementlist_()
    elif token == 'if':
        statement()
        statementlist_()
    elif token == 'while':
        statement()
        statementlist_()
    else:
        del synch_set[:]
        synch_set.append('end')
        handle_sync()
        syntax_error(token, 'begin', 'id', 'if', 'while')


def statementlist_():
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == ';':
        match(';')
        statement()
        statementlist_()
    elif token == 'end':
        pass
    else:
        del synch_set[:]
        synch_set.append('end')
        handle_sync()
        syntax_error(token, ';', 'end')


def assignop_error(line, v, e):
    print "Assignop Error in line " + str(line) + ": You are trying to assign a " + str(v) + " with an " + str(e)
    error = "Assignop Error in line " + str(line) + ": You are trying to assign a " + str(v) + " with an " + str(e)
    new_list_file[int(line)].append(error)


def statement():
    line = tokens[0]
    node = nodes[0]
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == 'begin':
        compstate()
    elif token == 'id':
        variable_type = variable()
        match('assignop')
        var_type = expression()
        if variable_type == 'a-integer':
            variable_type = 'integer'
        elif variable_type == 'a-real':
            variable_type = 'real'
        if var_type == 'a-integer':
            var_type = 'integer'
        elif var_type == 'a-real':
            var_type = 'real'
        if variable_type != var_type:
            assignop_error(line_number, variable_type, var_type)
            bool_flag.append('false')
        else:
            bool_flag.append('true')
    elif token == 'if':
        match('if')
        var_type = expression()
        match('then')
        statement()
        statement_()
    elif token == 'while':
        match('while')
        var_type = expression()
        match('do')
        statement()
    else:
        del synch_set[:]
        my_set = ['else', ';', 'end']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, 'begin', 'id', 'assignop', 'if', 'while')


def statement_():
    global line_number
    line_number = get_line_number()
    token = peek_token()

    if token == ';':
        pass
    elif token == 'else':
        match('else')
        statement()
    elif token == 'end':
        pass
    else:
        del synch_set[:]
        my_set = [';', 'end', 'else']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, ';', 'else', 'end')


def peek_stack():
    return nodes[0]


def semantic_error(lexem):
    return "Semantic Error " + lexem + "does not exist in scope"


def variable():
    global line_number
    line_number = get_line_number()
    token = peek_token()
    line = tokens[0]
    stack = nodes
    if token == 'id':
        line = tokens[0]
        temp_type = ""
        error = ""
        variables = variable_types
        # looking_at_node = peek_stack()
        # while looking_at_node.right_sibling is not None:
        #     looking_at_node = looking_at_node.right_sibling
        #     if looking_at_node.data == line[1]:
        #         temp_type = looking_at_node.w_type
        #     else:
        #         error = semantic_error(line[1])
        # make sure is declare
        for node in nodes:
            if node.data == line[1]:
                if node.w_type == 'temptype':
                    temp_type = node.return_type
                    break
                else:
                    temp_type = node.w_type
                    break
        # if line[1] in variables:
        #     temp_type = variables[line[1]]
        match('id')

        is_array = variable_()
        if temp_type or is_array:
            return temp_type
        elif error:
            return error
    else:
        del synch_set[:]
        synch_set.append('assignop')
        handle_sync()
        syntax_error(token, 'id')


def variable_():
    token = peek_token()
    line = tokens[0]
    global line_number
    line_number = get_line_number()
    if token == '[':
        match('[')
        expression()
        match(']')
        return True
    elif token == 'assignop':
        pass
    else:
        del synch_set[:]
        synch_set.append('assignop')
        handle_sync()
        syntax_error(token, '[', 'assignop')
        return False


def expresslist():
    line = tokens[0]
    global line_number
    line_number = get_line_number()
    token = peek_token()

    if token == '(':
        expression()
        expresslist_()
    elif token == '+':
        expression()
        expresslist_()
    elif token == '-':
        expression()
        expresslist_()
    elif token == 'id':
        line = tokens[0]
        node = peek_stack()
        while node.right_sibling is not None:
            node = node.right_sibling
            if node.w_type == line[1]:
                print "Hey"
        expression()
        expresslist_()
    elif token == 'not':
        expression()
        expresslist_()
    elif token == 'integer' or token == 'real':
        expression()
        expresslist_()
    else:
        del synch_set[:]
        synch_set.append(')')

        handle_sync()
        syntax_error(token, '(', '+', '-', 'id', 'not', 'num')


def expresslist_():
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == ')':
        pass
    elif token == ',':
        match(',')
        expression()
        expresslist_()
    else:
        del synch_set[:]
        synch_set.append(')')
        handle_sync()
        syntax_error(token, ')', ',')


def expression():
    token = peek_token()
    line = tokens[0]
    global line_number
    line_number = get_line_number()
    if token == '(' or token == '+' or token == '-' or token == 'id' or token == 'not' or token == 'real' or token == 'integer':
        var_type = simpexpression()
        var_type2 = expression_(var_type)
        if var_type2:
            return var_type2
        else:
            return var_type
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, '(', '+', '-', 'id', 'not', 'num')
        return 0


def relop_error(line, v, v2):
    print "Relop Error: Line " + str(line) + " you can't compare a " + str(v) + " with " + str(v2)
    error = "Relop Error: Line " + str(line) + " you can't compare a " + str(v) + " with " + str(v2)
    new_list_file[int(line)].append(error)


def expression_(var_type):
    global line_number
    line_number = get_line_number()
    test = var_type
    line = tokens[0]
    token = peek_token()
    if token == ')':
        pass
    elif token == ',':
        pass
    elif token == ';':
        pass
    elif token == ']':
        pass
    elif token == 'do':
        pass
    elif token == 'else':
        pass
    elif token == 'end':
        pass
    elif token == 'relop':
        match('relop')
        variable_type = simpexpression()
        if variable_type == 'a-integer':
            variable_type = 'integer'
        elif variable_type == 'a-real':
            variable_type = 'real'
        if var_type != variable_type:
            relop_error(line_number, var_type, variable_type)
            return 'false'
        else:
            return 'true'
    elif token == 'then':
        pass
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, ')', ',', ';', ']', 'do', 'else', 'end', 'relop', 'then')


def simpexpression():
    token = peek_token()
    line = tokens[0]
    stack = nodes
    global line_number
    line_number = get_line_number()
    if token == '(':
        var_type = term()
        simpexpression_(var_type)
        return var_type
    elif token == '+':
        sign()
        var_type = term()
        simpexpression_(var_type)
        return var_type
    elif token == '-':
        sign()
        var_type = term()
        simpexpression_(var_type)
        return var_type
    elif token == 'id':
        var_type = term()
        simpexpression_(var_type)
        return var_type
    elif token == 'not':
        var_type = term()
        simpexpression_(var_type)
        return var_type
    elif token == 'real' or token == 'integer':
        var_type = term()
        simpexpression_(var_type)
        return var_type
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else', 'relop']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, '(', '+', '-', 'id', 'not', 'num')


def addop_error(line, v, e):
    print "ADDOP ERROR in line " + line + " You can't add " \
          + str(v) + " with a " + str(e)
    error = "ADDOP ERROR in line " + line + " You can't add " \
            + str(v) + " with a " + str(e)
    new_list_file[int(line)].append(error)


def simpexpression_(var_type):
    line = tokens[0]
    stack = nodes
    token = peek_token()
    global line_number
    line_number = get_line_number()
    if token == ')':
        pass
    elif token == ',':
        pass
    elif token == ';':
        pass
    elif token == ']':
        pass
    elif token == 'addop':
        match('addop')
        test = term()
        simpexpression_(var_type)
        testing = bool_flag
        if var_type == 'a-integer':
            var_type = 'integer'
        if var_type == 'a-real':
            var_type = 'real'
        if var_type is not None and test is not None:
            if var_type != test:
                addop_error(line_number, test, var_type)

    elif token == 'do':
        pass
    elif token == 'end':
        pass
    elif token == 'relop':
        pass
    elif token == 'then':
        pass
    elif token == 'else':
        pass
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else', 'relop']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, ')', ',', ';', ']', 'addop', 'do', 'end', 'relop', 'then')


def term():
    token = peek_token()
    line = tokens[0]
    global line_number
    line_number = get_line_number()
    if token == '(':
        var_type = factor()
        term_(var_type)
        return var_type
    elif token == 'id':
        var_type = factor()
        term_(var_type)
        return var_type
    elif token == 'not':
        var_type = factor()
        term_(var_type)
        return var_type
    elif token == 'integer' or token == 'real':
        var_type = factor()
        term_(var_type)
        return var_type
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else', 'relop', 'addop']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error('(', 'id', 'not', 'num')


def term_(var_type):
    global line_number
    line_number = get_line_number()
    token = peek_token()
    line = tokens[0]
    if token == ')':
        pass
    elif token == ',':
        pass
    elif token == ';':
        pass
    elif token == ']':
        pass
    elif token == 'addop':
        pass
    elif token == 'do':
        pass
    elif token == 'else':
        pass
    elif token == 'end':
        pass
    elif token == 'mulop':
        match('mulop')
        other_variable_type = factor()
        term_(var_type)

        if var_type != other_variable_type:
            mulop_error(line_number, var_type, other_variable_type)

    elif token == 'relop':
        pass
    elif token == 'then':
        pass
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else', 'relop', 'addop']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, ')', ',', ';', ']', 'addop', 'do', 'else', 'end', 'mulop', 'relop', 'then')


def mulop_error(line, v, v2):
    print "Mulop Error: Line " + str(line) + " you can't Multiply or Divide a " + str(v) + " with a " + str(v2)
    error = "Mulop Error: Line " + str(line) + " you can't Multiply or Divide a " + str(v) + " with a " + str(v2)
    new_list_file[int(line)].append(error)


def factor():
    line = tokens[0]
    token = peek_token()
    # node = nodes[0]
    stack = nodes
    checking = variable_types

    var_type = ""
    global line_number
    line_number = get_line_number()
    if token == '(':
        match('(')
        var_type = expression()
        match(')')
        return var_type
    elif token == 'id':
        check_scope(line[1], line_number)
        # fix this. next time. fix how is checking type
        for node in nodes:
            if node.data == line[1]:
                if node.w_type == 'temptype':
                    var_type = node.return_type
                    break
                else:
                    var_type = node.w_type
                    break
        # while node is not None:
        #     wtf = node.data
        #     v = line[1]
        #     if node.data == line[1]:
        #         var_type = node.w_type
        #     node = node.right_sibling
        # if var_type != 'integer' or var_type != 'real':
        #         if line[1] in variable_types:
        #             var_type = variable_types[line[1]]
        match('id')
        factor_(var_type)
        return var_type
    elif token == 'not':
        match('not')
        var_type = factor()
        return var_type
    elif token == 'integer' or token == 'real':
        match('num')
        var_type = token
        return var_type
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else', 'relop', 'addop', 'mulop']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, 'id', 'not', 'num')


def factor_(var_type):
    line = tokens[0]
    token = peek_token()
    node = peek_stack()
    global line_number
    line_number = get_line_number()
    if token == '(':

        match('(')
        expresslist()

        match(')')
        # return True
    elif token == ')':
        pass
    elif token == ',':
        pass
    elif token == ';':
        pass
    elif token == '[':
        match('[')
        expression()
        match(']')
        # return True
    elif token == ']':
        pass
    elif token == 'addop':
        pass
    elif token == 'do':
        pass
    elif token == 'else':
        pass
    elif token == 'end':
        pass
    elif token == 'mulop':
        pass
    elif token == 'relop':
        pass
    elif token == 'then':
        pass
    else:
        del synch_set[:]
        my_set = [']', ',', ')', 'then', 'do', ';', 'end', 'else', 'relop', 'addop', 'mulop']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, '(', ')', ',', ';', '[', ']', 'addop', 'do', 'else', 'end', 'mulop', 'relop', 'then')
        return False


def sign():
    global line_number
    line_number = get_line_number()
    token = peek_token()
    if token == '+':
        match('+')
    elif token == '-':
        match('-')
    else:
        del synch_set[:]
        my_set = ['id', 'num', 'not', '(']
        for i in my_set:
            synch_set.append(i)
        handle_sync()
        syntax_error(token, '+', '-')
