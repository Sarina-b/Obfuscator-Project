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

    parser = yacc.yacc()