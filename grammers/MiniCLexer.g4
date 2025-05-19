lexer grammar MiniCLexer;

fragment LETTER     : [a-zA-Z_] ;
fragment DIGIT      : [0-9] ;

ID              : LETTER (LETTER | DIGIT)* ;
INT_LITERAL     : DIGIT+ ;
CHAR_LITERAL    : '\'' . '\'' ;
BOOL_LITERAL    : 'true' | 'false' ;
STRING_LITERAL  : '"' .*? '"' ;

// Keywords
STRUCT          : 'struct' ;
IF              : 'if' ;
ELSE            : 'else' ;
WHILE           : 'while' ;
FOR             : 'for' ;
RETURN          : 'return' ;
PRINTF          : 'printf' ;
SCANF           : 'scanf' ;
INT             : 'int' ;
CHAR            : 'char' ;
BOOL            : 'bool' ;

// Operators and symbols
PLUS            : '+' ;
MINUS           : '-' ;
STAR            : '*' ;
DIV             : '/' ;
ASSIGN          : '=' ;
EQUAL           : '==' ;
NOTEQUAL        : '!=' ;
LT              : '<' ;
GT              : '>' ;
LE              : '<=' ;
GE              : '>=' ;
AND             : '&&' ;
OR              : '||' ;
NOT             : '!' ;
DOT             : '.' ;

LPAREN          : '(' ;
RPAREN          : ')' ;
LBRACE          : '{' ;
RBRACE          : '}' ;
SEMI            : ';' ;
COMMA           : ',' ;

// Whitespace and comments
WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '//' ~[\r\n]* -> skip ;
