__author__ = 'andreasbotero'


def match():
    pass

def parse():
    pass

def syntax_error():
    pass


def prg(token):
    if token == 'program':
        match('program')
        match('id')
        match('(')
        idlist()
        match(')')
        match(';')
        prg_()
    else:
        syntax_error()


def prg_(token):
    if token == 'begin':
        compstate()
        match('.')
    if token == 'function':
        subprgdeclarations()
        compstate()
        match('.')
    if token == 'var':
        declarations()
        prg__()


def prg__(token):
    if token == 'begin':
        compstate()
        match('.')
    if token == 'function':
        subprgdeclarations()
        compstate()

    
def idlist(token):
    if token == 'id':
        match('id')
        idlist_()


def idlist_(token):
    if token == ')':
        pass
    if token == ',':
        match('id')
        idlist_()


def declarations(toke):
    if toke == 'var':
        match('var')
        match('id')
        match(':')
        type_()
        match(';')
        declarations_()
    pass


def declarations_(token):
    if token == 'begin':
        pass
    if token == 'function':
        pass
    if token == 'var':
        match('var')
        match('id')
        match(':')
        type_()
        match(';')
        declarations_()


def type_(token):
    if token == 'array':
        match('array')
        match('[')
        match('num')
        match('..')
        match('num')
        match(']')
        match('of')
        standtype()
    if token == 'integer':
        standtype()
    if token == 'real':
        standtype()

    pass

def standtype(token):
    if token == 'integer':
        match('integer')
    if token == 'real':
        match('real')



def subprgdeclarations(token):
    if token == 'function':
        subprgdeclaration()
        match(';')
        subprgdeclarations_()


def subprgdeclarations_(token):
    if token == 'begin':
        pass
    if token == 'function':
        subprgdeclaration()
        match(';')
        subprgdeclarations_()


def subprgdeclaration(token):
    if token == 'function':
        subprghead()
        subprgdeclaration_()


def subprgdeclaration_(token):
    if token == 'begin':
        compstate()
    if token == 'function':
        declarations()
        subprgdeclaration__()
    if token == 'var':
        compstate()

    pass
    
def subprgdeclaration__():
    pass
    
def subprghead():
    pass

def subprghead_():
    pass
    
def arguments():
    pass

def paramlist():
    pass

def paramlist_():
    pass
    
def compstate():
    pass

def compstate_():
    pass
    
def optionalstate():
    pass

def statementlist():
    pass

def statementlist_():
    pass
    
def statement():
    pass

def statement_():
    pass
    
def variable():
    pass

def variable_():
    pass
    
def expresslist():
    pass

def expresslist_():
    pass
    
def expression():
    pass

def expression_():
    pass
    
def simpexpression():
    pass

def simpexpression_():
    pass
    
def term():
    pass

def term_():
    pass
    
def factor():
    pass

def factor_():
    pass
    
def sign():
    pass
