import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'CHAR', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN', 'EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA'
)

reserved = {
    'int': 'INT',
    'char': 'CHAR_TYPE',
    'bool': 'BOOL',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'printf': 'PRINTF',
    'scanf': 'SCANF'
}

tokens = list(tokens) + list(reserved.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='
t_EQ      = r'=='
t_NEQ     = r'!='
t_LT      = r'<'
t_GT      = r'>'
t_LEQ     = r'<='
t_GEQ     = r'>='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMMA   = r','

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_CHAR(t):
    r'\'(\\.|[^\\\n])\''
    t.value = t.value[1:-1]
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'//.*'
    pass

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()