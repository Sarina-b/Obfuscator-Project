grammar MiniC;

program
    : (functionDecl | structDecl | varDecl)* EOF
    ;

// تابع
functionDecl
    : typ ID '(' paramList? ')' block
    ;

// ساختار struct
structDecl
    : 'struct' ID '{' varDecl* '}'
    ;

// تعریف متغیرها
varDecl
    : typ varDeclList ';'
    ;

varDeclList
    : varDeclItem (',' varDeclItem)*
    ;

varDeclItem
    : ID ('=' expression)?
    ;

// نوع داده (به جای type از typ استفاده شده)
typ
    : baseType pointerType*
    ;

baseType
    : 'int'
    | 'char'
    | 'bool'
    | ID           // برای struct type
    ;

pointerType
    : '*'
    ;

// لیست پارامترهای تابع
paramList
    : param (',' param)*
    ;

param
    : typ ID
    ;

// بلوک کد
block
    : '{' statement* '}'
    ;

// دستورات
statement
    : varDecl
    | assignStat
    | ifStat
    | whileStat
    | forStat
    | returnStat
    | funcCall ';'
    | ioStat ';'
    | block
    ;

// انتساب
assignStat
    : lvalue '=' expression ';'
    ;

lvalue
    : ID ( ('[' expression ']') | '.' ID | pointerDereference )*
    ;

pointerDereference
    : '->' ID
    ;

// if-else
ifStat
    : 'if' '(' expression ')' statement ('else' statement)?
    ;

// while
whileStat
    : 'while' '(' expression ')' statement
    ;

// for
forStat
    : 'for' '(' (varDecl | assignStat | ';') expression? ';' expression? ')' statement
    ;

// return
returnStat
    : 'return' expression? ';'
    ;

// تابع فراخوانی
funcCall
    : ID '(' argumentList? ')'
    ;

argumentList
    : expression (',' expression)*
    ;

// ورودی/خروجی: scanf و printf
ioStat
    : 'scanf' '(' STRING ',' '&'? ID ')'
    | 'printf' '(' STRING (',' expressionList)? ')'
    ;

expressionList
    : expression (',' expression)*
    ;

// عبارات (بیان ساده، می‌شه توسعه داد)
expression
    : expression ('*' | '/' | '%') expression
    | expression ('+' | '-') expression
    | expression ('<' | '<=' | '>' | '>=') expression
    | expression ('==' | '!=') expression
    | expression ('&&' | '||') expression
    | unaryOp expression
    | '(' expression ')'
    | literal
    | funcCall
    | lvalue
    ;

unaryOp
    : '!'
    | '-'
    ;

literal
    : INT
    | CHAR
    | BOOL
    ;

// ترمینال‌ها
BOOL
    : 'true'
    | 'false'
    ;

INT
    : [0-9]+
    ;

CHAR
    : '\'' . '\''
    ;

STRING
    : '"' (~["\\] | '\\' .)* '"'
    ;

// شناساگرها (tokens)
ID
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

