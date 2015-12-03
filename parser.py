__author__ = 'andreasbotero'

tokens = []


def add_tokens():
    with open('write_it.txt', 'r') as token_file:
        next(token_file)
        for line in token_file:
            tokens.append(line.replace(' ', '').split('|'))
    for item in tokens:
        print item


def peek_token():
    return tokens[0]


def get_token():
    return tokens.pop(0)


def match(expect_token):
    peek = peek_token()
    if peek == expect_token and peek != '$':
        get_token()
    elif peek == expect_token and peek == '$':
        print "PARSE COMPLETE"
    elif peek != expect_token:
        syntax_error()


def parse():
    add_tokens()
    prg()
    match('$')


def syntax_error():
    print "ERROR SYNTAX"


def prg():
    token = peek_token()
    if token == 'program':
        match('program')
        match('id')
        match('(')
        idlist()
        match(')')
        match(';')
        prg_()
    else:
        print "ERROR"


def prg_():
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
        syntax_error()


def prg__():
    token = peek_token()
    if token == 'begin':
        compstate()
        match('.')
    elif token == 'function':
        subprgdeclarations()
        compstate()


def idlist():
    token = peek_token()
    if token == 'id':
        match('id')
        idlist_()
    else:
        syntax_error()


def idlist_():
    token = peek_token()
    if token == ')':
        pass
    elif token == ',':
        match('id')
        idlist_()
    else:
        syntax_error()


def declarations():
    token = peek_token()
    if token == 'var':
        match('var')
        match('id')
        match(':')
        type_()
        match(';')
        declarations_()
    else:
        syntax_error()


def declarations_():
    token = peek_token()
    if token == 'begin':
        pass
    elif token == 'function':
        pass
    elif token == 'var':
        match('var')
        match('id')
        match(':')
        type_()
        match(';')
        declarations_()
    else:
        syntax_error()


def type_():
    token = peek_token()
    if token == 'array':
        match('array')
        match('[')
        match('num')
        match('..')
        match('num')
        match(']')
        match('of')
        standtype()
    elif token == 'integer':
        standtype()
    elif token == 'real':
        standtype()
    else:
        syntax_error()


def standtype():
    token = peek_token()
    if token == 'integer':
        match('integer')
    elif token == 'real':
        match('real')


def subprgdeclarations():
    token = peek_token()
    if token == 'function':
        subprgdeclaration()
        match(';')
        subprgdeclarations_()
    else:
        syntax_error()


def subprgdeclarations_():
    token = peek_token()
    if token == 'begin':
        pass
    elif token == 'function':
        subprgdeclaration()
        match(';')
        subprgdeclarations_()
    else:
        syntax_error()


def subprgdeclaration():
    token = peek_token()
    if token == 'function':
        subprghead()
        subprgdeclaration_()
    else:
        syntax_error()


def subprgdeclaration_():
    token = peek_token()
    if token == 'begin':
        compstate()
    elif token == 'function':
        declarations()
        subprgdeclaration__()
    elif token == 'var':
        compstate()
    else:
        syntax_error()


def subprgdeclaration__():
    token = peek_token()
    if token == 'begin':
        compstate()
    elif token == 'function':
        subprgdeclarations()
        compstate()
    else:
        print "ERROR"


def subprghead():
    token = peek_token()
    if token == 'function':
        match('function')
        match('id')
        subprghead_()
    else:
        print "ERROR"


def subprghead_():
    token = peek_token()
    if token == '(':
        arguments()
        match(':')
        standtype()
        match(';')
    elif token == ':':
        match(':')
        standtype()
        match(';')
    else:
        syntax_error()


def arguments():
    token = peek_token()
    if token == '(':
        match('(')
        paramlist()
        match(')')
    else:
        syntax_error()


def paramlist():
    token = peek_token()
    if token == 'id':
        match('id')
        match(':')
        type_()
        paramlist_()
    else:
        syntax_error()


def paramlist_():
    token = peek_token()
    if token == ')':
        pass
    elif token == ';':
        match(';')
        match('id')
        match(':')
        type_()
        paramlist_()
    else:
        syntax_error()


def compstate():
    token = peek_token()
    if token == 'begin':
        match('begin')
        compstate_()
    else:
        syntax_error()


