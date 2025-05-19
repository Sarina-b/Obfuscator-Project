import ply.yacc as yacc
from lexer import tokens
import random

class Node:
    def init(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

    def repr(self):
        return f"{self.type}({self.value}) -> {self.children}"

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_program(p):
    'program : declaration_list'
    p[0] = Node('program', [p[1]])

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 3:
        p[0] = Node('declaration_list', p[1].children + [p[2]])
    else:
        p[0] = Node('declaration_list', [p[1]])

def p_declaration(p):
    '''declaration : function_decl
                   | var_decl'''
    p[0] = p[1]

def p_var_decl(p):
        'var_decl : type_specifier ID SEMI'
        p[0] = Node('var_decl', [], (p[1], p[2]))

def p_type_specifier(p):
    '''type_specifier : INT
                          | CHAR_TYPE
                          | BOOL'''
    p[0] = p[1]

def p_function_decl(p):
        'function_decl : type_specifier ID LPAREN params RPAREN compound_stmt'
        p[0] = Node('function_decl', [p[4], p[6]], p[2])

def p_params(p):
        '''params : param_list
                  | empty'''
        p[0] = p[1]

def p_param_list(p):
        '''param_list : param_list COMMA param
                      | param'''
        if len(p) == 4:
            p[0] = Node('param_list', p[1].children + [p[3]])
        else:
            p[0] = Node('param_list', [p[1]])
def p_param(p):
    'param : type_specifier ID'
    p[0] = Node('param', [], (p[1], p[2]))

def p_compound_stmt(p):
    'compound_stmt : LBRACE declaration_list RBRACE'
    p[0] = Node('compound_stmt', [p[2]])

def p_empty(p):
    'empty :'
    p[0] = Node('empty')

def p_error(p):
    print("Syntax error at token:", p)

parser = yacc.yacc()