def compstate_():
    token = peek_token()
    if token == 'begin':
        optionalstate()
        match('end')
    elif token == 'end':
        match('end')
    elif token == 'id':
        optionalstate()
        match('end')
    elif token == 'if':
        optionalstate()
        match('end')
    elif token == 'while':
        optionalstate()
        match('end')
    else:
        syntax_error()


def optionalstate():
    token = peek_token()
    if token == 'begin':
        statementlist()
    elif token == 'id':
        statementlist()
    elif token == 'if':
        statementlist()
    elif token == 'while':
        statementlist()
    else:
        syntax_error()


def statementlist():
    token = peek_token()
    if token == 'begin':
        statement()
        statementlist_()
    elif token == 'id':
        statement()
        statementlist_()
    elif token == 'if':
        statement()
        statementlist_()
    elif token == 'if':
        statement()
        statementlist_()
    else:
        syntax_error()


def statementlist_():
    token = peek_token()
    if token == ';':
        match(';')
        statement()
        statementlist_()
    elif token == 'end':
        pass
    else:
        syntax_error()


def statement():
    token = peek_token()
    if token == 'begin':
        compstate()
    elif token == 'id':
        variable()
        match('assignop')
        expression()
    elif token == 'if':
        match('if')
        expression()
        match('then')
        statement()
        statement_()
    elif token == 'while':
        match('while')
        expression()
        match('do')
        statement()
    else:
        syntax_error()


def statement_():
    token = peek_token()
    if token == ';':
        pass
    elif token == 'else':
        match('else')
        statement_()
    elif token == 'end':
        pass
    else:
        syntax_error()


def variable():
    token = peek_token()
    if token == 'id':
        match('id')
        variable_()
    else:
        syntax_error()


def variable_():
    token = peek_token()
    if token == '[':
        match('[')
        expression()
        match(']')
    elif token == 'assignop':
        pass
    else:
        syntax_error()


def expresslist():
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
        expression()
        expresslist_()
    elif token == 'not':
        expression()
        expresslist_()
    elif token == 'num':
        expression()
        expresslist_()
    else:
        syntax_error()


def expresslist_():
    token = peek_token()
    if token == ')':
        pass
    elif token == ',':
        match(',')
        expression()
        expresslist_()
    else:
        syntax_error()


def expression():
    token = peek_token()
    if token == '(':
        simpexpression()
        expression_()
    elif token == '+':
        simpexpression()
        expression_()
    elif token == '-':
        simpexpression()
        expression_()
    elif token == 'id':
        simpexpression()
        expression_()
    elif token == 'not':
        simpexpression()
        expression_()
    elif token == 'num':
        simpexpression()
        expression_()
    else:
        syntax_error()


def expression_():
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
        simpexpression()
    elif token == 'then':
        pass
    else:
        syntax_error()


def simpexpression():
    token = peek_token()
    if token == '(':
        term()
        simpexpression_()
    elif token == '+':
        sign()
        term()
        simpexpression_()
    elif token == '-':
        sign()
        term()
        simpexpression_()
    elif token == 'id':
        term()
        simpexpression_()
    elif token == 'not':
        term()
        simpexpression_()
    elif token == 'num':
        term()
        simpexpression_()
    else:
        syntax_error()


def simpexpression_():
    token = peek_token()
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
        term()
        simpexpression_()
    elif token == 'do':
        pass
    elif token == 'end':
        pass
    elif token == 'relop':
        pass
    elif token == 'then':
        pass
    else:
        syntax_error()


def term():
    token = peek_token()
    if token == '(':
        factor()
        term_()
    elif token == 'id':
        factor()
        term_()
    elif token == 'not':
        factor()
        term_()
    elif token == 'num':
        factor()
        term_()
    else:
        syntax_error()


def term_():
    token = peek_token()
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
        factor()
        term_()
    elif token == 'relop':
        pass
    elif token == 'then':
        pass
    else:
        syntax_error()


def factor():
    token = peek_token()
    if token == 'id':
        match('id')
        factor_()
    elif token == 'not':
        match('not')
        factor()
    elif token == 'num':
        match('num')
    else:
        syntax_error()


def factor_():
    token = peek_token()
    if token == '(':
        match('(')
        expresslist()
        match(')')
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
        syntax_error()


def sign():
    token = peek_token()
    if token == '+':
        match('+')
    elif token == '-':
        match('-')
    else:
        syntax_error()
